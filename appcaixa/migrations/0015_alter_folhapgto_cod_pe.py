# Generated by Django 5.0.6 on 2024-06-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0014_alter_clientes_cpf_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folhapgto',
            name='cod_pe',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
