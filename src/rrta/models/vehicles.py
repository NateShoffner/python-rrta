from enum import Enum
from dataclasses import dataclass
from typing import Optional


class CommStatus(Enum):
    BADGPS = "BAD GPS"
    GOOD = "GOOD"


class Direction(Enum):
    D = "D"
    I = "I"
    L = "L"
    O = "O"


class DirectionLong(Enum):
    Deadhead = "Deadhead"
    Inbound = "Inbound"
    Loop = "Loop"
    Outbound = "Outbound"


class OccupancyStatusReportLabel(Enum):
    Empty = "Empty"


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
    OpStatus: Optional[str] = None
    RouteId: Optional[int] = None
    RunId: Optional[int] = None
    Speed: Optional[int] = None
    TripId: Optional[int] = None
    VehicleId: Optional[int] = None
    SeatingCapacity: Optional[int] = None
    TotalCapacity: Optional[int] = None
    PropertyName: Optional[PropertyName] = None
    OccupancyStatusReportLabel: Optional[OccupancyStatusReportLabel] = None
