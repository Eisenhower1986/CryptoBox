import logging

def setup_logger(log_file='app.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

# Example usage
if __name__ == '__main__':
    setup_logger()
    log_info("This is an info message")
    log_error("This is an error message")
