from django.shortcuts import render
from grade9.models import *


# Create your views here.
def get_chapter(text):
    chapter = text.split(" ")[1]
    return int(chapter)


def main(request):

    passage_with_choices = Text.objects.filter(type='choices').order_by('?').first()
    questions_for_the_first_passage = TextQuestion.objects.filter(text_id=passage_with_choices.id)[:5]
    tf_passage = Text.objects.filter(type="tof").order_by('?').first()
    questions_for_the_second_passage = TFQuestions.objects.filter(text_id=tf_passage.id)
    vocabularies = Multiples.objects.filter(type='vocabulary').order_by('?')[:3]
    grammars = Multiples.objects.filter().exclude(type="vocabulary").order_by('?')[:17]
    questions = MakeQuestions.objects.filter()[:4]
    correct = CorrectTheMistake.objects.filter().order_by('?').first()
    paragraph = Paragraphs.objects.filter().order_by('?').first()

    context = {'passage_with_choices': passage_with_choices,
               'questions_for_the_first_passage': questions_for_the_first_passage,
               'tf_passage': tf_passage,
               'questions_for_the_second_passage': questions_for_the_second_passage,
               'vocabularies': vocabularies,
               'grammars': grammars,
               'questions': questions,
               'correct': correct,
               'para': paragraph,

               }
    return render(request, "9thGrade/index.html", context=context)
