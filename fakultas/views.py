from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import DosenFaperta,  StaffFaperta, MahasiswaFaperta
from . models import  DosenFeb, StaffFeb, MahasiswaFeb
from . models import  DosenFh, StaffFh, MahasiswaFh
from . models import  DosenFisip, StaffFisip, MahasiswaFisip
from . models import  DosenFk, StaffFk, MahasiswaFk    
from . models import  ProdiFkip, DosenFkip, StaffFkip, MahasiswaFkip, AkreditasiFkip, HmjFkip, RuanganFkip, UkmFkip, DutaFkip, MatakuliahFkip
from . models import  DosenFt, StaffFt, MahasiswaFt
from . models import  DosenPascasarjana, StaffPascasarjana, MahasiswaPascasarjana   



# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def faperta(request):
    template = loader.get_template('faperta.html')
    dosen = DosenFaperta.objects.all()
    staff = StaffFaperta.objects.all()
    mahasiswa = MahasiswaFaperta.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def feb(request):
    template = loader.get_template('feb.html')
    dosen = DosenFeb.objects.all()
    staff = StaffFeb.objects.all()
    mahasiswa = MahasiswaFeb.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fh(request):
    template = loader.get_template('fh.html')
    dosen = DosenFh.objects.all()
    staff = StaffFh.objects.all()
    mahasiswa = MahasiswaFh.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fisip(request):
    template = loader.get_template('fisip.html')
    dosen = DosenFisip.objects.all()
    staff = StaffFisip.objects.all()
    mahasiswa = MahasiswaFisip.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fk(request):
    template = loader.get_template('fk.html')
    dosen = DosenFk.objects.all()
    staff = StaffFk.objects.all()
    mahasiswa = MahasiswaFk.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fkip(request):
    template = loader.get_template('fkip.html')
    prodi = ProdiFkip.objects.all()
    dosen = DosenFkip.objects.all()
    staff = StaffFkip.objects.all()
    mahasiswa = MahasiswaFkip.objects.all()
    akreditasi = AkreditasiFkip.objects.all()
    hmj = HmjFkip.objects.all()
    ruangan = RuanganFkip.objects.all()
    ukm = UkmFkip.objects.all()
    duta = DutaFkip.objects.all()
    matakuliah = MatakuliahFkip.objects.all()
    context = {
        'dataProdi': prodi,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
        'akreditasi': akreditasi,
        'dataHmj': hmj,
        'dataRuangan': ruangan,
        'dataUkm': ukm,
        'dataDuta': duta,
        'dataMatakuliah': matakuliah,
         
    }
    return HttpResponse(template.render(context))

def ft(request):
    template = loader.get_template('ft.html')
    dosen = DosenFt.objects.all()
    staff = StaffFt.objects.all()
    mahasiswa = MahasiswaFt.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
         
    }
    return HttpResponse(template.render())

def pascasarjana(request):
    template = loader.get_template('pascasarjana.html')
    dosen = DosenPascasarjana.objects.all()
    staff = StaffPascasarjana.objects.all()
    mahasiswa = MahasiswaPascasarjana.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
         
    }
    return HttpResponse(template.render())

def selayangpandang(request):
    template = loader.get_template('selayangpandang.html')
    return HttpResponse(template.render())
def visidanmisi(request):
    template = loader.get_template('visidanmisi.html')
    return HttpResponse(template.render())
def strukturorganisasi(request):
    template = loader.get_template('strukturorganisasi.html')
    return HttpResponse(template.render())
def maknalambang(request):
    template = loader.get_template('maknalambang.html')
    return HttpResponse(template.render())

