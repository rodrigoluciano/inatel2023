# import libs
import tkinter as tk
from tkinter import ttk
from pathlib import Path

from tkinterdnd2 import DND_FILES, TkinterDnD

'''A extensão tkdnd fornece uma interface para mecanismos nativos de arrastar e soltar
específicos da plataforma . '''

import pandas as pd


class Application(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        # create a title
        self.title("Leitor de CSV")
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand="true")
        self.geometry("900x800")


if __name__ == '__main__':
    root = Application()
    root.mainloop()