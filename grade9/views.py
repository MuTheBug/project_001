from django.shortcuts import render
from grade9.models import *


# Create your views here.
def get_chapter(text):
    chapter = text.split(" ")[1]
    return int(chapter)


def main(request):
    chapters = ['1s', '2s', '1a', '2a']
    passage_with_choices = Text.objects.filter(type='choices', chapter__number__in=chapters).order_by('?').first()
    questions_for_the_first_passage = TextQuestion.objects.filter(text_id=passage_with_choices.id)[:5]
    tf_passage = Text.objects.filter(type="tof", chapter__number__in=chapters).order_by('?').first()
    questions_for_the_second_passage = TFQuestions.objects.filter(text_id=tf_passage.id).order_by('?')[:5]
    c = CTMistake.objects.filter().order_by('?')[:4]
    vocabularies = Multiples.objects.filter(type='vocabulary', chapter__number__in=chapters).order_by('?')[:4]
    grammars = Multiples.objects.filter().exclude(type="vocabulary", chapter__number__in=chapters).order_by('?')[:16]
    questions = MakeQuestions.objects.filter(chapter__number__in=chapters).order_by('?')[:4]
    correct = CorrectTheMistake.objects.filter(chapter__number__in=chapters).order_by('?').first()
    paragraph = Paragraphs.objects.filter(chapter__number__in=chapters).order_by('?').first()

    context = {'passage_with_choices': passage_with_choices,
               'c': c,
               'questions_for_the_first_passage': questions_for_the_first_passage,
               'tf_passage': tf_passage,
               'questions_for_the_second_passage': questions_for_the_second_passage,
               'vocabularies': vocabularies,
               'grammars': grammars,
               'questions': questions,
               'correct': correct,
               'para': paragraph
               }
    return render(request, "9thGrade/index2.html", context=context)
