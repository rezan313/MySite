from django.db import models

class Qustion(models.Model):
    qustion_text=models.CharField(max_length=200)
    pup_date=models.DateTimeField('date published')
    def __str__(self):
        return self.qustion_text

class Choice(models.Model):
    qustion=models.ForeignKey(Qustion,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=300)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.