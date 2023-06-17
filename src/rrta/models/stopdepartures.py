from enum import Enum
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


class ModeReportLabel(Enum):
    Normal = "Normal"


class PropertyName(Enum):
    RRTA = "RRTA"


class PStatusReportLabel(Enum):
    Scheduled = "Scheduled"


class DirectionCode(Enum):
    L = "L"
    O = "O"


@dataclass
class Trip:
    IVRServiceDesc: None
    BlockFareboxId: Optional[int] = None
    GtfsTripId: Optional[str] = None
    InternalSignDesc: Optional[str] = None
    InternetServiceDesc: Optional[str] = None
    StopSequence: Optional[int] = None
    TripDirection: Optional[DirectionCode] = None
    TripId: Optional[int] = None
    TripRecordId: Optional[int] = None
    TripStartTime: Optional[str] = None
    TripStartTimeLocalTime: Optional[datetime] = None
    TripStatus: Optional[int] = None
    TripStatusReportLabel: Optional[PStatusReportLabel] = None


@dataclass
class Departure:
    ADT: None
    ADTLocalTime: None
    ATA: None
    ATALocalTime: None
    Bay: None
    Dev: Optional[datetime] = None
    EDT: Optional[str] = None
    EDTLocalTime: Optional[datetime] = None
    ETA: Optional[str] = None
    ETALocalTime: Optional[datetime] = None
    IsCompleted: Optional[bool] = None
    IsLastStopOnTrip: Optional[bool] = None
    LastUpdated: Optional[str] = None
    LastUpdatedLocalTime: Optional[datetime] = None
    Mode: Optional[int] = None
    ModeReportLabel: Optional[ModeReportLabel] = None
    PropogationStatus: Optional[int] = None
    SDT: Optional[str] = None
    SDTLocalTime: Optional[datetime] = None
    STA: Optional[str] = None
    STALocalTime: Optional[datetime] = None
    StopFlag: Optional[int] = None
    StopStatus: Optional[int] = None
    StopStatusReportLabel: Optional[PStatusReportLabel] = None
    Trip: Optional[Trip] = None
    PropertyName: Optional[PropertyName] = None


@dataclass
class RouteDirection:
    HeadwayDepartures: None
    Departures: Optional[List[Departure]] = None
    Direction: Optional[str] = None
    DirectionCode: Optional[DirectionCode] = None
    IsDone: Optional[bool] = None
    IsHeadway: Optional[bool] = None
    IsHeadwayMonitored: Optional[bool] = None
    RouteId: Optional[int] = None
    RouteRecordId: Optional[int] = None


@dataclass
class StopDeparture:
    LastUpdated: Optional[str] = None
    RouteDirections: Optional[List[RouteDirection]] = None
    StopId: Optional[int] = None
    StopRecordId: Optional[int] = None
