# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('score')
logger.setLevel(logging.INFO)
logging.basicConfig(filename='results.log', filemode='w')
print ("logging start")
def logit (algo, accuracy, columns):
    text = "{algo}, {accu}".format(algo=algo, accu=accuracy)
    print (text)
    logger.info("{algo}, {accu}, {columns}".format(algo=algo, accu=accuracy, columns=columns))
    return

def flush():
    logging.shutdown()

    