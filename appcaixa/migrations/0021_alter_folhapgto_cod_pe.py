# Generated by Django 5.0.6 on 2024-07-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0020_folhapgto_id_instrutor_folhapgto_nm_instrutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folhapgto',
            name='cod_pe',
            field=models.CharField(max_length=50),
        ),
    ]