from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page not Found! <br><br> <button onclick="" href='';""> Go to Homepage <br><br>")

def home(request):
    return HttpResponse("Little Lemon!")