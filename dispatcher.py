from driver import Driver
from rider import Rider
from container import Queue(), PriorityQueue()


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @type _riders: Queue of Rider
        @type _fleet: PriorityQueue of Driver
        @rtype: None
        """
        self._waitlist = Queue()
        self._fleet = PriorityQueue()

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        return '{} {}'.format(str(self._riders), str(self._fleet))

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """

        # Check fleet for idle driver
        for driver in _fleet:
            if driver.is_idle:
    #I added this
                driver.is_idle = False
                return driver
        else:
            self._waitlist.add(rider)
            return None
        # Is there a way to get a driver who's also closer, not just faster?
        # Fleet is now sorted in order of driver speed

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """
        # Add driver to fleet if new
        if driver not in self._fleet:
            self._fleet.add(driver)

        # If riders list is not empty, assign a rider

        if not self._waitlist.is_empty:
            rider = self._waitlist[0]
            return rider

        else:
            return None

# Waitlist currently sorted by patience

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
#the rider can cancel if they arent in a waitlist (I think) I should check if they are removed from the waitlist when a driver is assigned or when they are picked up (in Pickup class in event)

#Okay, I will need to remove rider from the waitlist when driver is assigned so that two drivers dont go for the same rider. Do this in Pickup event class

        if rider in waitlist:
            self._waitlist.remove(rider)

        rider._set_status(CANCELLED)
