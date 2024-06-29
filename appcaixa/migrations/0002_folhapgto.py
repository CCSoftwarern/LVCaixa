# Generated by Django 5.0.6 on 2024-06-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcaixa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='folhapgto',
            fields=[
                ('hora_lancamento', models.TimeField(auto_now_add=True)),
                ('id_cliente', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nm_cliente', models.CharField(max_length=100)),
                ('ACC', models.IntegerField(default=0, null=True)),
                ('Categoria_A', models.IntegerField(default=0, null=True)),
                ('Categoria_B', models.IntegerField(default=0, null=True)),
                ('Categoria_C', models.IntegerField(default=0, null=True)),
                ('Categoria_D', models.IntegerField(default=0, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.IntegerField(default=0, null=True)),
                ('dt_lancamento', models.DateField(auto_now_add=True)),
                ('forma_pgto', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]