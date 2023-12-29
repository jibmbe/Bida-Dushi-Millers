# Generated by Django 4.2.7 on 2023-12-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='buyer_email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_name',
            field=models.CharField(default='John Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
