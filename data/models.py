from django.db import models
from django.core.validators import FileExtensionValidator

class Portfolio(models.Model):
    img = models.ImageField(upload_to = 'images/', blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
     
class TechStack(models.Model):
    img = models.ImageField(null=True, upload_to='images/', validators=[FileExtensionValidator(['jpg', 'png', 'svg'])])
    tech_title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tech_title