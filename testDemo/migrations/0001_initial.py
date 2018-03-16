# Generated by Django 2.0.3 on 2018-03-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alipay',
            fields=[
                ('pay_ment_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=15)),
                ('is_operate', models.CharField(max_length=5)),
                ('pay_time', models.CharField(max_length=20)),
            ],
        ),
    ]