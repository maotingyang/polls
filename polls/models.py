import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField( max_length = 200 )
    # Field的第一個引數可以給一個給人看的名字
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField( max_length=200 )
    votes = models.IntegerField( default=0 )
    # 加入__str__method除了自己方便，admin也會用到
    def __str__(self):
        return self.choice_text