from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

#class User(User):
#    pass

class User(AbstractUser):
    nationality = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, choices=(('M', 'MALE'),('F', 'FEMALE'),('O', 'OTHER'),))
    institute = models.CharField(max_length=255)
    avatar = models.URLField(verbose_name="Display Picture",blank=True)
    def delete_user(self):
        return reverse("staff:delete-user")


class Roadmap(models.Model):
    creator=models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    r_name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    number_of_forks=models.IntegerField()
    number_of_courses=models.IntegerField()
    details = models.CharField(max_length=2000)
    stars = models.IntegerField()
    
class Achievement(models.Model):
    user = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    link = models.URLField()

class Course(models.Model):
    roadmap = models.ForeignKey(Roadmap,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_link = models.URLField()
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    course_description = models.CharField(max_length=255)

class Fork(models.Model):
    forker = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    roadmap_id = models.ForeignKey(Roadmap,on_delete=models.CASCADE)
    progress = models.IntegerField()
    date=models.DateTimeField(auto_now_add=True, null=True, blank=True)

# Create your models here.


