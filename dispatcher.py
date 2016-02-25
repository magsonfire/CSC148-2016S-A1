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
        fastest_driver = None

        # Set driver to first available one
        for driver in self._fleet:
            if driver.is_idle:
                # Set idle driver to comparator
                fastest_driver = driver
            # Otherwise, no drivers are available
            else:
                self._waitlist.add(rider)
                return None

        # Compare rest of fleet to first idle driver
        for driver in self._fleet:
            # If next idle driver is faster than current one
            if driver.get_travel_time(rider.location)\
                    < fastest_driver.get_travel_time(rider.location):
                # Set driver to next one
                fastest_driver = driver

        fastest_driver.is_idle = False
        return fastest_driver

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
        # If waitlist is not empty, assign a rider
        if not self._waitlist.is_empty:
            return self._waitlist[0]
        else:
            return None

    def remove_from_waitlist(self, rider):
        """Remove the rider from the waitlist
        
        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        # Find index of rider to remove
        for i in range(len(self._waitlist) - 1):
            if rider.id == self._waitlist[i].id:
                # Remove rider
                dispatcher.waitlist.remove(i)
                
    def cancel_ride(self, rider):
        """Cancel the ride for rider and change their status to CANCELLED.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        rider.status = CANCELLED                
                
    def end_wait(self, rider):
        """End the rider's wait and change their status to SATISFIED.
        
        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        rider.status = SATISFIED