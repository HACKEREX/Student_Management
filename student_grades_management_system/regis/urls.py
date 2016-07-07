from django.conf.urls import url
from django.contrib import admin
from models import studentdb,professorsdb

admin.site.register(studentdb)
admin.site.register(professorsdb)

urlpatterns=[
    url(r'stud/$','regis.views.studregis'),
    url(r'prof/$','regis.views.profregis'),
]
