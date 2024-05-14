from django.db import models
from main.models import CustomUser
from datetime import date

class company(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True,default="images/user1.jpg")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField(max_length=10000,null=True)


    def __str__(self):
        return f"{self.user.name}"
    


class Interview(models.Model):
    company=models.ForeignKey(company,on_delete=models.CASCADE)
    description=models.TextField(max_length=1000,default=" ")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    application_end_date = models.DateField()
    schedulded=models.BooleanField(default=False)

    @property
    def is_greater(self):
      return date.today() >= self.start_date
    
    @property
    def is_greater_enddate(self):
      print(date.today(),"asdasd")
      return date.today() >= self.end_date
    



    def __str__(self):
        return f"{self.name}"

class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',blank=True, null=True,)
    question_text = models.CharField(max_length=1000)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        mark= "" if self.question_text[-1]=="?" else "?"
        return f"{self.question_text}{mark}"

class User_Answer(models.Model):
    question_inter = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1000,default="None")
    semantic_score=models.FloatField(default=0)

    def __str__(self):
        return f"{self.user_answer}"

class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Spoofing_detection = models.IntegerField(default=0)
    copy_pasting = models.IntegerField(default=0)
    tab_changing = models.IntegerField(default=0)
    user_answers = models.ManyToManyField(User_Answer, related_name='reports')
    interview=models.ForeignKey(Interview,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        user_answers = self.user_answers.all()
        return f" Interview  :{user_answers[0].question_inter.interview.name } User : {self.user.name}"
