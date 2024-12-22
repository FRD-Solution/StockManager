import tkinter as Tk




class GUI:

    parfaim = ["Ylang-Ylang", "Orange", "Citronnel", "Lavande"]
    command_infos:"list[str]" = ["Nom", "Prénom", "Téléphone"] + parfaim + ["livraison"]

    def __init__(self) -> None:
        self.root = Tk.Tk("YAAY stock management")
        self.root.title("YAAY stock management")
        self.createHMI()
        self.stock_menu()
        
    def start(self) -> None:
        Tk.mainloop()
    
    def stock_menu(self) -> None:
        self.switch_menu()
        with open("stock.xml", "r") as db:
            for rowPosition, line in enumerate(db.readlines()):
                for gridPosition, case in enumerate(line.split(";")):
                    b = Tk.Label(self.root, text=str(case)).grid(column=gridPosition, row=rowPosition + 3)
       
    def command_menu(self) -> None:
        self.switch_menu()
        self.Button_New_Command = Tk.Button(self.root, width=10, height=3, text="new", command=self.new_command).grid(row=1, column=0)

    def new_command(self) -> None:
        for columnPosition, element in enumerate(GUI.command_infos):
            b = Tk.Label(self.root, text=element).grid(row=3, column= columnPosition)

    def switch_menu(self) -> None:
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.createHMI()

    def createHMI(self) -> None:
        #buttons
        self.Button_Command_menu = Tk.Button(self.root, width=10, height=3, text="Command", command=self.command_menu).grid(row=0, column=0)
        self.Button_Command_menu = Tk.Button(self.root, width=10, height=3, text="Stock", command=self.stock_menu).grid(row=0, column=1)
        self.Button_exit = Tk.Button(self.root, width=10, height=3, text="Exit", command=self.exit).grid(row=0, column=1000)

    def exit(self):
        self.root.destroy()
        self.root.quit()

gui = GUI()
gui.start()