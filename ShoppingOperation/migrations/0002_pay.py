# Generated by Django 2.0.2 on 2018-05-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingOperation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.CharField(max_length=10000)),
                ('box', models.CharField(max_length=10000)),
                ('sum', models.CharField(max_length=10000)),
            ],
        ),
    ]
