from datetime import datetime
from src.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date: datetime, last_service_date: datetime):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
