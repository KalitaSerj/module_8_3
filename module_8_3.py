class IncorrectVinNumber(Exception):
    def __init__(self, message='Некорректный тип vin номер'):
        self.message = message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message='Некорректный тип данных для номеров'):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.vin = vin
        self.numbers = numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

    def __is_valid_vin(self):
        self.is_valid_vin(self.vin)

    def __is_valid_numbers(self):
        self.is_valid_numbers(self.numbers)