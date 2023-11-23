
from django.urls import path

from todoapp import views

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('views/',views.TaskListView.as_view(),name='views'),
    path('detailnew/<int:pk>/', views.TaskDetailView.as_view(), name='detailnew'),
    path('updatenew/<int:pk>/', views.TaskUpdateView.as_view(), name='updatenew'),
    path('deletenew/<int:pk>/', views.TaskDeleteView.as_view(), name='deletenew'),
]
