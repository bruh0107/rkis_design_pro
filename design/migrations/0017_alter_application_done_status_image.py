# Generated by Django 4.2.16 on 2024-11-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0016_application_design_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='done_status_image',
            field=models.FileField(blank=True, null=True, upload_to='admin_photo/', verbose_name='Фото готового дизайна'),
        ),
    ]
