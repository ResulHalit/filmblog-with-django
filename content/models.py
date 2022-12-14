from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Name(models.Model):
    yazi_sahibi = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.yazi_sahibi

class Content(models.Model):
    baslık = models.CharField(max_length =100, verbose_name="İçerik Başlığı")
    yazi = models.TextField(max_length = 10000, verbose_name="İçerik Yazısı")
    resim = models.FileField(upload_to='filmResmi/', null=True, blank=True, verbose_name="Film Resmi")
    imdb = models.URLField(max_length = 500, null=True, blank=True ,verbose_name="IMDb Linki")
    isim = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    tarih = models.DateField(null=True, auto_now_add=True, verbose_name="Yazı Tarihi")
    

    def __str__(self):
        return self.baslık