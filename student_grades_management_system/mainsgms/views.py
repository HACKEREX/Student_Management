from django.shortcuts import render_to_response
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import  csrf_exempt



def main_page(request):
    return  render_to_response('index.html')


def gradecard(request):
    return render_to_response('marksheet.html')


def professors_site(request):
    return render_to_response('main_working.html')


@csrf_exempt
def studentlink(request,gotid):
    if request.method=="POST":

        studid=request.POST.get('id','')
        if gotid==studid:

            return JsonResponse({"id":"2014UGCS021","name":"Avinash Kumar"})
        else:
            return HttpResponse("Something Faulty")



    else:
        return HttpResponse("Request must be post");