import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")

logging.debug("this is debug logging.")
logging.info("this is info logging.")
logging.warning("this is warning logging.")
logging.error("this is error logging.")
logging.critical("this is critical logging.")