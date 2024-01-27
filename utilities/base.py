import inspect

import pytest
import logging


@pytest.mark.usefixtures("setup")
class Base:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("fileLog.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s logs: %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
