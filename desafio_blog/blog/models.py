from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    author = models.TextField()
    image = models.ImageField(upload_to='static/')
    content = models.TextField()