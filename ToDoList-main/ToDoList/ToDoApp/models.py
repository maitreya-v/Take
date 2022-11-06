from email.policy import default
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 244 )
    descript = models.TextField()
    #deadline = models.TimeField()
    # priority = models.IntegerField()
    image = models.ImageField(upload_to='test/',null=True)
    def __str__(self) :
        return self.title

    
class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('A Email is necessary')
        if not password:
            raise ValueError('A password is necessary')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,email,password):
        user= self.create_user(
            email,
            password=password,
        )
        user.staff=True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff= True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects= UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) :
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin