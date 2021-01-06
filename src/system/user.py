# Copyright (C) 2018-2020
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev
"""User Functions
The following functions give you access to view and edit users in the
Gateway.
"""

__all__ = [
    "addHoliday",
    "addRole",
    "addSchedule",
    "editHoliday",
    "editRole",
    "editSchedule",
    "getHoliday",
    "getHolidayNames",
    "getHolidays",
    "getRoles",
    "getSchedule",
    "getScheduledUsers",
    "getScheduleNames",
    "getSchedules",
    "getUser",
    "getUsers",
    "isUserScheduled",
    "removeHoliday",
    "removeRole",
    "removeSchedule",
]

import system.date

from java.lang import Object
from java.util import Locale


class AbstractScheduleModel(Object):
    def getScheduleForDay(self, cal):
        pass

    def getType(self):
        pass

    def isObserveHolidays(self):
        pass

    def setObserveHolidays(self, observeHolidays):
        pass


class ContactInfo(Object):
    def __init__(self, contactType=None, value=None):
        super(ContactInfo, self).__init__()
        self.contactType = contactType
        self.value = value


class HolidayModel(Object):
    """HolidayModel object."""

    def __init__(self, name, date, repeatAnnually):
        """HolidayModel instance.

        Args:
            name (str): The name.
            date (datetime): The date.
            repeatAnnually (bool): Repeat annually.
        """
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def isRepeatedAnnually(self):
        return self.repeatAnnually


class ScheduleModel(Object):
    pass


class UIResponse(Object):
    def __init__(self, locale):
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass


class User(object):
    Username = "johdoe"
    FirstName = "John"
    LastName = "Doe"
    Email = "johdoe@mycompany.com"
    Notes = "These are some notes."
    Roles = ["Administrator", "Developer"]
    Schedule = "Always"
    Language = "en_US"

    def get(self, prop):
        """Returns a the value of the requested item.

        Args:
            prop (User property): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        print self
        return prop

    def getContactInfo(self):
        """Returns a sequence of ContactInfo objects. Each of these
        objects will have a contactType and value property representing
        the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        print self
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getId(self):
        """Returns the internal identifier object that the backing user
        source needs to identify this user.

        Returns:
            str: The internal identifier object that the backing user
                source needs to identify this user.
        """
        print self
        return 1

    def getOrDefault(self, prop):
        """Returns a default value if the requested item is not present.

        Args:
            prop (User property): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        print self
        return prop

    def getRoles(self):
        """Returns a sequence of strings representing the roles that
        this user belongs to.

        Returns:
             list[str]: Sequence of strings representing the roles that
                this user belongs to.
        """
        print self
        return User.Roles


def addHoliday(holiday):
    """Allows a holiday to be added.

    Args:
        holiday (HolidayModel): The holiday to add.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the add.
    """
    print holiday
    return UIResponse(Locale.ENGLISH)


def addRole(userSource, role):
    """Allows a role to the specified user source. When altering the
    Gateway System User Source, the Allow User Admin setting must be
    enabled.

    Args:
        userSource (str): The user source to add a role to. Blank will
            use the default user source.
        role (str): The role to add. Role must not be blank and must not
            already exist.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the add.
    """
    print (userSource, role)
    return UIResponse(Locale.ENGLISH)


def addSchedule(schedule):
    """Allows a schedule to be added.

    Args:
        schedule (AbstractScheduleModel): The schedule to add.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the add.
    """
    print schedule
    return UIResponse(Locale.ENGLISH)


def editHoliday(holidayName, holiday):
    """Allows a holiday to be edited.

    Args:
        holidayName (str): The name of the holiday to edit. Name is
            case-sensitive.
        holiday (HolidayModel): The edited holiday.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print (holidayName, holiday)
    return UIResponse(Locale.ENGLISH)


def editRole(userSource, oldName, newName):
    """Renames a role in the specified user source. When altering the
    Gateway System User Source, the Allow User Admin setting must be
    enabled.

    Args:
        userSource (str): The user source in which the role is found.
            Blank will use the default user source.
        oldName (str): The role to edit. Role must not be blank and must
            exist.
        newName (str): The new name for the role. Must not be blank.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print (userSource, oldName, newName)
    return UIResponse(Locale.ENGLISH)


def editSchedule(scheduleName, schedule):
    """Allows a schedule to be edited.

    Args:
        scheduleName (str): The name of the schedule to edit. Name is
            case-sensitive.
        schedule (AbstractScheduleModel): The edited schedule.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print (scheduleName, schedule)
    return UIResponse(Locale.ENGLISH)


def getHoliday(holidayName):
    """Returns a specific holiday.

    Args:
        holidayName (str): The name of the holiday to return.
            Case-sensitive.

    Returns:
        HolidayModel: The holiday, or None if not found.
    """
    print holidayName
    return None


def getHolidayNames():
    """Returns a collection of Strings of all holiday names.

    Returns:
        list[str]: A list of all holiday names, or an empty list if no
            holidays are defined.
    """
    return ["Labor Day", "Groundhog Day"]


def getHolidays():
    """Returns a sequence of all of the holidays available.

    Returns:
        list[HolidayModel]: A list of holidays.
    """
    return None


def getRoles(userSource):
    """Returns a sequence of strings representing all of the roles
    configured in a specific user source.

    Args:
        userSource (str): The user source to fetch the roles for.

    Returns:
        list[str]: A List of Strings that holds all the roles in the
            user source.
    """
    print userSource
    return None


def getSchedule(scheduleName):
    """Returns a specific schedule.

    Args:
        scheduleName (str): The name of the schedule to return.
            Case-sensitive.

    Returns:
         AbstractScheduleModel: The schedule, which can be a
            BasicSchedule, CompositeSchedule, or another type registered
            by a module, or None if not found.
    """
    print scheduleName
    return None


def getScheduledUsers(userSource, date=None):
    """Returns a list of users that are scheduled on. If no users are
    scheduled, it will return an empty list.

    Args:
        userSource (str): The name of the user source to check for
            scheduled users.
        date (object): The date to check schedules for. May be a Java
            Date or Unix Time in ms.. If omitted, the current date and
            time will be used. Optional.

    Returns:
        list[User]: List of all Users scheduled for the given date,
            taking schedule adjustments into account.
    """
    date = system.date.now() if date is None else date
    print (userSource, date)
    return None


def getScheduleNames():
    """Returns a sequence of strings representing the names of all of
    the schedules available.

    Returns:
        list[str]: A List of Strings that holds the names of all the
            available schedules.
    """
    return ["A", "Always", "B", "C", "Example", "MyComposite", "MySchedule"]


def getSchedules():
    """Returns a sequence of all available schedule models, which can be
    used to return configuration information on the schedule, such as
    time for each day of the week.

    Returns:
        list[ScheduleModel]: A list of ScheduleModel objects.
            ScheduleModel objects can be a Basic Schedule, Composite
            Schedule (composed of exactly two other schedules), or
            another type registered by a module.
    """
    return [ScheduleModel()]


def getUser(userSource, username):
    """Looks up a specific user in a user source, by username. The full
    User object is returned except for the user's password.

    Args:
        userSource (str): The name of the user source to search for the
            user in.
        username (str): The username of the user to search for.

    Returns:
        User: A User object.
    """
    print (userSource, username)
    return User()


def getUsers(userSource):
    """Retrieves the list of users in a specific user source. The User
    objects that are returned contain all of the information about that
    user, except for the user's password.

    Args:
        userSource (str): The name of the user source to find the users
            in.

    Returns:
        list[User]: A list of User objects.
    """
    print userSource
    # You may return more than one User object.
    return [User()]


def isUserScheduled(user, date=None):
    """Will check if a specified User is scheduled currently or on a
    specified date/time.

    Args:
        user (User): The user object to check the schedule for.
        date (object): The date to check schedules for. May be a Java
            Date or Unix Time in ms. If omitted, the current date and
            time will be used. Optional.

    Returns:
        bool: True if the user is scheduled for the specified date,
            False if not.
    """
    date = system.date.now() if date is None else date
    print (user, date)
    return True


def removeHoliday(holidayName):
    """Allows a holiday to be deleted.

    Args:
        holidayName (str): The name of the holiday to delete. Name is
            case-sensitive.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print holidayName
    return UIResponse(Locale.ENGLISH)


def removeRole(userSource, role):
    """Removes a role from the specified user source. When altering the
    Gateway System User Source, the Allow User Admin setting must be
    enabled.

    Args:
        userSource (str): The user source in which the role is found.
            Blank will use the default user source.
        role (str): The role to remove. The role must exist.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print (userSource, role)
    return UIResponse(Locale.ENGLISH)


def removeSchedule(scheduleName):
    """Allows a schedule to be deleted. Note that schedules which are
    used in Composite Schedules can not be deleted until they are
    removed from the Composite Schedule.

    Args:
        scheduleName (str): The name of the schedule to delete. Name is
            case-sensitive.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print scheduleName
    return UIResponse(Locale.ENGLISH)
