# Generated by Django 4.2.2 on 2023-07-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_payment_amount_paid_remove_payment_cart_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=100, verbose_name='آدرس گیرنده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=250, verbose_name='کد پستی'),
        ),
    ]
