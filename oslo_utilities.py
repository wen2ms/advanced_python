from oslo_utils import strutils, timeutils, uuidutils, versionutils
from datetime import datetime, timedelta, timezone

try:
    strutils.check_string_length("foo", name="username", min_length=7, max_length=8)
except (TypeError, ValueError) as e:
    print(f"Validate Error: {e}")

print(strutils.bool_from_string("yes"))

print(timeutils.utcnow())

past_time = datetime.now(timezone.utc) - timedelta(hours=2)
print(timeutils.is_older_than(past_time, 3600))

print(uuidutils.generate_uuid())

print(versionutils.convert_version_to_int("2.3.4"),versionutils.convert_version_to_int("2.3.77"))