# Generated by Django 4.2.16 on 2024-11-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_alter_customuser_email_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1, verbose_name='Пол'),
        ),
    ]