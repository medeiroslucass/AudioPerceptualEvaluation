from django.contrib import admin
from .models import Audio, Experimento, Evaluation, Row, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name_category', )
    list_display = ('id' ,'name_category', )
    search_fields = ('name_category', )
    ordering = ('name_category', )
    list_filter = ('name_category', )

admin.site.register(Category, CategoryAdmin)


class EvaluationAdmin(admin.ModelAdmin):
    fields = ('audio', 'usuario', 'score', )

admin.site.register(Evaluation, EvaluationAdmin)


class AudioInline(admin.TabularInline):
    model = Audio
    extra = 1


class ExperimentoAdmin(admin.ModelAdmin):
    fields = ('name', 'description', )
    inlines = [AudioInline]


admin.site.register(Experimento, ExperimentoAdmin)


class RowAdmin(admin.ModelAdmin):
    list_display = ('id', 'row')
    fields = ('row',)
    inlines = [AudioInline]


admin.site.register(Row, RowAdmin)


# class AudioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'archive', 'form', 'row')
#     fields = ('archive', 'form', 'row')
#
#
# admin.site.register(Audio, AudioAdmin)