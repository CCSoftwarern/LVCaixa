# Generated by Django 5.0.6 on 2024-06-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0013_alter_folhapgto_nm_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cpf_cnpj',
            field=models.CharField(max_length=22, unique=True),
        ),
    ]