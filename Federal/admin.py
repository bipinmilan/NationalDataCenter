from django.contrib import admin

from Federal.models import Executive, Legislative, Judiciary

admin.site.site_header = 'National Data Center'


class ExecutiveAdmin(admin.ModelAdmin):
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


class LegislativeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'related_house', 'category', 'last_modified_by', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username', 'related_house__name')
    list_per_page = 25
    exclude = ['author', 'last_modified_by', 'timestamp']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name="Federal_Legislative").exists():
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class JudiciaryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'is_published', 'related_court', 'category', 'last_modified_by', 'modified_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'author__username', 'related_court__name')
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


admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(Judiciary, JudiciaryAdmin)
admin.site.register(Legislative, LegislativeAdmin)
