from src.engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        return self.current_mileage - self.last_service_mileage > 60000
