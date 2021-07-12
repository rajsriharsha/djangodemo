from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=127)
    status = models.PositiveIntegerField(
        choices=(
            (
                0,
                "pending",
            ),
            (
                1,
                "completed",
            ),
        )
    )
    todo_child = models.ForeignKey(
        "Todo_Child", on_delete=models.CASCADE, related_name="todo_child_todo"
    )


class Todo_Child(models.Model):
    sub_task = models.CharField(max_length=100)
    active_flag = models.BooleanField()
