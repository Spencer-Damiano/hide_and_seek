import random

class Seeker:
    """A code template for a the seeker who looks for the hider. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Hider.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Seeker (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = random.randint(1, 1000)
        self._distance = [0, 0] # start with two so get_message always works
    
    def get_location(self):
        """Gets the seeker's current location.
        
        Returns:
            number: The seeker's location,
        """
        return self._location
        
    def get_message(self):
        """Gets a message from the seeker.

        Args:
            self (Seeker): An instance of Seeker.
        
        Returns:
            string: A message from the seeker.
        """
        message = "\nI'm going to find you!"
        if self._distance[-1] == 0:
            message = "\nI'm going to find you!"
        elif self._distance[-1] < self._distance[-2]:
            message = "\nShhh. I'm sneaking in now..."
        elif self._distance[-1] > self._distance[-2]:
            message = "\nI'm running around, but I'll find you..."
        return message

    def move(self, location):
        """Moves to the given location and keeps track of the distance.

        Args:
            self (Seeker): An instance of Seeker.
        """
        distance = abs(self._location - location)
        self._distance.append(distance)
        self._location = location