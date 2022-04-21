from abc import ABC, abstractmethod
from operator import methodcaller

class servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass