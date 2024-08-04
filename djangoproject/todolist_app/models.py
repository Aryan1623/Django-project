from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tasklist(models.Model):
    task = models.CharField(max_length=3000)
    done = models.BooleanField(default=False)
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def __str__(self):
     return self.task + '-' + str(self.done)
