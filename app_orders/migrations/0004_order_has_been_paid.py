# Generated by Django 3.1.7 on 2021-06-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0003_auto_20210625_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='has_been_paid',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
    ]
