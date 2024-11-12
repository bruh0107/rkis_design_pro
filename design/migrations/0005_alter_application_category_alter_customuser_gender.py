# Generated by Django 4.2.16 on 2024-11-12 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_category_alter_customuser_gender_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='category',
            field=models.ForeignKey(default='O', on_delete=django.db.models.deletion.CASCADE, to='design.category', verbose_name='Категория заявки'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1, verbose_name='Пол'),
        ),
    ]
