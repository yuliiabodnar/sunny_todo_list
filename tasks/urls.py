from django.urls import path
from tasks.views import TaskListView, TaskListAPIView, TaskDetailView, TaskAddEditView, TaskLocationAPIView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task_list_api'),
    path('api/location/<int:pk>/', TaskLocationAPIView.as_view(), name='task_location_api'),
    path('tasks/add/', TaskAddEditView.as_view(), name='task_add'),
    path('tasks/edit/<int:pk>/', TaskAddEditView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

]
