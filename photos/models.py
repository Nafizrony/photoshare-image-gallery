from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=120,null=True,blank=True)
    slug = models.SlugField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse("gallery_category",args=[self.slug])    

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        if self.slug is None:
            self.slug = slugify(self.category_name)
            self.save() 

class Gallery(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    slug = models.SlugField(max_length=200,blank=True,null=True)
    images = models.ImageField(null=True,blank=True,upload_to='photos')
    description = models.TextField()

    def __str__(self):
        return self.description
    
    def get_url(self):
        return reverse("photo", args=[self.category.slug,self.id])
    
    

