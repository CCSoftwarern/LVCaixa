# Generated by Django 5.0.6 on 2024-07-12 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0024_remove_folhapgto_cod_pe'),
    ]

    operations = [
        migrations.AddField(
            model_name='folhapgto',
            name='codigo_pe',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
    ]
