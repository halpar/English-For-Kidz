# Create your models here.
from django.db import models

class CardCategory(models.Model):
    name = models.CharField(max_length=3000, blank=False, null=False, unique=False, default='')
    photo = models.FileField(upload_to="cc", blank=True, null=True, unique=False)


class Card(models.Model):
    type = models.ForeignKey(CardCategory, related_name='cardcategory', on_delete=models.CASCADE)
    name_tr = models.CharField(max_length=3000, blank=False, null=False, unique=False, default='')
    name_eng = models.CharField(max_length=3000, blank=False, null=False, unique=False, default='')
    photo = models.FileField(upload_to="c", blank=True, null=True, unique=False)
    
    class Meta:
        ordering = ['name_tr']

    def __str__(self):
        return self.name_tr
    

class User(models.Model):
    username = models.CharField(max_length=3000, blank=False, null=False, unique=True, default='')
    cards = models.ManyToManyField(Card)
    
    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
   
   
   
    # #facebook = models.CharField(max_length=30000, blank=True, null=True, unique=False, default='')
    # instagram = models.CharField(max_length=30000, blank=True, null=True, unique=False, default='')
    # twitter = models.CharField(max_length=30000, blank=True, null=True, unique=False, default='')
    # linkedin = models.CharField(max_length=30000,blank=True, null=True, unique=False, default='')
    # hero_image = models.FileField(upload_to="photos", blank=True, null=True, unique=False)
    # tags = models.ManyToManyField(Tag, related_name='membear_tags') #SOR BU HATA VERİYO
    # website = models.CharField(max_length=30000, blank=True, null=True, unique=False, default='')