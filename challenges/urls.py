from django.urls import path
from challenges import views

urlpatterns = [
    path("", views.index_main), #triggers /challenges
    path("<int:month>", views.challenge_index_number),
    path("<str:month>", views.challenge_index, name="month_challenge")
]

