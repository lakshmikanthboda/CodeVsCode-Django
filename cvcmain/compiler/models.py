from datetime import datetime
from django.db import models
from django.utils import timezone
class register(models.Model):
    name= models.CharField(max_length=152)
    email=models.EmailField(max_length=201)
    mobile=models.IntegerField()
    password=models.CharField(max_length=51)
    answers=models.IntegerField()
    answered=models.CharField(max_length=10000)
    def __str__(self):

        return self.name

    class Meta:
        db_table=''
        managed=True
        verbose_name='register'
        verbose_name_plural='registers'

class questions(models.Model):
    question= models.TextField(max_length=1000)
    inputs=models.TextField(max_length=502)
    answer=models.TextField(max_length=501)
    no = models.TextField(max_length=500)
    def __str__(self):
        return str(self.no)

    class Meta:
        db_table=''
        managed=True
        verbose_name='questions'
        verbose_name_plural='questionss'


class post(models.Model):
    title= models.CharField(max_length=300)
    img=models.ImageField(upload_to ='images/')
    cat=models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    content=models.TextField()
    def __str__(self):
        return str(self.title)

    class Meta:
        db_table=''
        managed=True
        verbose_name='post'
        verbose_name_plural='posts'






# Create your models here.
class comment(models.Model):
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    comments = models.TextField()
    def __str__(self):
        return str(self.fname+' | '+self.lname+' | '+self.comments)

    class Meta:
        db_table=''
        managed=True
        verbose_name='comment'
        verbose_name_plural='comments'