from django.db import models


# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=32, default='', blank=False, null=False)
    last_name = models.CharField(max_length=32, default='', blank=True, null=True)
    pan = models.CharField(blank=False, null=False, max_length=10)
    # date_of_birth = models.DateTimeField(auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
