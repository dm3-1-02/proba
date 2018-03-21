class Produktuak:
    def __init__(self,produktuID,izena,prezioa,kompainia):
        self.produktuID=produktuID
        self.izena=izena
        self.prezioa=prezioa
        self.kompainia=kompainia
class Jokoak(Produktuak):
    def _init_(self,generoa,data, produktuID, izena, prezioa, kompainia):
        self.generoa=generoa
        self.data=data
        Produktuak.__init__(self, produktuID, izena, prezioa, kompainia)
class kontsolak(Produktuak):
    def _init_(self,jokoak, produktuID, izena, prezioa, kompainia):
        self.jokoak=jokoak
        Produktuak.__init__(self, produktuID, izena, prezioa, kompainia)
class osagarriak(Produktuak):
    def __init__(self, produktuID, izena, prezioa, kompainia):
        Produktuak.__init__(self, produktuID, izena, prezioa, kompainia)
        print("xxxxxxxxxxxxxxxxxddddddddddddddddddd")
