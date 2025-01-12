from msilib.schema import Class
from datetime import datetime
from car import Car

class spindler_battery(Car):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
