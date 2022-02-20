# Generated by Django 3.2.4 on 2021-08-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0015_alter_menu_item_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='category_type',
            field=models.CharField(choices=[('category1', 'pizza'), ('category2', 'steak'), ('category3', 'burger'), ('category4', 'juice'), ('category5', 'rice'), ('category6', 'pasta')], max_length=50, null=True),
        ),
    ]
