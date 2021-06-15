from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, contact, address, password, **other_fields):
        if not email:
            raise ValueError('You must provide an Email Address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                            contact=contact,
                            address=address, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, contact, address, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not contact:
            raise ValueError("User must have a contact")
        if not address:
            raise ValueError("User must have a address")
        if not other_fields.get('is_staff'):
            raise ValueError("SuperUser must have assigned is_staff=True")
        if not other_fields.get('is_superuser'):
            raise ValueError("SuperUser must have assigned is_superuser=True")

        user = self.model(
            email=self.normalize_email(email), **other_fields)
        user.contact = contact
        user.address = address
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=125)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(blank=True, max_length=500)
    contact = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'contact', 'address']


    def __str__(self) -> str:
        return str(self.username)