from django.db import models
from django.contrib.auth.models import User
from student.models import Student
from quiz.models import Course,Result

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Teacher/',null=True,blank=True)
    email=models.EmailField(null=True)
    address = models.CharField(max_length=40)
    mobile = models.PositiveIntegerField(null=True)
    status= models.BooleanField(default=False)
    salary=models.PositiveIntegerField(null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name