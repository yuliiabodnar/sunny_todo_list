from django.urls import path
from tasks.views import TaskListView, TaskDetailView, TaskAddEditView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('tasks/add/', TaskAddEditView.as_view(), name='task_add'),
    path('task/edit/<int:pk>/', TaskAddEditView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
