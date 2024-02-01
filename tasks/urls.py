
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/create/', views.CreateTaskView.as_view(), name='task-create'),
    path('task/<pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<pk>/update/', views.UpdateTaskView.as_view(), name='task-update'),
    path('task/<pk>/delete/', views.DeleteTaskView.as_view(), name='task-delete'),
    path('delete_photo/<int:photo_id>/<int:task_id>/', views.delete_photo, name='delete-photo'),
]
