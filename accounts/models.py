from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None):
        if not email:
            raise ValueError("please enter an email")
        if not password:
            raise ValueError("please enter a password")

        user_obj = self.model(
            email=self.normalize_email(email)

        )
        user_obj.full_name = full_name
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,email, full_name=None, password=None,):
        user = self.create_user(
            email = email,
            full_name=full_name,
            password=password,
        )
        user.is_admin = False
        user.is_staff = True
        user.is_superuser = False
        # group = Group.objects.get(name='staff')
        # user.groups.add(group)
        my_group = Group.objects.get(name='staff')
        my_group.user_set.add(user)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,full_name,password=None):
        user = self.create_user(
            email= email,
            full_name= full_name,
            password= password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
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
        return self.is_admin

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.email


