import yaml

# ---------------------------------------------------
# Properties
# ---------------------------------------------------
configFile = False

# ---------------------------------------------------
# Methods
# ---------------------------------------------------
def init():
    global configFile
    configFile = yaml.load(open('config.yaml'), Loader=yaml.SafeLoader)

def get(key):
    global configFile
    return configFile.get(key)