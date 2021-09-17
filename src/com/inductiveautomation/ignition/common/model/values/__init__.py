__all__ = ["QualifiedValue", "Quality"]


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def getQuality(self):
        pass

    def getTimestamp(self):
        pass

    def getValue(self):
        pass


class Quality(object):
    def getDescription(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass
