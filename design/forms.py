from cProfile import label

from django import forms
from django.contrib.auth.password_validation import password_changed
from django.core.exceptions import ValidationError

from .models import CustomUser, Application


class CustomUserCreatingForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя", max_length=150)
    email = forms.EmailField(label="Адрес электронной почты", max_length=150)
    first_name = forms.CharField(label="Имя", max_length=150)
    last_name = forms.CharField(label="Фамилия", max_length=150)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердить пароль", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Такое имя пользователя занято.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Такой адрес электронной почты занят.")
        return email

    def clean(self):
        super().clean()
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Пароли не совпадают")

        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
            return user

    class Meta:
        model = CustomUser
        fields = ('username', "email", "first_name", "last_name", 'gender')
        widgets = {
            'gender': forms.RadioSelect
        }

class ApplicationForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок заявки', widget=forms.TextInput)
    description = forms.CharField(label='Описание заявки', widget=forms.Textarea)
    category = forms.ChoiceField(label='Категория заявки', widget=forms.Select)
    image = forms.FileField(label='Фото заявки', widget=forms.FileInput)