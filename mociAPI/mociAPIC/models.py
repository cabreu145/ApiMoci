from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para Perfiles de Usuario """
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')

        email= self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo Basde de Datos para Usuarios en el Sistema """
    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' Obtener Nombre Completo del Usuario'''
        return self.name

    def get_short_name(self):
        '''Obtener Nombre Corto del Usuario '''
        return self.name

    def __str__(self):
        '''Retornar Cadena Representando Nuestro Usuario ''' 
        return self.email
    class Meta:
        db_table="usuarios"
        verbose_name = u'Usuario'
        verbose_name_plural = u'Usuarios'

class encuesta_1(models.Model):
    fecha_hora=models.DateTimeField(default=now, editable=False)
    nombre=models.CharField(max_length=150)
    seccion=models.IntegerField()
    manzana=models.IntegerField()
    colonia=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    pregunta_1=models.CharField(max_length=300)
    pregunta_2=models.CharField(max_length=300)
    pregunta_3=models.CharField(max_length=300)
    pregunta_4=models.CharField(max_length=300)
    pregunta_5=models.CharField(max_length=300)
    edad=models.IntegerField()
    g_estudios=models.CharField(max_length=50)
    e_civil=models.CharField(max_length=20)
    ocupacion=models.CharField(max_length=80)
    ing_prom=models.IntegerField()
    acc_prog=models.CharField(max_length=200)
    lim_fis=models.CharField(max_length=200)
    cred_vot=models.CharField(max_length=10)
    observaciones=models.CharField(max_length=500)
    class Meta:
        db_table="encuesta_1"
        verbose_name = u'Encuesta'
        verbose_name_plural = u'Encuestas'
    def __str__(self):
        return self.nombre
