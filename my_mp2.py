import multiprocessing
import random
from time import sleep
from datetime import datetime

def mi_proceso(tiempo, proceso):
    sleep(tiempo)
    fechaActual = datetime.now()
    print("Soy el proceso:", proceso, "con un tiempo de:", tiempo, "segundos. Mi fecha es:", fechaActual)

if __name__ == "__main__":
    
    for n in range(1, 4):
        segundos = random.randrange(1, 6)
        proceso = multiprocessing.Process(target=mi_proceso, args=(segundos, n))
        proceso.start()
        #sleep(segundos) Sleep se ejecuta secuencialmente aqui
        #proceso.terminate()

"""Si los procesos se ejecutan secuencialmente, nunca se verá el multiprocesamiento y será
como un loop FOR normal. Deben ejecutarse en simultáneo para que se vea que un proceso posterior
puede terminar primero que otro si su tiempo de ejecución es menor"""