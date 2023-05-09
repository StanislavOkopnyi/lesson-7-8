from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.all_students),
    path('teachers/', views.TeachersView.as_view())
]
