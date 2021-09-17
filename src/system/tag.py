"""Tag Functions.

The following functions give you access to interact with Ignition Tags.
"""

__all__ = [
    "addTag",
    "browseConfiguration",
    "browseHistoricalTags",
    "browseTags",
    "browseTagsSimple",
    "editAlarmConfig",
    "editTag",
    "editTags",
    "exists",
    "getAlarmStates",
    "isOverlaysEnabled",
    "loadFromFile",
    "queryTagCalculations",
    "queryTagDensity",
    "queryTagHistory",
    "read",
    "readAll",
    "removeTag",
    "removeTags",
    "scan",
    "setOverlaysEnabled",
    "storeTagHistory",
    "write",
    "writeAll",
    "writeAllSynchronous",
    "writeSynchronous",
]

import pprint

import system.date
from com.inductiveautomation.ignition.common.browsing import BrowseResults
from com.inductiveautomation.ignition.common.model.values import QualifiedValue
from com.inductiveautomation.ignition.common.script.builtin.ialabs import (
    BrowseTag,
    TagAlarmDefinition,
)
from com.inductiveautomation.ignition.common.tags.config import (
    TagConfiguration,
)
from java.util import Date


def addTag(
    parentPath,
    name,
    tagType,
    dataType,
    accessRights,
    enabled,
    value,
    attributes,
    parameters,
    overrides,
    alarmList,
    alarmConfig,
):
    """Adds a new tag in Ignition.

    You can add OPC, memory, expression, query, folder, and UDT instance
    tags. You can't add Client Tags, because those can vary from project
    to project.

    Args:
        parentPath (str): The folder to add the tag to. Leave blank for
            the root folder.
        name (str): The name of the tag.
        tagType (str): The type of tag to create. Possible values are
            OPC, MEMORY, EXPRESSION, QUERY, Folder, and UDT_INST.
        dataType (str): The data type of the tag. Not used for UDT
            instances or folders. Possible basic values are Int1, Int2,
            Int4, Int8, Float4, Float8, Boolean, String, DataSet, and
            DateTime. Possible array values are Int4Array, Int8Array,
            Float8Array, BooleanArray, StringArray, DateTimeArray.
        accessRights (str): The access rights for a tag. Possible values
            are Read_Only, Read_Write, and Custom.
        enabled (bool): If True, the tag will be enabled.
        value (object): The value of the tag. Used for memory tags.
        attributes (dict): The tag's configuration attributes.
        parameters (dict): The parameters for a UDT instance tag.
        overrides (dict): All of the overrides for a UDT instance tag.
        alarmList (str): List of legacy alarms for the tag. The legacy
            alarm system was retired in 7.6.0, so the alarmConfig
            parameter should be utilized on newer versions.
        alarmConfig (dict): The alarm configuration for the tag. See
            editAlarmConfig for details on how to use this parameter.
    """
    pprint.pprint(
        [
            parentPath,
            name,
            tagType,
            dataType,
            accessRights,
            enabled,
            value,
            attributes,
            parameters,
            overrides,
            alarmList,
            alarmConfig,
        ]
    )


def browseConfiguration(path, recursive):
    """Browses a folder path or UDT and returns Tag configuration
    information for each Tag within the specified path.

    This can be used to view event scripts, alarms, as well as any other
    configurable attribute on a Tag.

    Args:
        path (str): The path that will be browsed, typically to a folder
            or UDT instance. Leave blank to browse the root folder. A
            Tag Provider may be specified as follows: "[TagProvider]".
            If the Tag Provider is omitted, client scoped calls will be
            made against the project's default provider. Gateway scoped
            calls must include a Tag Provider. When browsing UDTs,
            specifying the UDT path will browse the Tags inside the UDT.
            To browse the UDT instance, specify the parent of the
            instance.
        recursive (bool): If True, will recursively search for Tags in
            folders. Each folder will return a 'tags' property
            containing the nested TagConfigurations in another list.

    Returns:
        list(TagConfiguration): A list of TagConfiguration objects.
            Attributes on the object may be read by calling
            tag.get(propertyObject). A list of attributes with
            configuration information can be obtained by calling
            getProperties(). Only attributes with non-default values
            will appear in the attribute list.
    """
    pprint.pprint([path, recursive])
    return [TagConfiguration()]


def browseHistoricalTags(
    path, nameFilters=None, maxSize=None, continuationPoint=None
):
    """Will browse for any historical Tags at the provided historical
    path.

    It will only browse for Tags at the path, and will not go down
    through any children. Will return with a BrowseResults object.

    Args:
        path (str): The Historical Tag Path to browse. See the Tag
            Export page for a description of how to construct a
            historical Tag Path.
        nameFilters (list[str]): A list of name filters to be applied to
            the result set. Optional.
        maxSize (int): The maximum size of the result set. Optional.
        continuationPoint (object): Sets the continuation point in order
            to continue a browse that was previously started and then
            limited. Use .getContinuationPoint() on the BrowseResults
            object to get the continuation point. Optional.

    Returns:
        BrowseResults: An object that contains the results as well as
            the Continuation Point. Get the results by calling
            .getResults() on the BrowseResults object.
    """
    pprint.pprint([path, nameFilters, maxSize, continuationPoint])
    return BrowseResults()


def browseTags(
    parentPath,
    tagPath=None,
    tagType=None,
    dataType=None,
    udtParentType=None,
    recursive=False,
    sort="ASC",
):
    """Returns an array of tags from a specific folder.

    The function supports filtering and recursion. Leave filters blank
    to return all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        tagPath (str): Filters on a tag path. Use * as a wildcard for
            any number of characters and a ? for a single character.
            Optional.
        tagType (str): Filters on a tag type. Possible values are OPC,
            MEMORY, DB, QUERY, Folder, DERIVED and UDT_INST. Optional.
        dataType (str): The data type of the tag. Not used for UDT
            instances or folders. Possible values are Int1, Int2, Int4,
            Int8, Float4, Float8, Boolean, String, and DateTime.
            Optional.
        udtParentType (str): The name of the parent UDT. Optional.
        recursive (bool): Recursively search for tags inside of folders.
            Note: It is highly recommended that recursive is set to
            False, as server timeouts are more likely to occur.
            Optional.
        sort (str): Sets the sort order, possible values are ASC and
            DESC. Sorting is done on the full path of the tag. Optional.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the
            following variables: name, path, fullPath, type, dataType,
            and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    pprint.pprint(
        [
            parentPath,
            tagPath,
            tagType,
            dataType,
            udtParentType,
            recursive,
            sort,
        ]
    )
    return [BrowseTag()]


def browseTagsSimple(parentPath, sort):
    """Returns a sorted array of tags from a specific folder.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        sort (str): Sets the sort order, possible values are ASC and
            DESC.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the
            following variables: name, path, fullPath, type, dataType,
            and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    pprint.pprint([parentPath, sort])
    return [BrowseTag()]


def editAlarmConfig(tagPaths, alarmConfig):
    """Edit the alarm configuration of multiple existing tags in
    Ignition with a single call.

    Args:
        tagPaths (list[str]): The full path to the tag you want to edit.
            Note: you can specify the tag provider name in square
            brackets at the beginning of the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off then the project default provider will be used.
        alarmConfig (dict): A dictionary of multi-dimensional lists
            containing the new alarm configuration. The key in the
            dictionary will be the name of the alarm being to edit, and
            the value is a list of lists. The nested lists use the
            format ["name", "Value", "newValue"]. Note that item 1 is
            always "Value".
    """
    pprint.pprint([tagPaths, alarmConfig])


def editTag(
    tagPath,
    attributes=None,
    parameters=None,
    accessRights=None,
    overrides=None,
    alarmList=None,
    alarmConfig=None,
):
    """Edits an existing Tag in Ignition.

    This will not work on Client Tags, because there is a Client
    Provider for each project.

    Args:
        tagPath (str): The full path to the Tag you want to edit. For
            members of UDT instances, the tagPath will be the path to
            the UDT instance, with the overrides parameter listing out
            the member Tags to edit. Note: you can specify the Tag
            provider name in square brackets at the beginning of the
            parentPath string. Example: "[myTagProvider]MyTagsFolder".
            If the Tag provider name is left off then the project
            default provider will be used.
        attributes (dict): The Tag's configuration attributes. Optional.
        parameters (dict): The parameters for a UDT instance Tag.
            Optional.
        accessRights (string): The access rights for the Tags. Possible
            values are Read_Only, Read_Write, and Custom. Optional.
        overrides (dict): All of the overrides for a UDT instance Tag.
            The dictionary should be in the form of the names of member
            Tags as keys, with the values being a dictionary of
            properties/overrides ie. {'memberTagName':{dictionary of
            overrides}}. Optional.
        alarmList (str): List of legacy alarms for the Tag. The legacy
            alarm system was retired in 7.6.0. Newer systems should
            utilize the system.tag.editAlarmConfig function instead.
            Optional.
        alarmConfig (dict): The alarm configuration for the Tag. Note
            that this parameter cannot edit alarms on UDTs. Instead, the
            system.tag.editAlarmConfig function (which can also edit
            alarms on non-UDT Tags) should be used instead. See
            editAlarmConfig for details on how to use this parameter.
            Optional.
    """
    pprint.pprint(
        [
            tagPath,
            attributes,
            parameters,
            accessRights,
            overrides,
            alarmList,
            alarmConfig,
        ]
    )


def editTags(
    tagPaths,
    attributes,
    parameters,
    accessRights,
    overrides,
    alarmList,
    alarmConfig,
    provider,
    json,
):
    """Edit multiple existing Tags in Ignition with a single call.

    This will not work on Client Tags, because there is a Client
    Provider for each project.

    Args:
        tagPaths (list[str]): The full path to the Tag you want to edit.
            For members of UDT instances, the tagPath will be the path
            to the UDT instance, with the overrides parameter listing
            out the member Tags to edit. Note: you can specify the Tag
            provider name in square brackets at the beginning of the
            parentPath string. Example: "[myTagProvider]MyTagsFolder".
            If the Tag provider name is left off then the project
            default provider will be used.
        attributes (dict): The Tag's configuration attributes.
        parameters (dict): The parameters for a UDT instance Tag.
        accessRights (str): The access rights for a Tag. Possible values
            are Read_Only, Read_Write, and Custom.
        overrides (dict): All of the overrides for a UDT instance Tag.
        alarmList (str): List of legacy alarms for the Tag. The legacy
            alarm system was retired in 7.6.0, so the alarmConfig
            parameter should be utilized on newer versions.
        alarmConfig (dict): The alarm configuration for the Tag.
        provider (str): The name of the Tag provider, used in
            conjunction with the JSON argument. The default value is the
            default Tag provider. Optional.
        json (str): The properties to edit on Tags, represented as a
            JSON object. When using this, it acts as a replacement for
            other parameters. Optional.
    """
    pprint.pprint(
        [
            tagPaths,
            attributes,
            parameters,
            accessRights,
            overrides,
            alarmList,
            alarmConfig,
            provider,
            json,
        ]
    )


def exists(tagPath):
    """Checks whether or not a tag with a given path exists.

    Args:
        tagPath (str): The path of the tag to look up.

    Returns:
        bool: True if a tag exists for the given path, False otherwise.
    """
    pprint.pprint(tagPath)
    return True


def getAlarmStates(tagPath):
    """Returns an array of alarm definitions for a specific tag.

    Args:
        tagPath (str): The full path to the tag. Note: you can specify
            the tag provider name in square brackets at the beginning of
            the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off then the project default provider will be used.

    Returns:
        list[TagAlarmDefinition]: An array of TagAlarmDefinition.
    """
    pprint.pprint(tagPath)
    return [TagAlarmDefinition("alarm", None)]


def isOverlaysEnabled():
    """Returns whether or not the current client's quality overlay
    system is currently enabled.

    Returns:
         bool: True (1) if overlays are currently enabled.
    """
    return False


def loadFromFile(filePath, provider, mode):
    """This function locates an exported tag file and loads the tags
    into the specified tag provider.

    Args:
        filePath (str): The path of the tag file to import from.
        provider (str): The name of the provider to import to.
        mode (int): Dictates what happens if the tag already exists.
            0 = overwrite, 1 = ignore.
    """
    pprint.pprint([filePath, provider, mode])


def queryTagCalculations(
    paths,
    calculations,
    startDate=None,
    endDate=None,
    rangeHours=None,
    rangeMinutes=None,
    aliases=None,
    includeBoundingValues=True,
    validatesSCExec=True,
    noInterpolation=False,
    ignoreBadQuality=False,
):
    """Queries various calculations (aggregations) for a set of tags
    over a specified range.

    Returns a dataset with a row per tag, and a column per calculation.

    This is useful when you wish to aggregate tag history collected over
    a period of time into a single value per aggregate. If you want
    multiple values aggregated to a single time slice (i.e., hourly
    aggregates for the same tag over an 8 hour period) consider using
    system.tag.queryTagHistory

    Args:
        paths (list[str]): An array of tag paths (strings) to query
            calculations for. The resulting dataset will have a row for
            each tag, and a column for each calculation.
        calculations (list[str]): An array of calculations (aggregation
            functions) to execute for each tag. Valid values are:
            "Average" (time-weighted), "MinMax", "LastValue",
            "SimpleAverage", "Sum", "Minimum", "Maximum", "DurationOn",
            "DurationOff", "CountOn", "CountOff", "Count", "Range",
            "Variance", "StdDev", "PctGood", and "PctBad".
        startDate (Date): The starting point for the calculation
            window. If omitted, and range is not used, 8 hours before
            the current time is used. Optional.
        endDate (Date): The end of the calculation window. If
            omitted, and range is not used, uses the current time.
            Optional.
        rangeHours (int): Allows you to specify the query range in
            hours, instead of using start and end date. Can be positive
            or negative, and can be used in conjunction with startDate
            or endDate. Optional.
        rangeMinutes (int): Same as rangeHours, but in minutes.
            Optional.
        aliases (list[str]): Aliases that will be used to override the
            tag path names in the result dataset. Must be 1-to-1 with
            the tag paths. If not specified, the tag paths themselves
            will be used. Optional.
        includeBoundingValues (bool): A boolean flag indicating that the
            system should attempt to load values before and after the
            query bounds for the purpose of interpolation. The effect
            depends on the aggregates used. The default is "True".
            Optional.
        validatesSCExec (bool): A boolean flag indicating whether or not
            data should be validated against the scan class execution
            records. If False, calculations may include data that is
            assumed to be good, even though the system may not have been
            running. Default is "True". Optional.
        noInterpolation (bool): A boolean flag indicating that the
            system should not attempt to interpolate values in
            situations where it normally would, such as for analog tags.
            Default is "False". Optional.
        ignoreBadQuality (bool): A boolean flag indicating that bad
            quality values should not be used in the query process. If
            set, any value with a "bad" quality will be completely
            ignored in calculations. Default is "False". Optional.

    Returns:
        Dataset: A dataset representing the calculations over the
            specified range.
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
    pprint.pprint(
        [
            paths,
            calculations,
            startDate,
            endDate,
            rangeHours,
            rangeMinutes,
            aliases,
            includeBoundingValues,
            validatesSCExec,
            noInterpolation,
            ignoreBadQuality,
        ]
    )


def queryTagDensity(paths, startDate, endDate):
    """Queries the Tag history system for information about the density
    of data.

    In other words, how much data is available for a given time
    span.

    This function is called with a list of Tag paths, and a start and
    end date. The result set is a two column dataset specifying the
    timestamp, and a relative weight. Each row is valid from the given
    time until the next row. Tags are assigned a 1 or a 0 if they are
    present or not. All values are then multiplied together to get a
    decimal based percentage for the density. Thus, for four Tag paths
    passed in, if three Tags were present during the span, the result
    would be 0.75.

    Args:
        paths (list[str]): An array of Tag paths (strings) to query.
        startDate (Date): The start of the range to query.
        endDate (Date): The end of the range to query.

    Returns:
        Dataset: A 2-column dataset consisting of a timestamp and a
            weight. Each row is valid until the next row.
    """
    pprint.pprint([paths, startDate, endDate])
    return [0, 0]


def queryTagHistory(
    paths,
    startDate=None,
    endDate=None,
    returnSize=-1,
    aggregationMode="Average",
    returnFormat="Wide",
    columnNames=None,
    intervalHours=None,
    intervalMinutes=None,
    rangeHours=None,
    rangeMinutes=None,
    aggregationModes=None,
    includeBoundingValues=None,
    validateSCExec=None,
    noInterpolation=None,
    ignoreBadQuality=None,
    timeout=None,
):
    """Issues a query to the Tag Historian.

    Querying tag history involves specifying the tags and the date
    range, as well as a few optional parameters. The Tag historian will
    find the relevant history and then interpolate and aggregate it
    together into a coherent, tabular result set.

    Args:
        paths (list[str]): An array of tag paths (strings) to query.
            Each tag path specified will be a column in the result
            dataset.
        startDate (Date): The earliest value to retrieve. If
            omitted, 8 hours before current time is used. Optional.
        endDate (Date): The latest value to retrieve. If omitted,
            current time is used. Optional.
        returnSize (int): The number of samples to return. -1 will
            return values as they changed, and 0 will return the
            "natural" number of values based on the logging rates of the
            scan class(es) involved. -1 is the default. Optional.
        aggregationMode (str): The mode to use when aggregating multiple
            samples into one time slice. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad". Optional.
        returnFormat (str): Use "Wide" to have a column per tag queried,
            or "Tall" to have a fixed-column format. Default is "Wide".
            Optional.
        columnNames (list[str]): Aliases that will be used to override
            the column names in the result dataset. Must be 1-to-1 with
            the tag paths. If not specified, the tag paths themselves
            will be used as column titles. Optional.
        intervalHours (int): Allows you to specify the window interval
            in terms of hours, as opposed to using a specific return
            size. Optional.
        intervalMinutes (int): Same as intervalHours, but in minutes.
            Can be used on its own, or in conjunction with
            intervalHours. Optional.
        rangeHours (int): Allows you to specify the query range in
            hours, instead of using start and end date. Can be positive
            or negative, and can be used in conjunction with startDate
            or endDate. Optional.
        rangeMinutes (int): Same as rangeHours, but in minutes.
            Optional.
        aggregationModes (list[str]): A one-to-one list with paths
            specifying an aggregation mode per column. Optional.
        includeBoundingValues (bool): A boolean flag indicating that the
            system should attempt to include values for the query bound
            times if possible. The default for this property depends on
            the query mode, so unless a specific behavior is desired, it
            is best to not include this parameter. Optional.
        validateSCExec (bool): A boolean flag indicating whether or not
            data should be validated against the scan class execution
            records. If False, data will appear flat (but good quality)
            for periods of time in which the system wasn't running. If
            True, the same data would be bad quality during downtime
            periods. Optional.
        noInterpolation (bool): A boolean flag indicating that the
            system should not attempt to interpolate values in
            situations where it normally would. This will also prevent
            the return of rows that are purely interpolated. Optional.
        ignoreBadQuality (bool): A boolean flag indicating that bad
            quality values should not be used in the query process. If
            set, any value with a "bad" quality will be completely
            ignored in calculations and in the result set. Optional.
        timeout (int): Timeout in milliseconds for Client Scope. This
            property is ignored in the Gateway Scope. Optional.

    Returns:
        Dataset: A dataset representing the historian values for the
            specified tag paths. The first column will be the timestamp,
            and each column after that represents a tag.
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
    pprint.pprint(
        [
            paths,
            startDate,
            endDate,
            returnSize,
            aggregationMode,
            returnFormat,
            columnNames,
            intervalHours,
            intervalMinutes,
            rangeHours,
            rangeMinutes,
            aggregationModes,
            includeBoundingValues,
            validateSCExec,
            noInterpolation,
            ignoreBadQuality,
            timeout,
        ]
    )


def read(tagPath):
    """Reads the value of the tag at the given tag path.

    Returns a qualified value object. You can read the value, quality,
    and timestamp from this object. If the tag path does not specify a
    tag property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the
    attribute to the tagPath parameter. See the Tag Attributes page for
    a list of available attributes.

    Args:
        tagPath (str): Reads from the given tag path. If no property is
            specified in the path, the Value property is assumed.

    Returns:
        QualifiedValue: A qualified value. This object has three
            sub-members: value, quality, and timestamp.
    """
    pprint.pprint(tagPath)
    return QualifiedValue()


def readAll(tagPaths):
    """Reads the values of each tag in the tag path list.

    Returns a sequence of qualified value objects. You can read the
    value, quality, and timestamp from each object in the return
    sequence. Reading in bulk like this is more efficient than calling
    read() many times.

    Args:
        tagPaths (list[str]): A sequence of tag paths to read from.

    Returns:
        list[QualifiedValue]: A sequence of qualified values
            corresponding to each tag path given. Each qualified value
            will have three sub-members: value, quality, and timestamp.
    """
    pprint.pprint(tagPaths)
    return [QualifiedValue() for _ in range(len(tagPaths))]


def removeTag(tagPath):
    """Removes a tag from Ignition.

    Args:
        tagPath (str): The path to the tag you want to remove. You can
            specify the tag provider name in square brackets at the
            beginning of the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off, then the project default provider will be used.
            Note that an empty path ( '' ) will remove all tags.
    """
    pprint.pprint(tagPath)


def removeTags(tagPaths):
    """Removes multiple tags from Ignition with a single call.

    Args:
        tagPaths (list[str]): An array of the paths to the tags you want
            to remove. You can specify the tag provider name in square
            brackets at the beginning of the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off, then the project default provider will be used.
            Note that an empty path (['']) will remove all tags.
    """
    pprint.pprint(tagPaths)


def scan(provider, scname):
    """Forces execution of a scan class.

    On a leased scan class, if both the fast and slow rate are set to 0,
    this will not execute.

    Args:
        provider (str): The name of the scan class provider. If blank,
            it will use the default. Required if used in the gateway
            scope.
        scname (str): The name of the scan class to execute.
    """
    pprint.pprint([provider, scname])


def setOverlaysEnabled(enabled):
    """Enables or disables the component quality overlay system.

    Args:
        enabled (bool): True (1) to turn on tag overlays, False (0) to
            turn them off.
    """
    pprint.pprint(enabled)


def storeTagHistory(
    historyprovider,
    tagprovider,
    paths,
    values,
    qualities=None,
    timestamps=None,
):
    """Inserts data into the tag history system, allowing Tag history to
    be recorded via scripting.

    The Tag paths are associated with a historical and realtime
    provider, but they do not necessarily need to exist in the realtime
    provider. This means records from non-existent (virtual) Tags can be
    stored in the Tag History system. Because of this, it is imperative
    that Tag paths passed to the function are typed precisely, otherwise
    the history will be stored at an incorrect path.

    Note that the Tag History system does cache tag data. Thus, if this
    function is called, the tag path and tag id are cached until the
    history provider or gateway are restarted. This means manually
    removing the tag from the sqlth_te table, and then calling this
    function again with the same path will not re-populate the tag
    execution table (especially so when working purely with virtual tag
    paths). Instead, the cache must first be cleared, and then a new
    entry will be added the next time this function is called.

    Args:
        historyprovider (str): The historical provider to store to.
        tagprovider (str): The name of the realtime tag provider to
            associate these tags with. The tag provider does not need to
            exist, and the tag paths do not need to exist in it.
        paths (list[str]): A list of paths to store. The values,
            qualities, and timestamps are one-to-one with the paths. A
            single path may be present multiple times in order to store
            multiple values.
        values (list[object]): A list of values to store.
        qualities (list[int]): A list of integer quality codes
            corresponding to the values. Quality codes can be found on
            the Tag Quality and Overlays page. If omitted, GOOD quality
            will be used. Optional.
        timestamps (list[Date]): A list of Date timestamps corresponding
            to the values. If omitted, the current time will be used. A
            java.util.date object may be passed, so the system.date
            functions can be used to return a timestamp. Optional.
    """
    pprint.pprint(
        [historyprovider, tagprovider, paths, values, qualities, timestamps]
    )


def write(tagPath, value, suppressErrors=False):
    """Writes a value to a tag.

    Note that this function writes asynchronously. This means that the
    function does not wait for the write to occur before returning - the
    write occurs sometime later on a different thread.

    Args:
        tagPath (str): The path of the tag to write to.
        value (object): The value to write.
        suppressErrors (bool): A flag indicating whether or not to
            suppress errors. Optional.

    Returns:
        int: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    pprint.pprint([tagPath, value, suppressErrors])
    return 1


def writeAll(tagPaths, values):
    """Performs an asynchronous bulk write.

    Takes two sequences that must have the same number of entries. The
    first is the list of tag paths to write to, and the second is a list
    of values to write. This function is dramatically more efficient
    than calling write multiple times.

    Args:
        tagPaths (list[str]): The paths of the tags to write to.
        values (list[object]): The values to write.

    Returns:
        list[int]: Array of ints with an element for each tag written
            to: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    pprint.pprint([tagPaths, values])
    return [1] * len(tagPaths)


def writeAllSynchronous(tagPaths, values, timeout=45000):
    """Performs a synchronous write to multiple tags.

    Synchronous means that execution will not continue until this
    function has completed, so you will know that a write has been
    attempted on the provided tags. The first write to fail or time out
    will throw an exception, but any subsequent tags in the provided
    list will still be attempted. This function cannot be called from
    the event dispatch thread, meaning it cannot be called directly from
    a GUI event like a button press without creating a new thread with a
    call to system.util.invokeAsynchronous. You can call this from
    project event scripts like timer scripts.

    Note that the order of the tags listed in the tagPaths parameter
    determines the order that the writes will occur.

    Args:
        tagPaths (list[str]): The paths of the tags to write to.
        values (list[object]): The values to write.
        timeout (int): How long to wait in milliseconds before timing
            out pending writes. The default is 45000 milliseconds.
            Optional.
    """
    pprint.pprint([tagPaths, values, timeout])


def writeSynchronous(tagPath, value, timeout=45000):
    """Performs a write to a tag, synchronously.

    This means that you know at the end of this function whether or not
    the write succeeded or not. A write that fails or times out will
    throw an error. However, this function cannot be called from the
    event dispatch thread, which means that it cannot be called directly
    from a GUI event like a button press, without wrapping it in a
    system.util.invokeAsynchronous. You can call this from project event
    scripts like timer scripts.

    Args:
        tagPath (str): The path of the tag to write to.
        value (object): The value to write.
        timeout (int): How long to wait in milliseconds before timing
            out pending writes. The default is 45000 milliseconds.
            Optional.
    """
    pprint.pprint([tagPath, value, timeout])
