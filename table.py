from tkinter import ttk


# Classe responsável por criar a tabela
class TabelaApp:
    def __init__(self, frame, spents):
        self.frame = frame
        self.spents = spents
        self.criar_tabela()

    def criar_tabela(self):
        # Criando a Treeview
        columns = ("Value", "Category","Date")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=10)
        
        # Definindo os cabeçalhos
        for coluna in columns:
            self.tree.heading(coluna, text=coluna)
            self.tree.column(coluna, anchor="center", width=100)

        # Adicionando os dados à tabela
        for spent in self.spents:
            self.tree.insert("", "end", values=(spent.value, spent.category.name, spent.date))

        # Adicionando barra de rolagem
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Posicionando a tabela e a barra de rolagem
        self.tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

    def append(self, spent):
        self.tree.insert("", "end", values=(spent.value, spent.category, spent.date))