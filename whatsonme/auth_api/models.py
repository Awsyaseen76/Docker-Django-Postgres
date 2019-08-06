from django.db import models

# Create your models here.
class Auth(models.Model):
    user_name = models.CharField(max_length=128)
    email = models.EmailField()
    role = models.CharField(max_length=128, default='Member')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
