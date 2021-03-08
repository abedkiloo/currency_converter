import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# Create your models here.
from django.urls import reverse


class MyAccountManager(BaseUserManager):
    def create_user(self, email, user_name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            user_name=user_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True)
    user_name = models.CharField(max_length=30, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('user', kwargs={id: self.pk})


MyUser = get_user_model()
