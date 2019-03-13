import logging
import functools

class Logger:

    def create_logger(self):
        logger = logging.getLogger("example_logger")
        logger.setLevel(logging.INFO)
    
        # create the logging file handler
        fh = logging.FileHandler("/data/test.log")
    
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
    
        # add handler to logger object
        logger.addHandler(fh)
        return logger
    
    def exception(self, function):

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            logger = self.create_logger()
            try:
                return function(*args, **kwargs)
            except:
                
                err = "There was an exception in  "
                err += function.__name__
                logger.exception(err)
    
                raise
        return wrapper
