import logging
log_format = '%(asctime)s %(levelname)s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.DEBUG, format=log_format)
logger = logging.getLogger('WANG')

from circle1 import circle_area

def area(r):
    try:
        area = circle_area(r)
        logger.info(f"the area with radius {r} is {area}.")
    except Exception as err:
        logger.error(f"Error: {err}")

area(1)
area(-2)
area(3+4j)
area("hello")
area(3.4)
area(None)

print("Done.")