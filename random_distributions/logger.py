import logging
import os

import progressbar

from random_distributions import __name__

LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO

progressbar.streams.wrap_stderr()
log = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOGGING_FORMAT))

log.addHandler(handler)
log.setLevel(LEVEL)
