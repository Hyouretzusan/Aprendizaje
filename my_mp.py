import multiprocessing
import random
from time import sleep
from datetime import datetime

def now(seconds):

    sleep(seconds)
    print('Tiempo de espera', seconds, 'segundos. Fecha actual:', datetime.utcnow())

if __name__ == '__main__':

    for n in range(3):
        seconds = random.randrange(5)
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()