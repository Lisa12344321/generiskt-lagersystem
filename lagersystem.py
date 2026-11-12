from typing import TypeVar, Generic

T = TypeVar("T")

class Lager(Generic[T]):
    def __init__(self):
        self.__lagerhylla: list[T] = []

    def lägg_till(self, vara: T):
        self.__lagerhylla.append(vara)

    def ta_bort(self):
        if self.__lagerhylla:
            return self.__lagerhylla.pop()

    def get_lagerhylla(self) -> list[T]:
        return self.__lagerhylla


lager = Lager[object]()
print(lager.get_lagerhylla())



# class Vara(Generic[T]):
#     def __init__(self, namn: T):
#         self.__namn = namn

#     def get_namn(self) -> T:
#         return self.__namn


# lager = Lager[object]()
# vara1 = Vara[str]("hej")

# lager.lägg_till(vara1)
# print([vara.get_namn() for vara in lager.get_lagerhylla()])