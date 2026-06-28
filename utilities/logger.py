import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        log_folder = "logs"
        os.makedirs(log_folder, exist_ok=True)

        logger = logging.getLogger("AutomationFramework")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(
                "logs/automation.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger