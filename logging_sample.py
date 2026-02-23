import logging
import logging.config

logging.config.fileConfig(fname="conf/logger.conf")

logger = logging.getLogger("sampleLogger")
logger.debug("debugログ")
logger.info("infoログ")
logger.warning("warningログ")
logger.error("errorログ")
logger.critical("criticalログ")
