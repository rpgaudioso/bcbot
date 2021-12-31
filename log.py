import logging

# ---------------------------------------------------
# Properties
# ---------------------------------------------------

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def init():
    logging.basicConfig(filename='actions.log', 
                        filemode='a',
                        encoding='utf-8', 
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        format='%(asctime)s %(name)s [%(levelname)s] - %(message)s',
                        level=logging.DEBUG)

    # logger = logging.getLogger('actions')
 