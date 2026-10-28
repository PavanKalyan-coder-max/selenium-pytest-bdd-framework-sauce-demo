from abc import ABC, abstractmethod


class BasePageInterface(ABC):

    @abstractmethod
    def click(self, locator, description="Element"):
        pass

    @abstractmethod
    def enter_text(self, locator, text):
        pass