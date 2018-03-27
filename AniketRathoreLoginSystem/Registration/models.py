from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username
