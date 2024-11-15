from django.db import models
<<<<<<< HEAD
from django.contrib import auth

# Create your models here.
class User(auth.models.AbstractUser):
=======
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
>>>>>>> origin/master
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
<<<<<<< HEAD
        return self.first_name + ' ' + self.last_name
=======
        return self.first_name + ' ' + self.last_name
>>>>>>> origin/master
