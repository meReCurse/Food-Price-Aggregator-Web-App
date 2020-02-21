class UrlConstructor:
    def __init__(self):
        self.destination = 'https://www.perekrestok.ru/catalog/search?'
        self.data_page = 'page='
        self.data_sort = '&sort=weight_desc'
        self.data_text = '&text='

    def construct(self, page, search):
        return '{0}{1}{2}{3}{4}{5}'.format(
            self.destination,
            self.data_page,
            page,
            self.data_sort,
            self.data_text,
            search
            )
