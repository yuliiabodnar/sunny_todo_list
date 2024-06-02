from django.urls import path
from tasks.views import TaskListView, TaskLocationsContext, TaskDetailView, TaskAddEditView, TaskLocationContext, TaskDeleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/location-context/', TaskLocationsContext.as_view(), name='locations_context'),
    path('task/location-context/<int:pk>/', TaskLocationContext.as_view(), name='location_context'),
    path('task/add/', TaskAddEditView.as_view(), name='task_add'),
    path('task/<int:pk>/edit/', TaskAddEditView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),

]
