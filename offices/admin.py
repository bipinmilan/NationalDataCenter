from django.contrib import admin

# Register your models here.
from offices.models import ExecutiveOffice, LegislativeOffice, JudiciaryOffice, ProvinceJudiciaryOffice


class ExecutiveOfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(ExecutiveOffice, ExecutiveOfficeAdmin)
admin.site.register(LegislativeOffice)
admin.site.register(JudiciaryOffice)

# for provincial government offices
admin.site.register(ProvinceJudiciaryOffice)
