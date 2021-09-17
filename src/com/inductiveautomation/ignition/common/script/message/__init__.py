__all__ = ["Request", "RequestWatcher"]


class RequestWatcher(object):
    def block(self):
        pass

    def compose(self, requestWatchers):
        pass


class Request(RequestWatcher):
    def cancel(self):
        pass

    def checkTimeout(self):
        pass

    def dispatchFunc(self):
        pass

    def finishExceptionally(self, e):
        pass

    def finishSuccessfully(self, value):
        pass

    def get(self):
        pass

    def getError(self):
        pass

    def getLongId(self):
        pass

    def internalOperationCompleted(self):
        pass

    def internalWait(self):
        pass

    def onError(self, func):
        pass

    def onSuccess(self, func):
        pass

    def startTime(self):
        pass
