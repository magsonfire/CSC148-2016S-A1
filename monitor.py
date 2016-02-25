from location import Location
from driver import Driver
from rider import Rider

"""
The Monitor module contains the Monitor class, the Activity class,
and a collection of constants. Together the elements of the module
help keep a record of activities that have occurred.

Activities fall into two categories: Rider activities and Driver
activities. Each activity also has a description, which is one of
request, cancel, pickup, or dropoff.

=== Constants ===
@type RIDER: str
    A constant used for the Rider activity category.
@type DRIVER: str
    A constant used for the Driver activity category.
@type REQUEST: str
    A constant used for the request activity description.
@type CANCEL: str
    A constant used for the cancel activity description.
@type PICKUP: str
    A constant used for the pickup activity description.
@type DROPOFF: str
    A constant used for the dropoff activity description.
"""

RIDER = "rider"
DRIVER = "driver"

REQUEST = "request"
CANCEL = "cancel"
PICKUP = "pickup"
DROPOFF = "dropoff"


class Activity:
    """An activity that occurs in the simulation.

    === Attributes ===
    @type timestamp: int
        The time at which the activity occurred.
    @type description: str
        A description of the activity.
    @type identifier: str
        An identifier for the person doing the activity.
    @type location: Location
        The location at which the activity occurred.
    """

    def __init__(self, timestamp, description, identifier, location):
        """Initialize an Activity.

        @type self: Activity
        @type timestamp: int
        @type description: str
        @type identifier: str
        @type location: Location
        @rtype: None
        """
        self.description = description
        self.time = timestamp
        self.id = identifier
        self.location = location


class Monitor:
    """A monitor keeps a record of activities that it is notified about.
    When required, it generates a report of the activities it has recorded.
    """

    # === Private Attributes ===
    # @type _activities: dict[str, dict[str, list[Activity]]]
    #       A dictionary whose key is a category, and value is another
    #       dictionary. The key of the second dictionary is an identifier
    #       and its value is a list of Activities.

    def __init__(self):
        """Initialize a Monitor.

        @type self: Monitor
        """
        self._activities = {
            RIDER: {},
            DRIVER: {}
        }
        """@type _activities: dict[str, dict[str, list[Activity]]]"""

    def __str__(self):
        """Return a string representation.

        @type self: Monitor
        @rtype: str
        """
        return "Monitor ({} drivers, {} riders)".format(
                len(self._activities[DRIVER]), len(self._activities[RIDER]))

    def notify(self, timestamp, category, description, identifier, location):
        """Notify the monitor of the activity.

        @type self: Monitor
        @type timestamp: int
            The time of the activity.
        @type category: DRIVER | RIDER
            The category for the activity.
        @type description: REQUEST | CANCEL | PICKUP | DROPOFF
            A description of the activity.
        @type identifier: str
            The identifier for the actor.
        @type location: Location
            The location of the activity.
        @rtype: None
        """
        if identifier not in self._activities[category]:
            self._activities[category][identifier] = []

        activity = Activity(timestamp, description, identifier, location)
        self._activities[category][identifier].append(activity)

    def report(self):
        """Return a report of the activities that have occurred.

        @type self: Monitor
        @rtype: dict[str, object]
        """
        return {"rider_wait_time": self._average_wait_time(),
                "driver_total_distance": self._average_total_distance(),
                "driver_ride_distance": self._average_ride_distance()}

    def _average_wait_time(self):
        """Return the average wait time of riders that have either been picked
        up or have cancelled their ride.

        @type self: Monitor
        @rtype: float
        """
        wait_time = 0
        count = 0
        for activities in self._activities[RIDER].values():
            # A rider that has less than two activities hasn't finished
            # waiting (they haven't cancelled or been picked up).
            if len(activities) >= 2:
                # The first activity is REQUEST, and the second is PICKUP
                # or CANCEL. The wait time is the difference between the two.
                wait_time += activities[1].time - activities[0].time
                count += 1
        return wait_time / count

    def _average_total_distance(self):

        """Return the average distance drivers have driven.

        @type self: Monitor
        @rtype: float
        """
        total_dist = 0
        count = 0

        for driver in self._activities[DRIVER]:
            #Find each driver's total distance
           total_dist += get_riderless_distance(driver) + \
                get_ride_distance(driver)
           count += 1
        #Add them up and divide by nummber of drivers
        return total_dist / count

    def _average_ride_distance(self):
        """Return the average distance drivers have driven on rides.

        @type self: Monitor
        @rtype: float
        """
        total_dist = 0
        count = 0

        for driver in self._activities[DRIVER]:
            total_dist += get_ride_distance(driver)

            count += 1

        return total_dist / count

    def get_riderless_distance(self, driver):
        """Return the total distance travelled without a rider by driver.

        @type self: Monitor
        @type driver: str
        @rtype: int
        """
        total_dist = 0

        # Scan through activities list of given driver
        for i in range(len(self._activities[DRIVER][driver]) - 1):
            current = self._activities[DRIVER][driver][i]
            next = self._activities[DRIVER][driver][i + 1]
            # If activity is REQUEST
            if REQUEST in current.description:
                # Add distance between activity and next activity to total
                dist = manhattan_distance(current.location, next.location)
                total_dist += dist

        # Return total riderless distance
        return total_dist


        #This can be more efficient
    def get_ride_distance(self, driver):
        """Return the total distance travelled with a rider by driver.

        @type self: Monitor
        @type driver: str
        @rtype: int
        """
        total_dist = 0

        # Scan through activities list of given driver
        for i in range(len(self._activities[DRIVER][driver]) - 1):
            current = self._activities[DRIVER][driver][i]
            next = self._activities[DRIVER][driver][i + 1]
            # If activity is PICKUP followed by DROPOFF
            if PICKUP in current.description and DROPOFF in next.description:
            # Add distance between activity and next activity to total
                dist = manhattan_distance(current.location, next.location)
                total_dist += dist

        # Return total distance with rider
        return total_dist

#Get ridda dis!
def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int

    >>> manhattan_distance(Location(0,0), Location(3,4))
    7
    >>> manhattan_distance(Location(3,4), Location(0,0))
    7
    >>> manhattan_distance(Location(3,4), Location(3,4))
    0
    """
    return abs(destination.row - origin.row) + \
           abs(destination.column - origin.column)

if __name__ == '__main__':
    m = Monitor()
    m.notify(1, DRIVER, REQUEST, 'a', Location(0,0))
    m.notify(2, DRIVER, PICKUP, 'a', Location(1,1))
    print(m.get_riderless_distance('a'))
    m.notify(3, DRIVER, DROPOFF, 'a', Location(2,2))
    print(m.get_riderless_distance('a'))
    m.notify(4, DRIVER, REQUEST, 'a', Location(2,2))
    m.notify(4, DRIVER, PICKUP, 'a', Location(3,6))
    print(m.get_riderless_distance('a'))


#!!!WE MAY HAVE TO CHANGE PICKUP IN EVENT, IF RIDER CANCELS IS PICKUP STILL COUNTED??
