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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tabela com Treeview")
        self.geometry("600x400")

        # Frame para a tabela
        self.tabela_frame = ctk.CTkFrame(self)
        self.tabela_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Leitura dos dados
        spents = carregar_dados('banco.txt')

        # Criar a tabela no frame
        TabelaApp(self.tabela_frame, spents)

# Inicializando o aplicativo
if __name__ == "__main__":
    app = App()
    app.mainloop()