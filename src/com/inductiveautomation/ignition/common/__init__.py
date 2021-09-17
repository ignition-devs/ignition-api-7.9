__all__ = ["Dataset"]


class Dataset(object):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def getColumnCount(self):
        pass

    def getColumnIndex(self, name):
        pass

    def getColumnName(self, col):
        pass

    def getColumnNames(self):
        pass

    def getColumnType(self, col):
        pass

    def getPrimitiveValueAt(self, row, col):
        pass

    def getQualityAt(self, row, col):
        pass

    def getRowCount(self):
        pass

    def getValueAt(self, row, colName):
        pass
