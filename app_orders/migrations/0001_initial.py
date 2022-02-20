# Generated by Django 3.1.7 on 2021-06-10 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='MenuFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'verbose_name': 'Menu Field',
                'verbose_name_plural': 'Menu Fields',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Table',
                'verbose_name_plural': 'Table',
            },
        ),
        migrations.CreateModel(
            name='MenuUpdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('updated_fields', models.ManyToManyField(to='app_orders.MenuFields')),
                ('updated_menu', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_orders.menu')),
            ],
            options={
                'verbose_name': 'Menu Update',
                'verbose_name_plural': 'Menu Updates',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='updates',
            field=models.ManyToManyField(default=None, to='app_orders.MenuUpdates'),
        ),
    ]
