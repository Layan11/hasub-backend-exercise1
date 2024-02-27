import logging


def only_msg():
    logging.basicConfig(filename='only_msg.log', format='%(message)s', level=logging.INFO)
    logging.info('This is a log with only a message with no timestamp.')


def msg_with_timestamp():
    logging.basicConfig(filename='msg_with_timestamp.log', format='%(asctime)s %(message)s', level=logging.INFO)
    logging.info('This is a log with a message and a timestamp.')


def msg_timestamp_level():
    logging.basicConfig(filename='msg_with_timestamp_and_level.log', format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.WARNING)
    logging.warning('This is a log with a message and a timestamp and a log level (warning).')


def multi_log(log_fn):
    log_fn()


if __name__ == '__main__':
    multi_log(only_msg)
    multi_log(msg_with_timestamp)
    multi_log(msg_timestamp_level)
