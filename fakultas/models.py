from django.db import models

# Create your models here.

class DosenFaperta(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFaperta(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFaperta(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class DosenFeb(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFeb(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFeb(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)


class DosenFh(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFh(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFh(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class DosenFisip(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFisip(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFisip(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class DosenFk(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFk(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFk(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class ProdiFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    namajurusan = models.CharField(max_length=100, null=True)
    tahunberdiri = models.CharField(max_length=50)
    namakajur = models.CharField(max_length=50)

    def _str_(self):
        return "{}".format(self.nama)
    

class DosenFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)



class DosenFt(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffFt(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaFt(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class DosenPascasarjana(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class StaffPascasarjana(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)

class MahasiswaPascasarjana(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def _str_(self):
        return "{}".format(self.nama)



