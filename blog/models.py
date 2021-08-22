from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(     #for many to one relationships
        'auth.User',         # the built in user model that django provide fo auth
        on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):   # what the string that is printed with object call
        return self.title
        
