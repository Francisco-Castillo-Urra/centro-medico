# Generated by Django 4.1.13 on 2023-11-30 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Es super usuario')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Es staff')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Ultimo inicio de sesion')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', manager.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('hora_ini', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('valor_mensual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prevision', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('rut_pro', models.IntegerField(primary_key=True, serialize=False, verbose_name='RUT')),
                ('primer_nombre_pro', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('segundo_nombre_pro', models.CharField(max_length=50, verbose_name='Segundo nombre')),
                ('apellido_paterno_pro', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apellido_materno_pro', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('direccion_pro', models.CharField(max_length=50, verbose_name='Direccion')),
                ('celular_pro', models.IntegerField(verbose_name='Celular')),
                ('tarifa', models.IntegerField(verbose_name='Tarifa')),
                ('fecha_registro_pro', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.ciudad')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut_paciente', models.IntegerField(primary_key=True, serialize=False, verbose_name='RUT')),
                ('primer_nombre_pac', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('segundo_nombre_pac', models.CharField(max_length=50, verbose_name='Segundo nombre')),
                ('apellido_paterno_pac', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apellido_materno_pac', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('orden_apellido', models.BooleanField(default=False, verbose_name='Invertir el orden de los apellidos')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('direccion_pac', models.CharField(max_length=50, verbose_name='Direccion')),
                ('celular_pac', models.IntegerField(verbose_name='Celular')),
                ('fecha_registro_pac', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('nombre_social', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre social')),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manager.ciudad')),
                ('prevision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.prevision')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_contrato', models.DateField(default=django.utils.timezone.now)),
                ('valor_mensual', models.IntegerField()),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('rut_pro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.profesional')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateField(default=django.utils.timezone.now)),
                ('fecha_atencion', models.DateField()),
                ('tarifa', models.IntegerField()),
                ('atendido', models.BooleanField(default=False)),
                ('pagado', models.BooleanField(default=False)),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.bloque')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.profesional')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.paciente')),
            ],
        ),
        migrations.AddConstraint(
            model_name='agenda',
            constraint=models.UniqueConstraint(fields=('fecha_atencion', 'bloque', 'medico'), name='pk_constraint'),
        ),
    ]
