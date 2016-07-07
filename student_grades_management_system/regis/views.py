from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from forms import StudentForm
from models import studentdb,professorsdb
from django.contrib.auth.models import User

@csrf_exempt
def studregis(request):

    if request.method=='POST':
        studform=StudentForm(request.POST)
        if studform.is_valid():
	    stid=request.POST.get('id')
	    stname=request.POST.get('name')
	    stprog=request.POST.get('Programme')
	    stdept=request.POST.get('dept')
        
	    NewStud=studentdb(id=stid,name=stname,Programme=stprog,dept=stdept)
	    
	    

	    NewStud.save()
            return HttpResponse('DONE')
    else:
        studform=StudentForm()
    return render_to_response('registration.html',{'regis_for' :'Student Registration Form','form_main':studform})

def profregis(request):
    return HttpResponse('done')
