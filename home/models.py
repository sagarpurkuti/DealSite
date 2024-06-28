from django.db import models
from django.contrib.auth.models import User

# Make migrations: Create changes and store in a file
# Migrate: Apply the pending changes created by makemigrations

class Contact(models.Model):  
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=122, default='')
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):  # to get name of the person in the database Django
        return self.name
    
class Deal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Add user field
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.FileField(upload_to='deal_images/', blank=True, null=True)
    # image_url = models.URLField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=50)
    url = models.URLField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # Add user field
    image = models.ImageField(upload_to='banners/')
    url = models.URLField(max_length=200) 






