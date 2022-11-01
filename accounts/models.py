from django.db import models
from django.contrib.auth import models as auth_models


def filePath(instance, filename):
    return f'{instance.username}/profile.png'


class UserManager(auth_models.BaseUserManager):
    def create_user(self, name: str, username: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> 'User':
        if not email:
            raise ValueError('User must have an email')
        if not name:
            raise ValueError('User must have a name')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, name: str, username: str, email: str, password: str = None) -> 'User':
        user = self.create_user(
            name=name,
            email=email,
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    name = models.CharField(verbose_name='Name', max_length=255)
    username = models.CharField(verbose_name='Username', max_length=50, unique=True)
    email = models.CharField(verbose_name='Email', max_length=255, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100)
    birthdate = models.DateField(verbose_name='Birth Date', null=True)
    profilePic = models.ImageField(upload_to=filePath, blank=True, null=True)
    teacher = models.BooleanField(default=False)

    createdAt = models.DateField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def save(self, *args, **kwargs):
        self.username = self.username.lower().strip()
        self.email = self.email.lower().strip()
        return super(User, self).save(*args, **kwargs)
