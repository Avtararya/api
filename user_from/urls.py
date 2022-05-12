from . import views
from django.urls import path


urlpatterns = [
    path('',views.bodypart),
    path('symptom',views.symptom)

]