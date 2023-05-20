# Generated by Django 4.2.1 on 2023-05-20 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('actual_price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('total_units', models.PositiveIntegerField()),
                ('available_units', models.PositiveIntegerField()),
                ('is_lightning_deal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LightningDeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_time', models.DateTimeField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lightning_deal', to='product.product')),
            ],
        ),
    ]