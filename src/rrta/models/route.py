from dataclasses import dataclass
from typing import Optional, List, Any
from enum import Enum


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


class TextColor(Enum):
    FFFFFF = "FFFFFF"
    the000000 = "000000"


class CommStatus(Enum):
    GOOD = "GOOD"


class Direction(Enum):
    I = "I"
    L = "L"
    O = "O"


class DirectionLong(Enum):
    Inbound = "Inbound"
    Loop = "Loop"
    Outbound = "Outbound"


class OccupancyStatusReportLabel(Enum):
    Empty = "Empty"


class OpStatus(Enum):
    EARLY = "EARLY"
    ONTIME = "ONTIME"
    TRIPSTART = "TRIP START"


class PropertyName(Enum):
    RRTA = "RRTA"


@dataclass
class Vehicle:
    Deviation: None
    DisplayStatus: None
    CurrentStatus: None
    DriverLastName: None
    DriverFirstName: None
    OnBoard: None
    BlockFareboxId: Optional[int] = None
    CommStatus: Optional[CommStatus] = None
    Destination: Optional[str] = None
    Direction: Optional[Direction] = None
    DirectionLong: Optional[DirectionLong] = None
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
    OpStatus: Optional[OpStatus] = None
    RouteId: Optional[int] = None
    RunId: Optional[int] = None
    Speed: Optional[int] = None
    TripId: Optional[int] = None
    VehicleId: Optional[int] = None
    SeatingCapacity: Optional[int] = None
    TotalCapacity: Optional[int] = None
    PropertyName: Optional[PropertyName] = None
    OccupancyStatusReportLabel: Optional[OccupancyStatusReportLabel] = None


@dataclass
class Route:
    Directions: None
    GoogleDescription: None
    Group: None
    RouteStops: None
    RouteTraceHash64: None
    Stops: None
    Color: Optional[str] = None
    IncludeInGoogle: Optional[bool] = None
    IsHeadway: Optional[bool] = None
    IsHeadwayMonitored: Optional[bool] = None
    IsVisible: Optional[bool] = None
    IvrDescription: Optional[str] = None
    LongName: Optional[str] = None
    Messages: Optional[List[Message]] = None
    RouteAbbreviation: Optional[str] = None
    RouteId: Optional[int] = None
    RouteRecordId: Optional[int] = None
    RouteTraceFilename: Optional[str] = None
    SortOrder: Optional[int] = None
    ShortName: Optional[int] = None
    TextColor: Optional[TextColor] = None
    Vehicles: Optional[List[Vehicle]] = None
    DetourActiveMessageCount: Optional[int] = None
