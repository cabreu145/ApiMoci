# Generated by Django 3.2 on 2021-04-06 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='encuesta_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('nombre', models.CharField(max_length=150)),
                ('seccion', models.IntegerField()),
                ('manzana', models.IntegerField()),
                ('colonia', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('pregunta_1', models.CharField(max_length=300)),
                ('pregunta_2', models.CharField(max_length=300)),
                ('pregunta_3', models.CharField(max_length=300)),
                ('pregunta_4', models.CharField(max_length=300)),
                ('pregunta_5', models.CharField(max_length=300)),
                ('edad', models.IntegerField()),
                ('g_estudios', models.CharField(max_length=50)),
                ('e_civil', models.CharField(max_length=20)),
                ('ocupacion', models.CharField(max_length=80)),
                ('ing_prom', models.IntegerField()),
                ('acc_prog', models.CharField(max_length=200)),
                ('lim_fis', models.CharField(max_length=200)),
                ('cred_vot', models.CharField(max_length=10)),
                ('observaciones', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
                'db_table': 'encuesta_1',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
            },
        ),
    ]