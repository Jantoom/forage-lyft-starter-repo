from src.serviceable import Serviceable
from src.engine import Engine
from src.battery import Battery

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        return self.engine.needs_service() or self.battery.needs_service()

