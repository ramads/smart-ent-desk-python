from abc import abstractmethod


class BasePage:
    @abstractmethod
    def drawPage(self, data = None):
        raise NotImplementedError("Method drwaPage() harus diimplementasi!")