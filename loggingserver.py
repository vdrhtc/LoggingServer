import os
from multiprocessing import Queue
from threading import Thread

import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler


class LoggingServer:

    INSTANCE = None
    logger = logging.getLogger('overseer')

    @staticmethod
    def getInstance(test = False):
        if LoggingServer.INSTANCE is None:
            try:
                os.mkdir("log")
            except FileExistsError:
                pass
            finally:
                file_name = 'log/overseer.log' if not test else 'log/overseer_test.log'
                logging_handler = TimedRotatingFileHandler(
                    file_name, when="midnight", backupCount=1)

            if not test:
                logging_format = '%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s'
            else:
                logging_format = 'TESTING %(asctime)s.%(msecs)03d [%(levelname)s] %(message)s'

            logging_formatter = Formatter(fmt=logging_format, datefmt='%I:%M:%S')
            logging_handler.setFormatter(logging_formatter)

            LoggingServer.logger.setLevel("DEBUG")
            LoggingServer.logger.addHandler(logging_handler)

            LoggingServer.INSTANCE = LoggingServer()
            return LoggingServer.INSTANCE
        else:
            return LoggingServer.INSTANCE

    def __init__(self):
        self._messageQueue = Queue()
        t = Thread(target=self.run)
        t.setDaemon(True)
        t.start()

    def debug(self, *args):
        self._messageQueue.put(("debug", args))

    def warn(self, *args):
        self._messageQueue.put(("warn", args))

    def info(self, *args):
        self._messageQueue.put(("info", args))

    def run(self):
        while True:
            msg = self._messageQueue.get()
            if msg[0] == "debug":
                self.logger.debug(*msg[1])
            elif msg[0] == "warn":
                self.logger.warning(*msg[1])
            elif msg[0] == "info":
                self.logger.info(*msg[1])
