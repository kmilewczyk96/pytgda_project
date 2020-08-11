import uuid
from random import randint
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserQuerySet(UserManager):
    pass


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    personal_token = models.CharField(
        verbose_name="Personal token",
        max_length=5, null=False, blank=False, unique=False,
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.personal_token:
            personal_token = randint(1000, 9999)
            self.personal_token = '#' + str(personal_token)
        return super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=uuid.uuid4, related_name="posts")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-last_edit_date']