from django.contrib import admin
from . models import DosenFaperta, StaffFaperta, MahasiswaFaperta 
from . models import DosenFeb, StaffFeb, MahasiswaFeb
from . models import DosenFh, StaffFh, MahasiswaFh
from . models import DosenFisip, StaffFisip, MahasiswaFisip
from . models import DosenFk, StaffFk, MahasiswaFk
from . models import ProdiFkip, DosenFkip, StaffFkip, MahasiswaFkip, AkreditasiFkip, HmjFkip, RuanganFkip, UkmFkip, DutaFkip, MatakuliahFkip
from . models import DosenFt, StaffFt, MahasiswaFt
from . models import DosenPascasarjana, StaffPascasarjana, MahasiswaPascasarjana  




# Register your models here.
admin.site.register(DosenFaperta)
admin.site.register(StaffFaperta)
admin.site.register(MahasiswaFaperta)

admin.site.register(DosenFeb)
admin.site.register(StaffFeb)
admin.site.register(MahasiswaFeb)

admin.site.register(DosenFh)
admin.site.register(StaffFh)
admin.site.register(MahasiswaFh)

admin.site.register(DosenFisip)
admin.site.register(StaffFisip)
admin.site.register(MahasiswaFisip)

admin.site.register(DosenFk)
admin.site.register(StaffFk)
admin.site.register(MahasiswaFk)

admin.site.register(DosenFkip)
admin.site.register(StaffFkip)
admin.site.register(MahasiswaFkip)
admin.site.register(ProdiFkip)
admin.site.register(HmjFkip)
admin.site.register(RuanganFkip)
admin.site.register(UkmFkip)
admin.site.register(DutaFkip)
admin.site.register(MatakuliahFkip)
admin.site.register(AkreditasiFkip)

admin.site.register(DosenFt)
admin.site.register(StaffFt)
admin.site.register(MahasiswaFt)

admin.site.register(DosenPascasarjana)
admin.site.register(StaffPascasarjana)
admin.site.register(MahasiswaPascasarjana)


