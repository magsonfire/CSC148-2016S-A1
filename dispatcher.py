from driver import Driver
from rider import Rider


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
        @type _waitlist: PriorityQueue of Rider
        @type _fleet: PriorityQueue of Driver
        @rtype: None
        """
        self._waitlist = PriorityQueue()
        self._fleet = PriorityQueue()

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        return '{} {}'.format(str(self._waitlist), str(self._fleet))
    
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
                # Return first idle driver
                return driver
        else:
            # Add rider to waitlist
            self._waitlist.add(rider)

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
            
        # Check waitlist for waiting rider
        if rider in self._waitlist:
            return rider
        else:
            return None

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        rider.status = CANCELLED