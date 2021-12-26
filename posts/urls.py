from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "post"),
    path('<int:post_id>/', views.get_details, name = 'details')
]