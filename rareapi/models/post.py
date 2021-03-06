from django.db import models
from rest_framework.authtoken.models import Token

class Post(models.Model):
    author= models.ForeignKey(Token, on_delete=models.CASCADE)
    category= models.ForeignKey("category", on_delete=models.CASCADE)
    title= models.CharField(max_length=15)
    content= models.CharField(max_length=250)
    publication_date= models.DateTimeField(auto_now=False, auto_now_add=False)
    image_url= models.CharField(max_length=50)
    approved= models.BooleanField()
    deleted= models.BooleanField()


    # Custom Property for tags and helping with M to M table.
    @property
    def tags(self):
            return self.__tags

    @tags.setter
    def tags(self, value):
            self.__tags = value    
    @property
    def subscribed(self):
            return self.__subscribed

    @subscribed.setter
    def subscribed(self, value):
            self.__subscribed = value    