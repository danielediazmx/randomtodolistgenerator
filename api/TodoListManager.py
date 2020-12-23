from todoist.api import TodoistAPI

from seleniumtest.TodoListElement import TodoListElement


class TodoListManager:
    def __init__(self):  # initialize todolist class
        self.api = TodoistAPI('dfec637dfd89ea39e173493d96702d809ba102e7')
        self.project_id = '2253212422'

    def add_task(self, todo_list_element: TodoListElement):  # adds a task through todolist api
        section_id = '30277953'

        task = self.api.items.add(todo_list_element.name, project_id=self.project_id)  # create task
        task.move(section_id=section_id)  # move task to 'TODO' section

        self.api.commit()
