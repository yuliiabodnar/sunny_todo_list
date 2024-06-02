# tasks/tests/__init__.py

from .models.test_task_model import TaskModelTest
from .views.test_task_add_edit_view import TaskAddEditViewTest
from .views.test_task_delete_view import TaskDeleteViewTest
from .views.test_task_detail_view import TaskDetailViewTest
from .views.test_task_list_view import TaskListViewTest
from .middleware.test_check_task_completed_middleware import MiddlewareTest