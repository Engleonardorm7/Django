from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    inlines=[ChoiceInline]#permite crear las respuestas
    list_display=("question_text","pub_date","was_published_recently")
    list_filter=["pub_date"] #agregar filtro por fecha
    search_fields=["question_test"]##agregar barra de busqueda
#se muestra primero la fecha y luego la pregunta
admin.site.register(Question, QuestionAdmin)
