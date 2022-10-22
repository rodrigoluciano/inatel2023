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


        # chamada da função que inicia o programa'''
    if __name__ == '__main__':
    root = Application()
    root.mainloop()

