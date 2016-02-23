from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.is_idle = True

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str
        """
        return "{}, Location: ({}), Speed: {}, is_idle: {}"\
            .format(self.id,
                    str(self.location),
                    str(self.speed),
                    str(self.is_idle))

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool
        """
        return type(self), self.id, self.location, self.speed, self.is_idle == \
               type(other), other.id, other.location, other.speed, other.is_idle

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int
        """
        return int(manhattan_distance(self.location, destination)/self.speed)

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int
        """
        # Use self.speed to model passage of time as driving
        travel_time = get_travel_time(self, location)

        #

        pass

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        pass

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int
        """
        # Learns identity of the Rider and destination, use get_travel_time
        pass

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        pass
