from dataclasses import dataclass
from models.category import Category

@dataclass
class Spent:
    value: float
    category: Category
    date: str

    def __str__(self):
        return f"Spent(valor={self.value}, category={self.category.name}, date={self.date})"