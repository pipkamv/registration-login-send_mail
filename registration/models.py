from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey
    date_of_birth = models.DateField(blank='Мээрим Бегалиева', null=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)




