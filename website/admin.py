from django.contrib import admin
from .models import Board, FAQ, Chair, CoChair, Committee

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'club')
    search_fields = ('name', 'role')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    search_fields = ('question',)

class ChairAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name',)

class CoChairAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name',)

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chair_1_name', 'chair_2_name', 'topic')
    search_fields = ('name',)

    def chair_1_name(self, obj):
        return obj.chair_1_id.name

    def chair_2_name(self, obj):
        return obj.chair_2_id.name
    
    def cochair_name(self, obj):
        return obj.cochair_id.name
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'chair':
            kwargs['queryset'] = Chair.objects.all()  # Replace YourChairModel with the actual Chair model
            kwargs['name'] = 'name'  # Replace 'name' with the actual field representing the chair name
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Board, BoardAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Chair, CoChairAdmin)
admin.site.register(CoChair, ChairAdmin)
admin.site.register(Committee, CommitteeAdmin)