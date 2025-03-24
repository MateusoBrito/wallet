import customtkinter as ctk
from models.spent import Spent
from models.category import Category
from database.dao import Dao
from table import TabelaApp

# Configuração inicial do customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Wallet")
        self.geometry("900x500")
        self.minsize(width=900, height=500)

        self.frame_table()
        self.frame_right()

    def frame_right(self):
        # Frame para a categoria, que ocupará 200px da largura na direita
        self.frame_right = ctk.CTkFrame(self)
        self.frame_right.pack(side="right", fill="y", padx=10, pady=10)
        self.frame_right.configure(width=200) 
        self.frame_right.pack_propagate(False) 

        spents = Dao.carregar_dados()

        top_frame = ctk.CTkFrame(self.frame_right, height=50)
        top_frame.pack(side="top", fill="x", padx=10, pady=10)
        total = 0
        for spent in spents:
            total += spent.value
        text = f"total: {total:.2f}"
        ctk.CTkLabel(top_frame, text=text).pack(anchor="w", padx=10, pady=10)

        frame_category = ctk.CTkFrame(self.frame_right)
        frame_category.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        category_totals = {category.value: 0 for category in Category}
        for spent in spents:
            category_totals[spent.category.value] += spent.value

        for category, total in category_totals.items():
            text = f"{category}: {total:.2f}"
            ctk.CTkLabel(frame_category, text=text).pack(anchor="w", padx=10, pady=10)


    def frame_table(self):
        # Frame para a tabela, ocupando o restante da largura
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)


        table_container = ctk.CTkFrame(self.table_frame)
        table_container.pack(fill="both", expand=True, padx=10, pady=10)

        # Leitura dos dados
        spents = Dao.carregar_dados()

        # Criar a tabela no frame
        self.table = TabelaApp(table_container, spents)

        self.btn_new_spent = ctk.CTkButton(self.table_frame, text = 'New Spent', command = self.screen_new_spent)
        self.btn_new_spent.pack(side="bottom", pady=10)
    
    def screen_new_spent(self):
        screen = ctk.CTkToplevel(self)
        screen.title("New Spent")
        screen.geometry("300x280")

        ctk.CTkLabel(screen, text="Value:").pack()
        entry_value = ctk.CTkEntry(screen, placeholder_text="00000")
        entry_value.pack()

        ctk.CTkLabel(screen, text="Category:").pack()
        categories = [category.value for category in Category]
        entry_category = ctk.CTkOptionMenu(screen, values= categories,height= 32 ,fg_color= "#343638", button_color="#343638")
        entry_category.pack()
        entry_category.set("Choice")

        ctk.CTkLabel(screen, text="Date:").pack()
        entry_date = ctk.CTkEntry(screen, placeholder_text="dd/mm/yyyy")
        entry_date.pack()
        

        def save_data():
            category = Category[entry_category.get().upper()]
            spent = Spent(value=float(entry_value.get()), category=category.name, date=entry_date.get())

            if Dao.write_data(spent):
                self.table.append(spent)
                screen.destroy()
            else:
                error_label = ctk.CTkLabel(screen, text="Erro ao salvar o arquivo!", text_color="red")
                error_label.pack(pady=10)
        
        ctk.CTkButton(screen, text="Save", command=save_data).pack(pady=20)

# Inicializando o aplicativo
if __name__ == "__main__":
    app = App()
    app.mainloop()