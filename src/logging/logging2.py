import logging
log = logging.getLogger("Logging2")
log.setLevel(logging.DEBUG)

def doIt():
        log.debug("Doing stuff...")
        #do stuff...
        raise TypeError("Bogus type error for testing")

if __name__ == '__main__':
        doIt()