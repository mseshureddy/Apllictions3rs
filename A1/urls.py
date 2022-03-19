from A1.views import MSR
from django.urls import path
app_name='A1'
urlpatterns=[
    path('MSR/',MSR,name='MSR'),
]