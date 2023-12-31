# Generated by Django 4.2.2 on 2023-07-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_contactus_description_alter_contactus_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(choices=[('پیشنهاد', 'پیشنهاد'), ('CRITIC', 'انتقاد'), ('FOLLOW', 'پیگیری'), ('OTHER', 'سایر موضوعات')], max_length=150, verbose_name='عنوان'),
        ),
    ]
