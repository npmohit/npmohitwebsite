# Generated by Django 4.2.2 on 2023-07-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_payment_cart_id_alter_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checkout.order', verbose_name='سفارش'),
            preserve_default=False,
        ),
    ]
