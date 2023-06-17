from dataclasses import dataclass
from typing import Optional


@dataclass
class Stop:
    Description: Optional[str] = None
    IsTimePoint: Optional[bool] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    Name: Optional[str] = None
    StopId: Optional[int] = None
    StopRecordId: Optional[int] = None
