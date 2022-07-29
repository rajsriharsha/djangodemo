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

class Type(models.Model):

    type_id = models.AutoField(
        primary_key = True,verbose_name = 'Type ID'
    )
    type_name = models.CharField(
        max_length=100, verbose_name='Type Name'
    )
    type_desc = models.TextField(
        null=True, blank=True
    )
    active_status = models.BooleanField(
        default=True, verbose_name='Active ? '
    )
    remarks = models.TextField(
        default='',verbose_name='Remarks'
    )

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Type'
        ordering = ['type_name',]
        unique_together = ['type_name','active_status']
        db_table = 'authorisations_type'

    def __str__(self):
        return self.type_name + str(self.type_id)


class Status(models.Model):
    status_id = models.AutoField(
        primary_key=True,
    )
    status_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.status_name


class Region(models.Model):
    region_id = models.AutoField(
        primary_key=True,
    )
    region_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.region_name