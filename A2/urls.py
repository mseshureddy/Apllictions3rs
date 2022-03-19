from A2.views import VSR
from django.urls import path
app_name='A2'
urlpatterns=[
    path('VSR/',VSR,name='VSR')
]
