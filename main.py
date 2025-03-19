import customtkinter as ctk
from models.spent import Spent
from models.category import Category
from table import TabelaApp

# Configuração inicial do customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Função para carregar os dados do arquivo
def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    # Separar as linhas e os valores por vírgula

    spents = []
    for linha in linhas:
        dados = linha.strip().split(',')

        value = float(dados[0])
        category = Category[dados[1].strip().upper()]
        date = dados[2].strip()

        spent = Spent(value=value, category=category, date=date)
        spents.append(spent)
    
    return spents

def write_data(spent):
    with open('banco.txt', 'a') as f:
        f.write(f"{spent.value}, {spent.category}, {spent.date}\n")
        return True
    return False

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Wallet")
        self.geometry("900x500")
        self.screen_table()
        self.screen_category()

    def screen_category(self):
        # Frame para a categoria, que ocupará 200px da largura na direita
        self.category_frame = ctk.CTkFrame(self, width=200)
        self.category_frame.pack(side="right", fill="y", padx=10, pady=30)

    def screen_table(self):
        # Frame para a tabela, ocupando o restante da largura
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(side="left", fill="both", expand=True, padx=10, pady=30)


        table_container = ctk.CTkFrame(self.table_frame)
        table_container.pack(fill="both", expand=True)

        # Leitura dos dados
        spents = carregar_dados('banco.txt')

        # Criar a tabela no frame
        table = TabelaApp(table_container, spents)

        self.btn_new_spent = ctk.CTkButton(self.table_frame, text = 'New Spent', command = self.screen_new_spent2)
        self.btn_new_spent.pack(side="bottom", pady=10)
    
    def screen_new_spent2(self):
        self.table_frame.forget()

        new_screen = ctk.CTkFrame(self)
        new_screen.pack(padx=280, pady=120)

        ctk.CTkLabel(new_screen, text="Value:").pack(pady=5)
        entry_value = ctk.CTkEntry(new_screen)
        entry_value.pack(pady=5, padx=100)

        ctk.CTkLabel(new_screen, text="Category:").pack(pady=5)
        entry_category = ctk.CTkEntry(new_screen)
        entry_category.pack(pady=5, padx=100)

        ctk.CTkLabel(new_screen, text="Date (dd/mm/yyyy):").pack(pady=5)
        entry_date = ctk.CTkEntry(new_screen)
        entry_date.pack(pady=5, padx=100)

        def save_data():
            spent = Spent(value=entry_value.get(), category=entry_category.get(), date=entry_date.get())

            if write_data(spent):
                new_screen.forget()
                self.screen_table()
            else:
                error_label = ctk.CTkLabel(new_screen, text="Erro ao salvar o arquivo!", text_color="red")
                error_label.pack(pady=10)
        
        ctk.CTkButton(new_screen, text="Save", command=save_data).pack(pady=20)

# Inicializando o aplicativo
if __name__ == "__main__":
    app = App()
    app.mainloop()