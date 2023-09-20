from  django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse ('anasayfa')
def kurslar(request):
    return HttpResponse('kurs listesi')

urlpatterns = [
    path('',home),
    path('anasayfa', home),
    path('kurs listesi', kurslar),
    

]