from django.db import models








class Games(models.Model):
    image = models.ImageField(upload_to='games/')
    title = models.CharField(max_length=300)
    describtions = models.TextField()
    price = models.CharField(max_length=300)


    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=300)
    describtions = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=300)        
   
    def __str__(self):
        return self.title
 
 

# Create your models here.
