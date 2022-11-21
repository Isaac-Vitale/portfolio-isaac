from django.db import models

from django.db import models
from ckeditor.fields import RichTextField


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)


    # Social Network
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete



class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
