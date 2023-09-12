from datetime import datetime
from src.car import Car
from src.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from src.battery import NubbinBattery, SpindlerBattery

class CarFactory():

    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear: [float]) -> Car:
        """Creates a Calliope model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at
            tire_wear ([float]): The wear on each of the four tires, 0 to 1 inclusive

        Returns:
            Car: An instance of the Calliope model
        """
        calliope = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date)
        )

        return calliope
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear: [float]) -> Car:
        """Creates a Glissade model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at
            tire_wear ([float]): The wear on each of the four tires, 0 to 1 inclusive

        Returns:
            Car: An instance of the Glissade model
        """
        glissade = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date)
        )

        return glissade
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_wear: [float]) -> Car:
        """Creates a Palindrome model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            warning_light_on (bool): The status of the car's warning light. True if on, otherwise False
            tire_wear ([float]): The wear on each of the four tires, 0 to 1 inclusive

        Returns:
            Car: An instance of the Palindrome model
        """
        palindrome = Car(
            SternmanEngine(warning_light_on),
            NubbinBattery(current_date, last_service_date)
        )

        return palindrome
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear: [float]) -> Car:
        """Creates a Rorschach model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at
            tire_wear ([float]): The wear on each of the four tires, 0 to 1 inclusive

        Returns:
            Car: An instance of the Rorschach model
        """
        rorschach = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date)
        )

        return rorschach
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear: [float]) -> Car:
        """Creates a Thovex model based off information from the existing car.

        Args:
            current_date (datetime): Today's date
            last_service_date (datetime): The date that the car was last serviced
            current_mileage (int): The current mileage of the car
            last_service_mileage (int): The mileage that the car was last serviced at
            tire_wear ([float]): The wear on each of the four tires, 0 to 1 inclusive

        Returns:
            Car: An instance of the Thovex model
        """
        thovex = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date)
        )

        return thovex
