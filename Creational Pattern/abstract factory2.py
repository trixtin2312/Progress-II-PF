from abc import ABC, abstractmethod

class Browser(ABC):
    """
    Membuat abstract produk A
    """

    @abstractmethod
    def create_search_toolbar(self):
        pass

    @abstractmethod
    def create_browser_window(self):
        pass

class Messenger(ABC):
    """
    Membuat abstract produk B
    """

    @abstractmethod
    def create_messenger_window(self):
        pass

class EdgeBrowser(Browser):
    """
    Concrete produk
    Mengimpementasikan metode abstract pada kelas dasar Browser
    """

    def create_search_toolbar(self):
        print("Alat Pencarian Dibuat!")

    def create_browser_window(self):
        print("Jendela Peramban Dibuat")


class EdgeMessenger(Messenger):
    """
    Concrete produk
    Mengimpementasikan metode abstract pada kelas dasar Messenger
    """

    def create_messenger_window(self):
        print("Jendela Messenger Dibuat")

class KeamananBrowser(Browser):
    """
    Concrete produk
    Mengimpementasikan metode abstract pada kelas dasar Browser
    """

    # Browser base class
    def create_search_toolbar(self):
        print("Browser Aman - Alat Pencarian Dibuat")

    # Browser base class
    def create_browser_window(self):
        print("Browser Aman - Jendela Pencarian Dibuat")

    def create_incognito_mode(self):
        print("Browser Aman - Mode Penyamaran Dibuat")


class KeamananMassanger(Messenger):
    """
    Concrete produk
    Mengimpementasikan metode abstract pada kelas dasar Browser
    """

    # Messenger base class
    def create_messenger_window(self):
        print("Messenger Aman - Jendela Messenger Dibuat")

    def create_privacy_filter(self):
        print("Messenger Aman - Filter Privasi Dibuat")

    def disappearing_messages(self):
        print("Messenger Aman - Fitur Pesan Menghilang Diaktifkan")

class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass

class EdgeProdukFac(AbstractFactory):
    """
    Concrete Factory
    Mengimplentasikan operasi berikut untuk membuat concrete dari objek produk
    """

    def create_browser(self):
        return EdgeBrowser()

    def create_messenger(self):
        return EdgeMessenger()

class KeamananProduk(AbstractFactory):
    """
    Concrete Factory
    Mengimplentasikan operasi berikut untuk membuat concrete dari objek produk
    """

    def create_browser(self):
        return KeamananBrowser()

    def create_messenger(self):
        return KeamananMassanger()

def main():
    for factory in (EdgeProdukFac(), KeamananProduk()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()

if __name__ == "__main__":
    main()