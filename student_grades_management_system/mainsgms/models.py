from __future__ import unicode_literals

from django.db import models




CHOICES=(
    ("1","1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)



CHOICESBR=(
    (1,"CSE"),
    (2,"CIVIL"),
    (3,"MECHANICAL"),
    (4,"ECE"),
    (5,"ELECTRICAL"),
    (6,"META"),
    (7,"PRODUCTION")
)



class MarkSheet(models.Model):
    id=models.CharField(blank=False,max_length=50,primary_key=True)
    sem_no=models.CharField(choices=CHOICES,max_length=1,default=CHOICES[0])
    T1sub1 = models.CharField(max_length=2,blank=True)
    T1sub2 = models.CharField(max_length=2,blank=True)
    T1sub3 = models.CharField(max_length=2,blank=True)
    T1sub4 = models.CharField(max_length=2,blank=True)
    T1sub5 = models.CharField(max_length=2,blank=True)
    T1sub6 = models.CharField(max_length=2,blank=True)
    T2sub1 = models.CharField(max_length=2,blank=True)
    T2sub2 = models.CharField(max_length=2,blank=True)
    T2sub3 = models.CharField(max_length=2,blank=True)
    T2sub4 = models.CharField(max_length=2,blank=True)
    T2sub5 = models.CharField(max_length=2,blank=True)
    T2sub6 = models.CharField(max_length=2,blank=True)




    def __unicode__(self):
        return self.id


class Batch(models.Model):
    batch_no=models.CharField(max_length=4)
    cursem=models.SmallIntegerField()


class ProfWork(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    C1=models.CharField(max_length=6,blank=True)
    C2 = models.CharField(max_length=6,blank=True)
    C3 = models.CharField(max_length=6,blank=True)
    C4 = models.CharField(max_length=6,blank=True)
    C5 = models.CharField(max_length=6,blank=True)




