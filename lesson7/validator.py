from exceptions import ValidationError
from datetime import datetime


class Data():

    def __init__(self, name, age):
        self.name = self._clear_whitespaces(name)
        self.age = int(self._clear_whitespaces(age))

    def _clear_whitespaces(self, data):
        return data.strip(" ")


class DataWithDate(Data):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.date_time = datetime.now()


class Validator():

    def __init__(self):
        self.data_history = []

    def _validate_name(self, name) -> None:
        if not name or len(name) <= 3 or name.count(" ") > 1:
            raise ValidationError

    def _validate_age(self, age) -> None:
        if age < 14:
            raise ValidationError

    def validate(self, data):
        self.data_history.append(data)
        if self.data_history:
            self._validate_name(
                self.data_history[-1].name)
            self._validate_age(
                self.data_history[-1].age)
        else:
            raise ValueError
