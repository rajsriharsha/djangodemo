from django.urls import path
from rest_framework import routers
#Harsha Comments
from . import views
from .viewsets import TodoViewSet

router = routers.SimpleRouter()
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("todo-listings/", views.TodoList.as_view(), name="TodoListView"),
    path("todo-update/", views.TodoStatusBulkUpdate.as_view(), name="TodoStatusUpdate"),
]
