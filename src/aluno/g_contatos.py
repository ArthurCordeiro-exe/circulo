from src.aluno.base.circulo import Circulo
from src.aluno.base.contato import Contato
from src.cliente.icirculo_operations_manager import ICirculoOperationsManager
from src.cliente.icirculos_manager import ICirculosManager
from src.cliente.icontatos_manager import IContatosManager
from src.cliente.circulo_not_found_exception import CirculoNotFoundException
from src.cliente.contato_not_found_exception import ContatoNotFoundException


class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):

    def __init__(self):
        self.contatos = {}
        self.circulos = {}
        self.favoritos = set()


    def createContact(self, id: str, email: str) -> bool:
        if id in self.contatos:
            return False
        self.contatos[id] = Contato(id, email)
        return True

    def getAllContacts(self) -> list:
        return sorted(self.contatos.values())

    def updateContact(self, contato: Contato) -> bool:
        if contato.getId() not in self.contatos:
            return False
        self.contatos[contato.getId()].setEmail(contato.getEmail())
        return True

    def removeContact(self, id: str) -> bool:
        if id not in self.contatos:
            return False

        for circulo in self.circulos.values():
            circulo.contatos.discard(id)

        self.favoritos.discard(id)
        del self.contatos[id]
        return True

    def getContact(self, id: str) -> Contato:
        return self.contatos.get(id)

    def getNumberOfContacts(self) -> int:
        return len(self.contatos)

    def favoriteContact(self, idContato: str) -> bool:
        if idContato not in self.contatos:
            return False
        self.favoritos.add(idContato)
        return True

    def unfavoriteContact(self, idContato: str) -> bool:
        if idContato not in self.contatos:
            return False
        self.favoritos.discard(idContato)
        return True

    def isFavorited(self, id: str) -> bool:
        return id in self.favoritos

    def getFavorited(self) -> list:
        return sorted([self.contatos[id] for id in self.favoritos])


    def createCircle(self, id: str, limite: int) -> bool:
        if id in self.circulos or limite <= 0:
            return False
        self.circulos[id] = Circulo(id, limite)
        return True

    def updateCircle(self, circulo: Circulo) -> bool:
        if circulo.getId() not in self.circulos or circulo.getLimite() <= 0:
            return False
        self.circulos[circulo.getId()].setLimite(circulo.getLimite())
        return True

    def getCircle(self, idCirculo: str) -> Circulo:
        return self.circulos.get(idCirculo)

    def getAllCircles(self) -> list:
        return sorted(self.circulos.values())

    def removeCircle(self, idCirculo: str) -> bool:
        if idCirculo not in self.circulos:
            return False
        del self.circulos[idCirculo]
        return True

    def getNumberOfCircles(self) -> int:
        return len(self.circulos)


    def tie(self, idContato: str, idCirculo: str) -> bool:
        if idContato not in self.contatos:
            raise ContatoNotFoundException(idContato)

        if idCirculo not in self.circulos:
            raise CirculoNotFoundException(idCirculo)

        circulo = self.circulos[idCirculo]

        if idContato in circulo.contatos:
            return False

        if circulo.getNumberOfContacts() >= circulo.getLimite():
            return False

        circulo.contatos.add(idContato)
        return True

    def untie(self, idContato: str, idCirculo: str) -> bool:
        if idContato not in self.contatos:
            raise ContatoNotFoundException(idContato)

        if idCirculo not in self.circulos:
            raise CirculoNotFoundException(idCirculo)

        return self.circulos[idCirculo].contatos.discard(idContato) is None

    def getContacts(self, id: str) -> list:
        if id not in self.circulos:
            raise CirculoNotFoundException(id)

        contatos = [
            self.contatos[cid]
            for cid in self.circulos[id].contatos
        ]
        return sorted(contatos)

    def getCircles(self, id: str) -> list:
        if id not in self.contatos:
            raise ContatoNotFoundException(id)

        circulos = []
        for circulo in self.circulos.values():
            if id in circulo.contatos:
                circulos.append(circulo)

        return sorted(circulos)

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        if idContato1 not in self.contatos:
            raise ContatoNotFoundException(idContato1)
        if idContato2 not in self.contatos:
            raise ContatoNotFoundException(idContato2)

        comuns = []
        for circulo in self.circulos.values():
            if idContato1 in circulo.contatos and idContato2 in circulo.contatos:
                comuns.append(circulo)

        return sorted(comuns)
