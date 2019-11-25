# Generated by Django 2.2.7 on 2019-11-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_auto_20191117_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_taxa', models.CharField(blank=True, max_length=30, null=True)),
                ('valor_taxa', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
