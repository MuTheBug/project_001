from django.contrib import admin
from .models import Chapter, Text, TextQuestion,Multiples,TFQuestions,MakeQuestions,Paragraphs,CorrectTheMistake


admin.site.register(Chapter,)
admin.site.register(Text,)
admin.site.register(TextQuestion,)
admin.site.register(TFQuestions,)
admin.site.register(Multiples,)
admin.site.register(MakeQuestions,)
admin.site.register(Paragraphs,)
admin.site.register(CorrectTheMistake,)
