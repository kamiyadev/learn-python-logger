import logging
import logging.config

logging.config.fileConfig(fname="conf/logger_rotation.conf")

logger = logging.getLogger("sampleLogger")

import time

for _ in range(10):
    logger.debug("debugログ")
    logger.info("infoログ")
    logger.warning("warningログ")
    logger.error("errorログ")
    logger.critical("criticalログ")
    time.sleep(1)
