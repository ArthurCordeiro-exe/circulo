from src.cliente.exception_base import ExceptionBase

class CirculoNotFoundException(ExceptionBase):

    def __init__(self, circuloId: str, message="Circulo não encontrado"):
        self.circuloId = circuloId
        super().__init__(message)

    def getCirculoNaoEncontrado(self):
        return self.circuloId
