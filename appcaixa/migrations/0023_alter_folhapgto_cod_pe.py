# Generated by Django 5.0.6 on 2024-07-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0022_folhapgto_id_forma_pgtos_folhapgto_id_movimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folhapgto',
            name='cod_pe',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
