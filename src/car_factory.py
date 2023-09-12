from datetime import datetime
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import NubbinBattery, SpindlerBattery

class CarFactory():

    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        """Creates a Calliope model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at

        Returns:
            Car: An instance of the Calliope model
        """
        calliope = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date)
        )

        return calliope
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        """Creates a Glissade model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at

        Returns:
            Car: An instance of the Glissade model
        """
        glissade = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date)
        )

        return glissade
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
        """Creates a Palindrome model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            warning_light_on (bool): The status of the car's warning light. True if on, otherwise False

        Returns:
            Car: An instance of the Palindrome model
        """
        palindrome = Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(current_date, last_service_date)
        )

        return palindrome
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        """Creates a Rorschach model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at

        Returns:
            Car: An instance of the Rorschach model
        """
        rorschach = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date)
        )

        return rorschach
    
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        """Creates a Thovex model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at

        Returns:
            Car: An instance of the Thovex model
        """
        thovex = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date)
        )

        return thovex
