from django.db import models

# Create your models here.
class Wisata(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.CharField(max_length=50)
    deskripsi = models.TextField()
    lokasi = models.TextField()
    gambar = models.URLField(max_length=200)
