from django.contrib import admin

# Register your models here.
from provinces.models import ProvinceJudiciary, ProvinceExecutive


class ProvinceExecutiveAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'related_ministry', 'category', 'is_private',
        'last_modified_by', 'timestamp', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username', 'related_ministry__name')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']
    autocomplete_fields = ['related_ministry']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Executive").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class ProvinceJudiciaryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'court', 'category', 'last_modified_by', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Judiciary").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(ProvinceJudiciary, ProvinceJudiciaryAdmin)
admin.site.register(ProvinceExecutive, ProvinceExecutiveAdmin)
