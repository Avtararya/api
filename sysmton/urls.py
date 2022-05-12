from . import views
from django.urls import path


urlpatterns = [
    path('symptom',views.symptom)

]