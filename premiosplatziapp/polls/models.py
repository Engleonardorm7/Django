import datetime

from django.db import models
from django.utils import timezone
class Question(models.Model):
    #id - usando django no se necesita un id (Clave primaria) ya que el programa lo hace automaticamente asignando un valor incremental
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1) #se resta un dia para ver si es reciente

class Choice(models.Model):
    #id
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text