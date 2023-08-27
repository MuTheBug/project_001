from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


class Chapter(models.Model):
    choices = (
        ('1a', "chapter one activity"),
        ('1s', "chapter one student"),
        ('2a', "chapter two activity"),
        ('2s', "chapter two student"),
        ('3a', "chapter three activity"),
        ('3s', "chapter three student"),
        ('4a', "chapter four activity"),
        ('4s', "chapter four student"),
        ('5a', "chapter five activity"),
        ('5s', "chapter five student"),
        ('6a', "chapter six activity"),
        ('6s', "chapter six student"),
        ('7a', "chapter seven activity"),
        ('7s', "chapter seven student"),
        ('8a', "chapter eight activity"),
        ('8s', "chapter eight student"),
        ('9a', "chapter nine activity"),
        ('9s', "chapter nine student"),
        ('10a', "chapter ten activity"),
        ('10s', "chapter ten student"),
        ('11a', "chapter eleven activity"),
        ('11s', "chapter eleven student"),
        ('12a', "chapter twelve activity"),
        ('12s', "chapter twelve student"),

    )

    number = models.CharField(max_length=3, choices=choices, unique=True)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = "0- Chapter"


class Text(models.Model):
    text = models.TextField()
    type = models.CharField(max_length=15, choices=[("choices", "Choices"), ("tof", "True Or False")])

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='texts')
    marker = models.TimeField(auto_now=True)

    def __str__(self):
        return f'{self.type} Text from {self.chapter} : {self.id}'

    class Meta:
        verbose_name = "1- Text"


class TextQuestion(models.Model):
    question = models.CharField(max_length=200)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=200)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "2- Choices for Text"


class Multiples(models.Model):
    question = models.CharField(max_length=200)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    type = models.CharField(max_length=30,
                            choices=[("grammar", "Grammar"), ("phonetics", "Phonetics"), ("vocabulary", "Vocabulary")])
    correct_answer = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "4- Multiple Options Question"


class TFQuestions(models.Model):
    question = models.CharField(max_length=200)
    answer = models.BooleanField()
    text = models.ForeignKey(Text, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "3- True Or False Question"


class Paragraphs(models.Model):
    paragraph = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.paragraph

    class Meta:
        verbose_name = "7- Paragraph"


class MakeQuestions(models.Model):
    question = models.CharField(max_length=200)
    underlined_word = models.CharField(max_length=30)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200, null=True, blank=True)

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "5- Forming Question"


class CorrectTheMistake(models.Model):
    text = models.TextField()
    error1 = models.CharField(max_length=30)
    correction1 = models.CharField(max_length=30)

    error2 = models.CharField(max_length=30)
    correction2 = models.CharField(max_length=30)

    error3 = models.CharField(max_length=30)
    correction3 = models.CharField(max_length=30)

    error4 = models.CharField(max_length=30)
    correction4 = models.CharField(max_length=30)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "6- Find the mistake"


class CTMistake(models.Model):
    text = models.CharField(max_length=250)
    error1 = models.CharField(max_length=90)
    error2 = models.CharField(max_length=90)
    error3 = models.CharField(max_length=90)
    error4 = models.CharField(max_length=90)

    correct_answer = models.CharField(max_length=90,)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "8- Choose the mistake"
