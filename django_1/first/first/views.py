from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse("Welcome to First")

def couese(request):
    return HttpResponse("Course")