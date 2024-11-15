from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import CustomUser, Category, Application


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

class ApplicationAdminForm(forms.ModelForm):
    done_status_image = forms.ImageField(required=False,
                                    label='Фото готового дизайна (добавить, если статус меняется на "Выполнено")')
    comment = forms.CharField(required=False,
                              label='Комментарий к работе (добавить, если статус меняется на "Принято на работу")',
                              widget=forms.Textarea)

    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['image']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        current_status = self.instance.status if self.instance else None

        if current_status in ['P', 'D'] and status != current_status:
            raise ValidationError("Вы не можете поменять статус заявки, если она имеет статус 'Принято в работу' или 'Выполнено'")

        if status == 'P' and not cleaned_data.get('comment'):
            raise ValidationError('Добавьте комментарий')

        if status == 'D' and not cleaned_data.get('done_status_image'):
            raise ValidationError('Добавьте фото готового дизайна')

        return cleaned_data

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationAdminForm
    list_display = ('title', 'applicant', 'status', 'date', 'category', 'favorite')
    readonly_fields = ('applicant', 'title', 'description', 'category', 'date')
    exclude = ['image']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj:
            status = obj.status

            if status == 'P':
                if 'done_status_image' in form.base_fields:
                    form.base_fields['done_status_image'].required = False
                    del form.base_fields['done_status_image']

            elif status == 'D':
                if 'comment' in form.base_fields:
                    form.base_fields['comment'].required = False
                    del form.base_fields['comment']

        return form

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            obj.comment = form.cleaned_data.get('comment', '')
            obj.done_status_image = form.cleaned_data.get('done_status_image', None)
            with transaction.atomic():
                obj.save()

    def get_readonly_field(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and obj.status != 'D':
            readonly_fields += ('favorite')
        return readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
