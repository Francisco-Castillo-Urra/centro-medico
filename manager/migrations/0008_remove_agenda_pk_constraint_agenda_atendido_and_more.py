# Generated by Django 4.2.6 on 2023-11-15 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_agenda_pk_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='agenda',
            name='pk_constraint',
        ),
        migrations.AddField(
            model_name='agenda',
            name='atendido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agenda',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.UniqueConstraint(fields=('fecha_atencion', 'bloque', 'medico'), name='pk_constraint'),
        ),
    ]