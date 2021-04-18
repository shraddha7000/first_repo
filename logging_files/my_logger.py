import logging

import traceback

logging.basicConfig(filename="mylog.log", filemode='a+', format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__file__)
print(__file__)
print("logging.CRITICAL", logging.CRITICAL)
print("logging.ERROR", logging.ERROR)
print("logging.WARNING", logging.WARNING)
print("logging.INFO", logging.INFO)
print("logging.DEBUG", logging.DEBUG)
logger.setLevel(logging.ERROR)

if __name__ == "__main__":
    try:
        l = [1, 23, 3]
        print(l[100]) # raise InderError()
    except Exception as index_err_obj:
        print(index_err_obj)
        print(traceback.format_exc())
        logger.critical(traceback.format_exc())
        logger.error("This error message")
        logger.warning("This warning message.")
        logger.info("This info message.")
        logger.debug("This debug message.")
