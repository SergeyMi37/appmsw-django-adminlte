# Generated by Django 4.2.6 on 2024-01-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmsw', '0007_alter_comment_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Image'),
        ),
    ]
