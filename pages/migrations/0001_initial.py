# Generated by Django 4.2.2 on 2023-07-12 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomProductRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('files', models.FileField(blank=True, null=True, upload_to='requests/', verbose_name='بارگذاری فایل')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت درخواست')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='متقاضی')),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست\u200cها',
            },
        ),
    ]