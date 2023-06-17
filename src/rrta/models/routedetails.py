from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Any


class Dir(Enum):
    L = "L"


@dataclass
class Direction:
    DirectionDesc: None
    DirectionIconFileName: None
    Dir: Optional[Dir] = None


@dataclass
class ChannelMessage:
    ChannelId: Optional[int] = None
    ChannelMessageTranslations: Optional[List[Any]] = None
    Message: Optional[str] = None


@dataclass
class Message:
    URL: None
    DetourId: None
    SharedMessageKey: None
    Cause: Optional[int] = None
    CauseReportLabel: Optional[str] = None
    Header: Optional[str] = None
    ChannelMessages: Optional[List[ChannelMessage]] = None
    DaysOfWeek: Optional[int] = None
    Effect: Optional[int] = None
    EffectReportLabel: Optional[str] = None
    FromDate: Optional[str] = None
    FromTime: Optional[str] = None
    Message: Optional[str] = None
    MessageId: Optional[int] = None
    MessageTranslations: Optional[List[Any]] = None
    Priority: Optional[int] = None
    PublicAccess: Optional[int] = None
    Published: Optional[bool] = None
    Routes: Optional[List[int]] = None
    Signs: Optional[List[int]] = None
    ToDate: Optional[str] = None
    ToTime: Optional[str] = None
    IsPrimaryRecord: Optional[bool] = None


@dataclass
class RouteStop:
    Direction: Optional[Dir] = None
    RouteId: Optional[int] = None
    SortOrder: Optional[int] = None
    StopId: Optional[int] = None


@dataclass
class Stop:
    Description: Optional[str] = None
    IsTimePoint: Optional[bool] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    Name: Optional[str] = None
    StopId: Optional[int] = None
    StopRecordId: Optional[int] = None


@dataclass
class Vehicle:
    Deviation: None
    DisplayStatus: None
    CurrentStatus: None
    DriverLastName: None
    DriverFirstName: None
    OnBoard: None
    BlockFareboxId: Optional[int] = None
    CommStatus: Optional[str] = None
    Destination: Optional[str] = None
    Direction: Optional[Dir] = None
    DirectionLong: Optional[str] = None
    StopId: Optional[int] = None
    DriverName: Optional[str] = None
    DriverFareboxId: Optional[int] = None
    VehicleFareboxId: Optional[int] = None
    GPSStatus: Optional[int] = None
    Heading: Optional[int] = None
    LastStop: Optional[str] = None
    LastUpdated: Optional[str] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    Name: Optional[int] = None
    OccupancyStatus: Optional[int] = None
    OpStatus: Optional[str] = None
    RouteId: Optional[int] = None
    RunId: Optional[int] = None
    Speed: Optional[int] = None
    TripId: Optional[int] = None
    VehicleId: Optional[int] = None
    SeatingCapacity: Optional[int] = None
    TotalCapacity: Optional[int] = None
    PropertyName: Optional[str] = None
    OccupancyStatusReportLabel: Optional[str] = None


@dataclass
class RouteDetails:
    GoogleDescription: None
    Group: None
    RouteTraceHash64: None
    IvrDescription: Optional[int] = None
    LongName: Optional[int] = None
    RouteAbbreviation: Optional[int] = None
    ShortName: Optional[int] = None
    Color: Optional[str] = None
    Directions: Optional[List[Direction]] = None
    IncludeInGoogle: Optional[bool] = None
    IsHeadway: Optional[bool] = None
    IsHeadwayMonitored: Optional[bool] = None
    IsVisible: Optional[bool] = None
    Messages: Optional[List[Message]] = None
    RouteId: Optional[int] = None
    RouteRecordId: Optional[int] = None
    RouteStops: Optional[List[RouteStop]] = None
    RouteTraceFilename: Optional[str] = None
    SortOrder: Optional[int] = None
    Stops: Optional[List[Stop]] = None
    TextColor: Optional[str] = None
    Vehicles: Optional[List[Vehicle]] = None
    DetourActiveMessageCount: Optional[int] = None
