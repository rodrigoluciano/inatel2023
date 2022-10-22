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
            # self.file_names_listbox.dnd_bind("<<Drop>>",self.drop_inside_list_box)
            self.file_names_listbox.bind("<Double-1>")
            # self.file_names_listbox.bind("<Double-1>",self._display_file)
    
            self.search_entrybox = tk.Entry(parent)
            self.search_entrybox.place(relx=0.23, relwidth=0.75, y=650 )
            self.search_entrybox.bind("<Return>")

### Application 03 - Create DataTable ro recive data

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

### Application 04 - Custom widget Methods
    # class DataTable(ttk.Treeview):
    #   self.stored_dataframe = pd.DataFrame()
    # continue here ...

    def set_data_table(self,dataframe):
        self.stored_dataframe = dataframe
        self._draw_table(dataframe)

    def _draw_table(self,dataframe):
        self.delete(*self.get_children())
        columns = list(dataframe.columns)
        self.__setitem__("column", columns)
        self.__setitem__("show","headings")

        for col in columns:
            self.heading(col,text=col)

        df_rows = dataframe.to_numpy().tolist()
        for row in df_rows:
            self.insert("","end", values=row)
        return None

    def find_value(self,pairs):
        # pairs is a dictinary
        new_df = self.stored_dataframe
        for col,value in pairs.items():
            query_string = f"{col}.str.contains('{value}')"
            new_df = new_df.query(query_string, engine="python")

        self._draw_table(new_df)

    def reset_table(self):
        self._draw_table(self.stored_dataframe)

### Application 05 - Biding Methods
    
    # class SearchPage(tk.Frame):
    # connect to application - Treeview
    # self.data_table = DataTable(parent)
    # self.data_table.place(rely=0.05, relx=0.23, relwidth=0.75, relheight=0.89)
    #continue ...
    
    def drop_inside_list_box(self,event):
        pass

    # double click in display file show data in TreeView
    def _display_file(self,event):
        pass

    def _parse_drop_file(self, filename):
        pass

    def search_table(self):
        pass

### Application 06 Drap and drop files

        def _parse_drop_file(self, filename):
        # '/home/rodrigo/Documentos/PythonProjects/CONINFOR2022/Datasets/PS4_GamesSales.csv /home/rodrigo/Documentos/PythonProjects/CONINFOR2022/Datasets/XboxOne_GameSales.csv'
        size = len(filename)
        res = []  # list of filepath
        name = ""
        indx = 0

        while indx < size:
            if filename[indx] == "{":
                j = indx + 1
                while filename[j] != "}":
                    name += filename[j]
                    j += 1
                res.append(name)
                name == ""
                indx = j

            elif filename[indx] ==" " and name != "":
                res.append(name)
                name = ""
            elif filename[indx] != " ":
                name += filename[indx]
            indx += 1
        if name != "":
            res.append(name)
        return res

        
        def drop_inside_list_box(self, event):
            file_paths = self._parse_drop_file(event.data)
            current_list_box_items = set(self.file_names_listbox.get(0, "end"))
            for file_path in file_paths:
                if file_path.endswith(".csv"):
                    path_object = Path(file_path)
                    file_name = path_object.name
                    if file_name not in current_list_box_items:
                        self.file_names_listbox.insert("end", file_name)
                        self.path_map[file_name] = file_path

### Application 07 Display DataFrame in widget

    