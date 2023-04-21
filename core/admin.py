from django.contrib import admin
from .models import Audio, Experimento, Evaluation

class EvaluationAdmin(admin.ModelAdmin):
    fields = ('audio', 'usuario', 'score', )

admin.site.register(Evaluation, EvaluationAdmin)

class ExperimentoAdmin(admin.ModelAdmin):
    fields = ('name', 'description', )

admin.site.register(Experimento, ExperimentoAdmin)


class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'archive', 'category')
    fields = ('archive', 'category')

admin.site.register(Audio, AudioAdmin)