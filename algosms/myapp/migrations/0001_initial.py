# Generated by Django 5.0.4 on 2024-05-18 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_SYMBOL_QTY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('SYMBOL', models.CharField(blank=True, max_length=50, null=True)),
                ('QUANTITY', models.FloatField(blank=True, null=True)),
                ('trade', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='b0f4ac52', max_length=8, unique=True)),
                ('name_first', models.CharField(blank=True, max_length=50, null=True)),
                ('name_last', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('verify_code', models.CharField(blank=True, max_length=15, null=True)),
                ('date_joined', models.DateTimeField(default=None, verbose_name='date joined')),
                ('last_login', models.DateTimeField(default=None, verbose_name='last login')),
                ('is_staff', models.BooleanField(default=False)),
                ('clint_status', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.clientdetail', to_field='user_id')),
            ],
        ),
        migrations.CreateModel(
            name='SYMBOL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SYMBOL', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientSignal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(blank=True, max_length=50, null=True)),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('message_id', models.CharField(blank=True, max_length=50, null=True)),
                ('ids', models.CharField(blank=True, max_length=50, null=True)),
                ('TYPE', models.CharField(choices=[('BUY_ENTRY', 'BUY_ENTRY'), ('BUY_EXIT', 'BUY_EXIT'), ('SELL_ENTRY', 'SELL_ENTRY'), ('SELL_EXIT', 'SELL_EXIT')], max_length=10)),
                ('QUANTITY', models.FloatField(blank=True, null=True)),
                ('ENTRY_PRICE', models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True)),
                ('EXIT_PRICE', models.DecimalField(blank=True, decimal_places=5, max_digits=12, null=True)),
                ('profit_loss', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cumulative_pl', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('SYMBOL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_signals', to='myapp.symbol')),
            ],
        ),
    ]