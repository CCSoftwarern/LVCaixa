# Generated by Django 5.0.6 on 2024-06-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0003_folhapgto_id_folha_alter_folhapgto_id_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='folhapgto',
            name='data_pgto',
            field=models.DateField(null=True),
        ),
    ]
