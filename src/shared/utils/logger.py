import datetime
import general as GeneralUtils


class LoggerUtils:
    def __init__(self, tag: str):
        self.tag = tag

    def log_error(self, message: str, error: Exception):
        date = GeneralUtils.format_full_date_time(datetime.datetime.now())
        print(f"[{date}] {self.tag}: {message} - {error}", file=sys.stderr)

    def log_warn(self, message: str, *optional_params):
        date = GeneralUtils.format_full_date_time(datetime.datetime.now())
        print(f"[{date}] {self.tag}: {message}", *optional_params)

    def log_info(self, message: str, *optional_params):
        date = GeneralUtils.format_full_date_time(datetime.datetime.now())
        print(f"[{date}] {self.tag}: {message}", *optional_params)
