from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class ClientProfileManager(BaseUserManager):  
  def create_client(self,email, name, password=None):
    # ''' Crear nuevo client profile '''
    if not email:
      raise ValueError('User should contain an email address')
    
    email = self.normalize_email(email)
    user = self.model(email = email, name=name)
    
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  
  def create_superuser(self,email, name, password):
    
    user = self.create_client(email = email, name=name)
    
    user.is_superuser =True
    user.is_staff =True
    user.save(using=self._db)
    
    return user



class ClientProfile(AbstractBaseUser, PermissionsMixin):
  # Modelo base de datos de clientes en el sistema 
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True) 
  # Este campo verifica si el usuario se encuentra activo o inactivo para la administracion de su perfil
  is_staff = models.BooleanField(default=False)
  
  
  objects = ClientProfileManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']
  
  def get_full_name(self):
    return self.name
  
  


  


