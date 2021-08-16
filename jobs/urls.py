from django.urls import path,include
from jobs import views
urlpatterns = [
    path('<str:slug>', views.jobpage, name='jobpage' ),
]