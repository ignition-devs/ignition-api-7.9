__all__ = ["AlarmQueryResult"]


class AlarmQueryResult:
    """This is the result of a query against the alarming system, for
    both status and history.

    It provides the results as a list, but also provides additional
    helper functions for getting the event and associated data as a
    dataset.
    """

    def __init__(self):
        pass

    def getAssociatedDate(self, uuid):
        pass

    def getDataSet(self):
        pass

    def getEvent(self, uuid):
        pass
