#class for creating enums
from enum import Enum

# Define an Enum for room status
class room_status(Enum):
    # Enum member for an available room
    AVAILABLE = 1

    # Enum member for a booked room
    BOOKED = 2
