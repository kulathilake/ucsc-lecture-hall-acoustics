import sys
import tkinter as tk
class RedirectToConsole:
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        # if message != '\n':  # Avoid printing extra new lines
        self.widget.insert(tk.END, message)
        self.widget.yview(tk.END)  # Auto-scroll to the end

    def flush(self):
        pass  # No need to implement flush for this use case

class SimulationConsole:
    def __init__(self,root):
        console_frame = tk.Frame(root, bg='gray', height=50)
        console_frame.pack(side=tk.BOTTOM, fill=tk.X)
        text_output = tk.Text(console_frame, wrap=tk.WORD, bg='black', fg="white")
        text_output.pack(expand=True)
        sys.stdout = RedirectToConsole(text_output)