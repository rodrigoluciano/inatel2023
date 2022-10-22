# coninfor2022

### Application.py 01 - criação da tela e importação de bibliotecas

    import tkinter as tk
    from tkinterdnd2 import TkinterDnD
    
    '''A extensão tkdnd fornece uma interface para mecanismos nativos de arrastar e soltar
    específicos da plataforma . '''


    class Application(TkinterDnD.Tk):


        def __init__(self):
            super().__init__()
    
            # create a title
            self.title("Leitor de CSV")
            self.main_frame = tk.Frame(self)
            self.main_frame.pack(fill="both", expand="true")
            self.geometry("900x800")
            
            # add this line in Application 02
            # self.search_page = SearchPage(parent=self.main_frame)


        # chamada da função que inicia o programa'''
    if __name__ == '__main__':
    root = Application()
    root.mainloop()

### Application 02 - Create Search Page
    
    class SearchPage(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.file_names_listbox = tk.Listbox(parent, selectmode=tk.SINGLE, background="#2f9599")
            self.file_names_listbox.place(relheight=1, relwidth=0.20)
            self.file_names_listbox.drop_target_register(DND_FILES)
            self.file_names_listbox.dnd_bind("<<Drop>>")
            self.file_names_listbox.bind("<Double-1>")
    
            self.search_entrybox = tk.Entry(parent)
            self.search_entrybox.place(relx=0.23, relwidth=0.75, y=650 )
            self.search_entrybox.bind("<Return>")

