# Generated by Django 2.2.15 on 2020-08-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cui', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('pedido', models.IntegerField(default=0)),
            ],
        ),
    ]
