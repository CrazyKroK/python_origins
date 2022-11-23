class Phone:
    def __init__(self, model_phone, id_phone):
        self.model = model_phone
        self._id = id_phone  # Инкапсулирует метод id protected (см. ниже)
        self._loading()  # Запускает метод _loading автоматически при создании представителя класса
        self.__bla = "qwe"  # Второй метод инкапсуляции (privat).

    def call(self):
        print('calling')

    def _loading(self):  # Прячет метод loading за счет нижнего подчеркивания. Ее теперь нельзя вызвать работая с
                          # объектом класса Phone. Прием икапсуляции (protected).
        print(self.model, 'loading...')

    def get_id(self):  # Дает возможность добраться до инкапсулированного id protected, но не изменять его.
        return self._id


# my_phone = Phone('nokia1100', '12345')
# my_phone.call()
# print(my_phone._Phone__bla)  # Способ добраться до инкапсуляции Privat
# print(my_phone.get_id())

class SmartPhone(Phone):  # Наследует все методы от класса Phone.
    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


class IPhone(SmartPhone):
    def __init__(self, model_phone):
        super().__init__(model_phone)  # дополнеяет метод init информацией из класса Phone. По сути мы скомбинировали
                                       # новый и старый init
        print('show apple')

    def player(self):
        print('playing')

    def sms(self):
        print('imessage sending')
