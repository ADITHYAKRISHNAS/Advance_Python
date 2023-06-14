import logging
import other_module

# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(filename='my_logs.log', encoding='utf-8', filemode='w',
#                     level=logging.DEBUG)

# logging.debug("DEBUG")
# logging.info("INFO")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")

# logging.basicConfig(level=logging.DEBUG)

# x: int = 10 + 10

# logging.info("The answer is %s", x )
# logging.info(f"The answer is {x}" )

logging.basicConfig(format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG)

# logging.critical('OK')


logging.info("Hello, my name is slime shady!")


logging.warning("Oh no! You caught me!")


other_module.func()