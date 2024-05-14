from django.db import models
from main.models import CustomUser
from company.models import Interview
from datetime import date

class candidate(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True,default="images/user1.jpg")
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField(max_length=10000,null=True)


    def __str__(self):
        return f"{self.user.name}"

class Skill(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Eduaction(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    data=models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.data}"

class CVSubmission(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECT="Reject"

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECT,"Reject")
    ]

    applied_candidate=models.ForeignKey(candidate, on_delete=models.CASCADE)
    interview=models.ForeignKey(Interview,on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv_uploads/')
    show=models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.applied_candidate} , {self.interview}"
    
    @property
    def is_greater(self):
      print(date.today(),"asdasd")
      return date.today() >= self.start_date

class ApprovedCandidate(models.Model):
    app_candidate=models.ForeignKey(candidate,on_delete=models.CASCADE)
    interview=models.ForeignKey(Interview,on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.app_candidate} , {self.interview}"
