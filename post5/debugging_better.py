from loguru import logger
import sys

sys.tracebacklimit = -1


def compute_nth_fibonacci_number_good(n):
    try:
        if n <= 0:
            raise Exception("Number can't be negative")
        # assert(n > 0), "Number can't be negative"

        if n > 15:
            return "Not supported"
        if n == 1:
            return 1
        if n == 2:
            return 1
        return compute_nth_fibonacci_number_good(n - 1) + compute_nth_fibonacci_number_good(n - 2)
    except Exception as e:
        logger.exception(f"This isn't going to work - {e}")
        return None
