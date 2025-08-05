# Task 2 - Python To-Do List Application
This is my submission for **Task 2** of the internship program – a *command-line To-Do List app* built using Python.

The app allows users to manage tasks interactively through a simple text-based menu.

---

## 🚀 Features

- ✅ Add tasks (with optional custom position)
- ❌ Remove tasks (by number or task name)
- 👀 View the current to-do list
- 💾 Save tasks to a file (tasks.txt)
- 🔁 Automatically loads previous tasks when restarted

---

## 💡 How It Works

Tasks are stored in a .txt file using Python's open() function.  
The file persists between runs, so your to-do list remains even after closing the program.
The app displays a menu which contains all it's basic functionalities, which the user could choose from.
The tasks specified by the user can be added to the list either at the end or at a particular position in the list.
User can also remove tasks either using the exact task name directly or by specifying the position of the task, which can be viewed from the list displayed already.
User can choose to view the list anytime, for which it will get displayed on the screen.
When the user chooses to Exit, the list gets saved and written in a .txt file which can be accessed later.
The use of ASCII art makes the CLI more beautiful.
The app provides an attractive, easy-to-use and efficient Command-Line Interface.
The app also handles various errors gracefully and hence preventing it from getting crashed due to any invalid input or file handling.

---

## 🛠 Tools Used

- Python
- PyCharm Community Edition
- File Handling (open())
- Command-Line Interface (CLI)

---
