from abc import ABC, abstractmethod
from sys import _enablelegacywindowsfsencoding
from servicable import servicable

class Car(servicable, ABC):
    def __init__(self, last_service_date): 
        self.last_service_date = last_service_date

    
    @abstractmethod
    def needs_service(self):
        pass
