from src.cliente.circulo_base import CirculoBase


class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super().__init__(id, limite)
        self.contatos = set()

    def getNumeroOfContacts(self):
        return len(self.contatos)

    def getNumberOfContacts(self):
        return len(self.contatos)

    def setLimite(self, limite: int):
        self.limite = limite

    def __eq__(self, other):
        if not isinstance(other, Circulo):
            return False
        return self.id == other.id and self.limite == other.limite

    def __lt__(self, other):
        return self.id < other.id
