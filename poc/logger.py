# -*- coding: utf-8 -*-
import logging
logging.basicConfig(filename='results.log', filemode='w')
def logit (algo, accuracy):
    text = "{algo}, {accu}".format(algo=algo, accu=accuracy)
    print (text)
    logging.info("{algo}, {accu}".format(algo=algo, accu=accuracy))
    return

def flush():
    logging.shutdown()

    