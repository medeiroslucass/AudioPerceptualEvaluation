from django.contrib import admin
from .models import Audio, Experimento, Evaluation, Row

class EvaluationAdmin(admin.ModelAdmin):
    fields = ('audio', 'usuario', 'score', )

admin.site.register(Evaluation, EvaluationAdmin)

class ExperimentoAdmin(admin.ModelAdmin):
    fields = ('name', 'description', )

admin.site.register(Experimento, ExperimentoAdmin)



class AudioInline(admin.TabularInline):
    model = Audio
    extra = 0

class RowAdmin(admin.ModelAdmin):
    list_display = ('id', 'row')
    fields = ('row',)
    inlines = [AudioInline]

admin.site.register(Row, RowAdmin)


class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'archive', 'category', 'row')
    fields = ('archive', 'category', 'row')

admin.site.register(Audio, AudioAdmin)