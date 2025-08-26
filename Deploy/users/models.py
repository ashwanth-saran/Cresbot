from django.db import models
from django.contrib.auth.models import User






    
class Chatbot(models.Model):
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.message

