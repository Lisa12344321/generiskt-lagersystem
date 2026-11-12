from typing import TypeVar, Generic

T = TypeVar("T") #global

class Lager(Generic[T]):
    antal_varor = 0 #klassvariabel

    def __init__(self):
        self.__lagerhylla: list[T] = [] #instansvariabel


    def lägg_till(self, vara: T):
        Lager.antal_varor += 1
        self.__lagerhylla.append(vara)


    def ta_bort(self) -> T | None:
        antal = len(self.__lagerhylla) #lokal

        def kontrollera_lager():
            return antal > 0 # tar antal från den yttre metoden

        if kontrollera_lager():
            Lager.antal_varor -= 1
            return self.__lagerhylla.pop()
        
        return None

    
    def get_lagerhylla(self) -> list[T]:
        return self.__lagerhylla



class Vara():
    def __init__(self, namn: str, pris: int):
        self.namn = namn #instansvariabel
        self.pris = pris #instansvariabel



lager = Lager[Vara]() #global
vara1 = Vara("Daim", 15) #global
vara2 = Vara("Dumle", 10) #global
vara3 = Vara("Geisha", 5) #global

lager.lägg_till(vara1)
lager.lägg_till(vara2)
lager.lägg_till(vara3)

print([f"{vara.namn}: {vara.pris} kr" for vara in lager.get_lagerhylla()])
print(f"Antal varor: {lager.antal_varor}")
lager.ta_bort()
print([f"{vara.namn}: {vara.pris} kr" for vara in lager.get_lagerhylla()])
print(f"Antal varor: {lager.antal_varor}")


# ---------------------------------------
# 1.
# En klassvariabel lever under hela körningen av programmmet eftersom en klass kan användas närsomhelst för att det typ är som en ritning.
# En lokal variabel i en metod lever bara när metoden körs och kan inte nås efter det. Variabeln finns bara inom metoden.

# 2.
# Den kan inte det eftersom de lokala variablerna i en helt annan metod bara kan användas inom den metoden och sedan dör de.
