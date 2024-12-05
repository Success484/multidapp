from django.db import models

# Create your models here.

class Multiapps(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
    

class PhraseKey(models.Model):
    name = models.ForeignKey(Multiapps, on_delete=models.CASCADE, default=None)
    phrase_key = models.TextField(max_length=250, default=None)

    def __str__(self):
        return str(self.name)