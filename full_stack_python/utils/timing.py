from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def get_utc_now(tz_name: str = "UTC") -> datetime:
    """Get current time in specified timezone."""
    if tz_name == "UTC":
        return datetime.now(timezone.utc)
    return datetime.now(ZoneInfo(tz_name))


# def get_utc_now() -> datetime:
#     return datetime.now(timezone.utc)
