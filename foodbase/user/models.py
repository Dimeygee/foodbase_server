from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
import uuid


class UserManager(BaseUserManager):
    def create_user(self,email,phonenumber,username=None,password=None):
        if email is None:
            raise ValueError('Users must have email')

        if phonenumber is None:
            raise ValueError('Users must have an Phonenumbe.')


        user = self.model(
                email=self.normalize_email(email),
                phonenumber=phonenumber,
                username=username,
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,phonenumber,username=None,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            phonenumber=phonenumber,
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user 


class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(db_index=True,unique=True)
    phonenumber = models.IntegerField(db_index=True,unique=True) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber']

    objects = UserManager()

    #def get_full_name(self):
    #    return f"{self.first_name} {self.last_name}"


class MyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="p_default.jpg",upload_to="profile")
    fullname=models.CharField(max_length=100,blank=True)
    

#This is a wrong name actually but i'll leave it at this. lol
class OtpVerifier(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=100,null=True,blank=True)
    counter=models.PositiveIntegerField(default=0)
