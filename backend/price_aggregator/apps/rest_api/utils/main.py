from .selenium_session import Session, SessionManager
from .parser import Parser


class Perekrestok_prices_receiver:
    def __init__(self, name):
        self._name = name
        self._run()

    @property
    def session(self):
        if not hasattr(self, '_received'):
            setattr(self, '_session', Session())
        return self._session

    @property
    def received(self):
        return self._received

    @received.setter
    def received(self, value):
        if not hasattr(self, '_received'):
            setattr(
                self, '_received', {'source': 'www.perekrestok.ru','data': []}
                )
        self._received['data'].append(value)

    def _run(self):
        with SessionManager(self.session):
            page = 1
            while True:
                try:
                    result = self._parse_data(self._get_data(page))
                except TypeError:
                    break
                else:
                    self._add_received(result)
                finally:
                    page += 1

    def _get_data(self, page):
        data = self.session.get(page, self._name)
        if not data:
            raise TypeError
        return data

    def _parse_data(self, html):
        result = Parser(html).parse()
        if not result:
            raise TypeError
        return result

    def _add_received(self, data):
        for el in data.items():
            name = el[0]
            price = el[1]
            self.received = {'name': name, 'price': price}

