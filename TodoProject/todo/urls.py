from django.urls import path
from todo import views

urlpatterns = [
    path('add/', views.add),
    path('delete/<int:tid>', views.delete),
    path('update/<int:tid>', views.update)
]
