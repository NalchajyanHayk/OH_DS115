import enum
from abc import ABC, abstractmethod


class Person(ABC):
    __max_parking_lots = 50
    __used_parking_lots = 0

     def __init__(self, id: int, name: str, surname: str, gender: enum, birth_year: int, email: str, has_parking_lot: bool):
         self._id = id
         self._name = name
         self._surname = surname
         self._gender = gender
         self._birth_year = birth_year
         self._email = email
         self._has_parking_lot = has_parking_lot

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_sur):
        self._surname = new_sur

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gen):
        self._gender = new_gen

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.usage
    def birth_year(self, new_birth):
        self._birth_year = new_birth


    @abstractmethod
    def book_parking_lot(self) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_age(self) -> int:
        pass

    @classmethod
    def get_available_parking_lots(self) -> int:
        pass



