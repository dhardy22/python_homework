import logging 
logger = logging.getLogger(__name__ + "_parameter_log") # Names the logger with the module name and a suffix
logger.setLevel(logging.INFO) # Similar to a gateway, it filters out messages below the INFO level
logger.addHandler(logging.FileHandler("./decorator.log", "a")) # Writes log messages to a file named "decorator.log" in append mode

#Task 1
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}, args: {args}, kwargrs: {kwargs}, return: {result}")
        return result
    return wrapper


