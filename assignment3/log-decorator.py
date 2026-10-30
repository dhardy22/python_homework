#Task1

import logging 
logger = logging.getLogger(__name__ + "_parameter_log") # Names the logger with the module name and a suffix
logger.setLevel(logging.INFO) # Similar to a gateway, it filters out messages below the INFO level
logger.addHandler(logging.FileHandler("./decorator.log", "a")) # Writes log messages to a file named "decorator.log" in append mode

#Task 1
def logger_decorator(func):
    def wrapper(*args, **kwargs,):
        result = func(*args, **kwargs)
        posit_para = args if args else "none"
        key_para = kwargs if kwargs else "none"
        logger.info(f"function: {func.__name__}, positional parameters: {posit_para}, keyword parameters: {key_para}, return: {result}")
        return result
    return wrapper

@logger_decorator
def greeting():
    print("Hello World!") 

@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def check_kwargs(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    greeting()
    check_args("first argument", "second argument", "third argument")
    check_kwargs(name="Don")