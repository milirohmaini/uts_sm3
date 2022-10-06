from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import MahasiswaFkip, DosenFkip, StaffFkip


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def fkip(request):
    template = loader.get_template('fkip.html')
    mahasiswa = MahasiswaFkip.objects.all()
    dosen = DosenFkip.objects.all()
    staff = StaffFkip.objects.all()
    context = {
        'dataMahasiswa': mahasiswa,
        'dataDosen': dosen,
        'dataStaff': staff,
    }
    return HttpResponse(template.render(context))
def feb(request):
    template = loader.get_template('feb.html')
    return HttpResponse(template.render())
def fh(request):
    template = loader.get_template('fh.html')
    return HttpResponse(template.render())
def fisip(request):
    template = loader.get_template('fisip.html')
    return HttpResponse(template.render())
def fk(request):
    template = loader.get_template('fk.html')
    return HttpResponse(template.render())
def ft(request):
    template = loader.get_template('ft.html')
    return HttpResponse(template.render())
def pascasarjana(request):
    template = loader.get_template('pascasarjana.html')
    return HttpResponse(template.render())
def faperta(request):
    template = loader.get_template('faperta.html')
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

