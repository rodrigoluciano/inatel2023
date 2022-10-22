import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame
import pandas as pd
from tkdnd import DND_FILES
from tkinterdnd2 import TkinterDnD

'''A extensão tkdnd fornece uma interface para mecanismos nativos de arrastar e soltar
específicos da plataforma . '''


class Application(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Viewer")
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand="true")
        self.geometry("1000x690")
        self.search_page = SearchPage(parent=self.main_frame)


# class to prepare dataframe
class DataTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        scroll_y = tk.Scrollbar(self, orient="vertical", command=self.yview)
        scroll_x = tk.Scrollbar(self, orient="horizontal", command=self.xview)
        self.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        self.stored_dataframe = pd.DataFrame()


# structural page to recieve serch data
class SearchPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_names_listbox = tk.Listbox(parent, selectmode=tk.SINGLE, background="#2f9599")
        self.file_names_listbox.place(relheight=1, relwidth=0.20)
        self.file_names_listbox.drop_target_register(DND_FILES)
        self.file_names_listbox.dnd_bind("<<Drop>>")
        self.file_names_listbox.bind("<Double-1>")

        self.search_entrybox = tk.Entry(parent)
        self.search_entrybox.place(relx=0.23, relwidth=0.75, y=650)
        self.search_entrybox.bind("<Return>")

        # connect to application - Treeview
        self.data_table = DataTable(parent)
        self.data_table.place(rely=0.05, relx=0.23, relwidth=0.75, relheight=0.89)


'''chamada da função que inicia o programa'''
if __name__ == '__main__':
    root = Application()
    root.mainloop()
