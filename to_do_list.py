import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40,bg='lightblue')
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task,bg='yellow')
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50,bg='black',fg='white')
        self.task_listbox.pack(pady=10)


        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task,bg='yellow')
        self.remove_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit,bg='yellow')
        self.quit_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
