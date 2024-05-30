from django.urls import path
from tasks.views import TaskListView, TaskListAPIView, TaskDetailView, TaskAddEditView, TaskLocationAPIView, TaskDeleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task_list_api'),
    path('api/location/<int:pk>/', TaskLocationAPIView.as_view(), name='task_location_api'),
    path('task/add/', TaskAddEditView.as_view(), name='task_add'),
    path('task/<int:pk>/edit/', TaskAddEditView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

]
