import logging

# Create an configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "./Lumberjack.log", level = logging.ERROR, format = LOG_FORMAT, filemode='w')
logger = logging.getLogger()

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
