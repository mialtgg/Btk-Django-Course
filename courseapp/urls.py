
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

    

urlpatterns =[
    path('',include('courses.urls')),
    path('admin/',admin.site.urls),
]