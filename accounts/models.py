from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None,password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("please enter an email")
        if not password:
            raise ValueError("please enter a password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.full_name = full_name
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save()
        return user_obj

    def create_staffuser(self,email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, full_name,email, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff= True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        else:
            return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    def is_admin(self):
        return self.admin

    def is_active(self):
        return self.active


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.email


