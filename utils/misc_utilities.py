from functools import wraps
from time import time
import json

import logging
logger = logging.getLogger("boxes_demo_logger")
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        logger.info('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        return result

    return wrap


@timing
def read_json(f_name):
    with open(f_name) as f:
        fi = json.load(f)
