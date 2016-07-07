from __future__ import unicode_literals

from django.db import models


CHOICEPROG=(
    (1,'B.Tech'),
    (2,'M.Tech'),
)

CHOICEDEPT=(
    (1,'CSE'),
    (2,'CIVIL'),
    (3,'MECHANICAL'),
    (4,'ELECTRICAL'),
    (5,'META'),
    (6,'ECE'),
    (7,'PRODUCTION'),
)

CHOICEDEPTT=(
    (1,'CSE'),
    (2,'ECE'),
    (3,'SOFTSKILLS'),
    (4,'MATHEMATICS'),
    (5,'CHEMISTRY'),
    (6,'CIVIL'),
    (7,'ELECTRICAL'),
    (8,'PRODUCTION'),
    (9,'META'),
    (10,'MECHANICAL'),
)

class studentdb(models.Model):
    id=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=300)
    Programme=models.CharField(choices=CHOICEPROG,default="B.Tech",max_length=20)
    dept=models.CharField(choices=CHOICEDEPT,default="CSE",max_length=20)

    def __unicode__(self):
	return self.id



class professorsdb(models.Model):
    id=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    dept=models.CharField(choices=CHOICEDEPTT,default=CHOICEDEPTT[1],max_length=20)

    def __unicode__(self):
	return self.id

