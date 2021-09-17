__all__ = ["AbstractScheduleModel", "HolidayModel"]

from java.lang import Object


class AbstractScheduleModel(Object):
    def getScheduleForDay(self, cal):
        pass

    def getType(self):
        pass

    def isObserveHolidays(self):
        pass

    def setObserveHolidays(self, observeHolidays):
        pass


class HolidayModel(Object):
    def __init__(self, name, date, repeatAnnually):
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def isRepeatedAnnually(self):
        return self.repeatAnnually
