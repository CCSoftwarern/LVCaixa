# Generated by Django 5.0.6 on 2024-07-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0025_folhapgto_codigo_pe'),
    ]

    operations = [
        migrations.AddField(
            model_name='folhapgto',
            name='nm_categoria',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
