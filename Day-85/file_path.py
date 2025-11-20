from tkinter import filedialog
import os


def select_file_from_desktop():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    file_path = filedialog.askopenfilename(
        initialdir=desktop_path,
        title="Select a file from Desktop",
        filetypes=(("Image files", ("*.png", "*.jpg", "*.jpeg", "*.gif")), ("All files", "*.*"))
    )

    if file_path:
        return f"{file_path}"
        # with open(file_path, 'r') as f:
        #     content = f.read()
        #     print("File content:", content)
    else:
        return "No file selected."