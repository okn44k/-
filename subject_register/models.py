from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ls=[(0,'一般'),(1,'M'),(2,'E'),(3,'D'),(4,'J'),(5,'C')]

class Subject(models.Model):
    course = models.IntegerField(choices=ls)
    grade = models.IntegerField()
    select = models.BooleanField()
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    credit = models.IntegerField()
    url = models.URLField(blank=True)
    students = models.ManyToManyField(User,related_name='subjects',blank=True)
    def __str__(self):
        return self.title

class Form(models.Model):
    course = models.IntegerField(choices=ls)
    grade = models.IntegerField()
    def __str__(self):
        return ls[self.course][1] + str(self.grade)

class Option(models.Model):
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject,on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title

@receiver(post_save, sender=Option)
def make_option_title(sender, **kwargs):
    """ 新ユーザー作成時に空のprofileも作成する """
    if kwargs['created']:
        sender.title = sender.subject.title