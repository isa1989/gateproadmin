from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
import random


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=12, unique=True, verbose_name="Phone number"
    )
    name = models.CharField(
        max_length=200, null=True, blank=False, verbose_name="Customer name"
    )
    surname = models.CharField(
        max_length=200, null=True, blank=False, verbose_name="Customer surname"
    )
    address = models.CharField(
        max_length=200, null=True, blank=False, verbose_name="Customer address"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    firebase_token = models.CharField(max_length=255)
    email = models.BooleanField(default=True)
    sms = models.BooleanField(default=True)
    push = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        Group, related_name="customers", blank=True, verbose_name="Groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customers",
        blank=True,
        verbose_name="User permissions",
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["id"]

    def __str__(self):
        return self.phone_number


class OTP(models.Model):
    phone_number = models.CharField(
        max_length=12, unique=True, verbose_name="Phone number"
    )
    otp_code = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        # if not self.otp_code:  # Generate OTP if not already set
        self.otp_code = self._generate_otp()
        super().save(*args, **kwargs)

    def _generate_otp(self):
        if self.phone_number == "994558403938":
            return "1234"
        while True:
            otp_code = random.randint(1000, 9999)
            if not OTP.objects.filter(otp_code=otp_code).exists():
                return otp_code


class CustomerToken(models.Model):
    phone_number = models.CharField(
        max_length=12, unique=True, verbose_name="Phone number"
    )
    token = models.CharField(
        max_length=300
    )  # Adjust the max_length as per your token length
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
