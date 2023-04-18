from django.contrib import admin
from .models import Audio, Experimento

class AudioAdmin(admin.ModelAdmin):
    fields = ('arquivo', 'criterio')

admin.site.register(Audio, AudioAdmin)

class ExperimentoAdmin(admin.ModelAdmin):
    fields = ('nome', 'descricao', )

admin.site.register(Experimento, ExperimentoAdmin)