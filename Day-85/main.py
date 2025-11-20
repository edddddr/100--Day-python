from tkinter import  *
from tkinter import ttk, filedialog
import tkinter as tk
import os
from img_pil import make_watermark
from file_path import select_file_from_desktop

class Application(tk.Frame):
    def __init__(self, master=None):
        root = tk.Frame.__init__(self, master)
        self.mainframe = ttk.Frame(root, padding=(10, 10, 22, 22))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.createWidgets()



        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



    def createWidgets(self):
        self.watermark = StringVar()
        self.watermark_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.watermark)
        self.watermark_entry.grid(column=3, row=1)
        self.watermark_entry.focus()

        self.img_path = StringVar()
        self.image_path_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.img_path)
        self.image_path_entry.grid(column=3, row=2)

        ttk.Label(self.mainframe, text="Enter a text to be Watermarked").grid(column=2, row=1)
        ttk.Label(self.mainframe, text="Enter the file path or hit the button").grid(column=2, row=2)

        self.getButton = ttk.Button(self.mainframe, text='Get the path', command=self.get_file_path)
        self.getButton.grid(column=3, row=3, sticky=(W, E))

        self.addWatermark_button = ttk.Button(self.mainframe, text='Add Watermark', command=self.addWatermarkText)
        self.addWatermark_button.grid(column=2, row=3, sticky=(W, E))


        # self.show = StringVar()
        # ttk.Label(self.mainframe, textvariable=self.show).grid(column=2, row=2, sticky=(W, E))


    def get_file_path(self):
        file_path = select_file_from_desktop()
        self.img_path.set(file_path)
        return file_path


    def  addWatermarkText(self):
         watermark_text = self.watermark.get()
         url_path = self.img_path.get()

         split_path = url_path.split("/")
         split_path.pop()
         directory = "/".join(split_path)


         make_watermark(watermark_text, url_path, directory)







app = Application()
app.master.title('WaterMarker')
# app.bind("<Return>", app.return_img_path)
app.mainloop()