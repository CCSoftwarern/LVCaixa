# Generated by Django 5.0.6 on 2024-06-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0004_folhapgto_data_pgto'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimento',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movimento',
            name='id_cliente',
            field=models.IntegerField(default=0),
        ),
    ]
