from django.contrib import admin

# Register your models here.
from offices.models import ExecutiveOffice, LegislativeOffice, JudiciaryOffice


class ExecutiveOfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(ExecutiveOffice, ExecutiveOfficeAdmin)
admin.site.register(LegislativeOffice)
admin.site.register(JudiciaryOffice)
