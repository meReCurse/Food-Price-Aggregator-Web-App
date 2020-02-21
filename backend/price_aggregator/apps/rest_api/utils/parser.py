from bs4 import BeautifulSoup


class Parser(BeautifulSoup):
    def __init__(self, content):
        super().__init__(content, 'html5lib')

    def parse(self):
        def form_name_list(catalogue):
            names = []
            attr = "data-gtm-product-name"
            for item in catalogue.find_all('div'):
                if attr in item.attrs:
                    names.append(item[attr])
            return names

        def form_price_list(catalogue):
            prices = []
            attr = "itemprop"
            for item in catalogue.find_all('span'):
                if attr in item.attrs and item[attr] == 'price':
                    prices.append(item.text)
            return prices

        catalogue = self.find('ul', {"id": "catalogItems"})
        if not catalogue:
            return False

        names = form_name_list(catalogue)
        prices = form_price_list(catalogue)
        return dict(zip(names, prices))


if __name__ == '__main__':
    pass
