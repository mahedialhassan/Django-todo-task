from django.urls import path
from task.views import home,addItem,allItem,DelateTask,editTask,completeTasks,CompleteTaskUpdate,DelateCompletedTask,complete_editTask
urlpatterns = [
    path('',home),
    path('add_item',addItem, name='addItem'),
    path('all_item/',allItem, name='allItem'),
    path('delete_task/<int:id>',DelateTask, name='delete_task'),
    path('edit_task/<int:id>',editTask, name='edit_task'),
    path('complete_tasks/',completeTasks, name='complete_tasks'),
    path('complete_task/<int:id>',CompleteTaskUpdate, name='complete_task'),
    path('delete_completed_task/<int:id>',DelateCompletedTask, name='delete_completed_task'),
    path('edit_completed_task/<int:id>',complete_editTask, name='edit_completed_task'),
   
    # path('complete_tasks_Delate',completeTaskDelate, name='complete_tasks_Delate'),
]
