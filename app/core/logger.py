import logging


def setup_logging():
    """
    Configures the logging system for the application.

    This function sets the basic settings for logging, including the severity level,
    the message format and the date and time format. The settings defined here apply
    to all logs created in the application.

    The logging level is set to INFO, which means that all events of this and higher levels (WAR) will be logged.
    this level and higher levels (WARNING, ERROR, CRITICAL) will be logged.

    Log message format:
    - Date and time of the event.
    - Name of the logger that generated the log
    - Severity level of the event
    - Log message
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


logger = logging.getLogger(__name__)
