from datetime import date, datetime, time, timezone
from typing import Optional

def ensure_datetime(d: Optional[date]) -> Optional[datetime]:
    if d is None:
        return None
    return datetime.combine(d, time.min, tzinfo=timezone.utc)