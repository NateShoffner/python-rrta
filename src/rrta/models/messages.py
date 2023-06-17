from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class ChannelMessage:
    ChannelId: Optional[int] = None
    ChannelMessageTranslations: Optional[List[Any]] = None
    Message: Optional[str] = None


@dataclass
class Message:
    URL: None
    Detour_Id: None
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
