from models.category import Category
from models.spent import Spent

DATA = 'database/data.txt'

class Dao:
    def carregar_dados():
        with open(DATA, 'r') as f:
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
        with open(DATA, 'a') as f:
            f.write(f"{spent.value}, {spent.category}, {spent.date}\n")
            return True
        return False