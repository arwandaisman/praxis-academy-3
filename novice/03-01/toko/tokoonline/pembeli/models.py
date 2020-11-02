from django.conf import settings
from django.db import models

class Online(models.Model):
    nomor_id = models.CharField(max_length =5, null=True,blank=False)
    nama_barang = models.CharField(max_length=240, null=True,blank=False)
    ukuran_barang = models.CharField(max_length=6, null=True,blank=False)
    nama_pemesan = models.CharField(max_length=100, null=True,blank=False)
    alamat_pemesan = models.CharField(max_length=100, null=True,blank=False)
    jumlah_pemesanan = models.IntegerField(null=True,blank=False)

    # def __str__(self):
    #     return self.nomor_id