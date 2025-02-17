# Generated by Django 4.2 on 2025-01-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.client')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ['-ordered_at'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('picture', models.ImageField(upload_to='')),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=1)),
                ('description', models.TextField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minha_lanchonete.product')),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
                'db_table': 'pizza',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=12, unique=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.client')),
            ],
            options={
                'verbose_name': 'PaymentMethod',
                'verbose_name_plural': 'PaymentMethods',
                'db_table': 'payment_method',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minha_lanchonete.order')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minha_lanchonete.product')),
            ],
            options={
                'verbose_name': 'OrderProduct',
                'verbose_name_plural': 'OrderProducts',
                'db_table': 'order_product',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='id_payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minha_lanchonete.paymentmethod'),
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('volume', models.IntegerField()),
                ('type', models.CharField(max_length=22)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minha_lanchonete.product')),
            ],
            options={
                'verbose_name': 'Drink',
                'verbose_name_plural': 'Drinks',
                'db_table': 'drink',
                'ordering': ['-id'],
                'managed': True,
            },
        ),
    ]
