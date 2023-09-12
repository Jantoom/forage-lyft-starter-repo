from src.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        if self.warning_light_is_on:
            return True
        else:
            return False
