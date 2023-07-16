# Generated by Django 4.2.2 on 2023-07-04 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50, verbose_name='شناسه')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال؟')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبدهای خرید',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, verbose_name='شماره سفارش')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(max_length=20, verbose_name='تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('country', models.CharField(max_length=50, verbose_name='کشور')),
                ('state', models.CharField(max_length=50, verbose_name='استان')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('status', models.CharField(choices=[('New', 'جدید'), ('Accepted', 'پذیرفته شده'), ('Completed', 'تکمیل شده'), ('Cancelled', 'لغو شده')], default='New', max_length=50, verbose_name='وضعیت')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='جمع کل')),
                ('paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='پرداخت')),
                ('ip', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, verbose_name='شناسه پرداخت')),
                ('payment_method', models.CharField(max_length=50, verbose_name='روش پرداخت')),
                ('amount_paid', models.CharField(max_length=50, verbose_name='مقدار')),
                ('status', models.CharField(max_length=50, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(verbose_name='تاریخ ثبت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت\u200cها',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='مقدار')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'قلم سفارش',
                'verbose_name_plural': 'اقلام سفارشات',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.payment', verbose_name='پرداخت'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='مقدار')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال؟')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.cart', verbose_name='سبد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'قلم',
                'verbose_name_plural': 'اقلام خرید',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('phone_number', models.CharField(max_length=20, verbose_name='تلفن')),
                ('country', models.CharField(default='ایران', max_length=50, verbose_name='کشور')),
                ('state', models.CharField(max_length=50, verbose_name='استان')),
                ('city', models.CharField(max_length=50, verbose_name='شهر')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('zip_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس\u200cها',
            },
        ),
    ]
