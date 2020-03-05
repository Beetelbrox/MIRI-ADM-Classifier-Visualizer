# The class that contains all the values that can be modified in the GUI
class Config:

    def __init__(self, options):
        for o in options:
            self.__dict__[o] = [x.strip() for x in options[o].split(',')] if ',' in options[o] else options[o].strip()



def read_config(path):
    with open(path, mode='r', encoding='utf-8') as f:
        options = dict([line.rstrip().split(':') for line in f if line[0] != '#'])
    return Config(options)
