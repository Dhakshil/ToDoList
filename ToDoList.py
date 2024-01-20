import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = {}

        self.layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.task_list = QListWidget()

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)

        self.add_button.clicked.connect(self.add_task)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks[task] = False
            self.task_list.addItem(task)
            self.input_field.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            del self.tasks[item.text()]
            self.task_list.takeItem(self.task_list.row(item))

    def mark_task_complete(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            self.tasks[item.text()] = True
            item.setCheckState(2)

    def keyPressEvent(self, event):
        if event.key() == 16777248:
            self.delete_task()
        elif event.key() == 16777249:
            self.mark_task_complete()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
