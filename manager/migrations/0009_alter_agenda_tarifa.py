# Generated by Django 4.2.6 on 2023-11-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_remove_agenda_pk_constraint_agenda_atendido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='tarifa',
            field=models.IntegerField(editable=False),
        ),
    ]