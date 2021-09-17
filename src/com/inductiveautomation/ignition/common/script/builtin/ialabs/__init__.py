__all__ = [
    "BrowseTag",
    "OPCBrowseTag",
    "TagAlarmDefinition",
    "TagAlarmProperty",
]

import pprint

from java.lang import Object


class BrowseTag(Object):
    def __init__(
        self,
        name=None,
        path=None,
        fullPath=None,
        type=None,
        valueSource=None,
        dataType=None,
    ):
        super(BrowseTag, self).__init__()
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type
        self.valueSource = valueSource
        self.dataType = dataType

    def getDataType(self):
        return self.dataType

    def getFullPath(self):
        return self.fullPath

    def getPath(self):
        return self.path

    def getTagType(self):
        return self.type

    def getValueSource(self):
        return self.valueSource

    def isDB(self):
        pprint.pprint(self)
        return True

    def isExpression(self):
        pprint.pprint(self)
        return True

    def isFolder(self):
        pprint.pprint(self)
        return True

    def isMemory(self):
        pprint.pprint(self)
        return True

    def isOPC(self):
        pprint.pprint(self)
        return True

    def isQuery(self):
        pprint.pprint(self)
        return True

    def isUDT(self):
        pprint.pprint(self)
        return True

    def toString(self):
        pass


class OPCBrowseTag(Object):
    def __init__(
        self,
        opcServer=None,
        type=None,
        displayName=None,
        displayPath=None,
        dataType=None,
        opcItemPath=None,
    ):
        super(OPCBrowseTag, self).__init__()
        self.opcServer = opcServer
        self.type = type
        self.displayName = displayName
        self.displayPath = displayPath
        self.dataType = dataType
        self.opcItemPath = opcItemPath

    def getDataType(self):
        return self.dataType

    def getDisplayName(self):
        return self.displayName

    def getDisplayPath(self):
        return self.displayPath

    def getOpcItemPath(self):
        return self.opcItemPath

    def getOpcServer(self):
        return self.opcServer

    def getType(self):
        return self.type


class TagAlarmDefinition(Object):
    def __init__(self, alarm, alarmProperties):
        self.alarm = alarm
        self.alarmProperties = alarmProperties

    def getAlarmProperties(self):
        pprint.pprint(self)
        return TagAlarmProperty()


class TagAlarmProperty(Object):
    def __init__(self, property=None, value=None, type=None):
        self.property = property
        self.type = type
        self.value = value
