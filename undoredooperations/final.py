import tkinter as tk

class UndoRedoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vyshu's Smart Notepad")
        self.root.geometry("500x400")

        # Stacks for Undo and Redo
        self.history = []
        self.redo_stack = []

        # 1. Label
        self.label = tk.Label(root, text="Type something and try Undo/Redo", font=("Arial", 12))
        self.label.pack(pady=10)

        # 2. Text Box
        self.text_area = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.text_area.pack(pady=10)
        
        # Save state when user types
        self.text_area.bind("<KeyRelease>", self.save_state)

        # 3. Buttons Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.undo_btn = tk.Button(button_frame, text="Undo", command=self.undo, width=10, bg="#ffcccc")
        self.undo_btn.grid(row=0, column=0, padx=10)

        self.redo_btn = tk.Button(button_frame, text="Redo", command=self.redo, width=10, bg="#ccffcc")
        self.redo_btn.grid(row=0, column=1, padx=10)

        # 4. Keyboard Shortcuts
        self.root.bind("<Control-z>", lambda event: self.undo())
        self.root.bind("<Control-y>", lambda event: self.redo())

        # Initialize history
        self.history.append("")

    def save_state(self, event=None):
        # Keyboard press ayinappudu current text ni save chestundi
        current_text = self.text_area.get("1.0", tk.END).strip()
        if not self.history or current_text != self.history[-1]:
            self.history.append(current_text)
            self.redo_stack.clear() # Kotha text vaste redo clear avvali

    def undo(self):
        if len(self.history) > 1:
            # Current state ni redo ki pampinchi, pathadi teeskodam
            self.redo_stack.append(self.history.pop())
            previous_text = self.history[-1]
            
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", previous_text)
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_stack:
            next_text = self.redo_stack.pop()
            self.history.append(next_text)
            
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", next_text)
        else:
            print("Nothing to redo")

# App Run Cheyadam
if __name__ == "__main__":
    root = tk.Tk()
    app = UndoRedoApp(root)
    root.mainloop()