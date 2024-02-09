from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    author = models.TextField()
    image = models.ImageField(upload_to='images/')
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body