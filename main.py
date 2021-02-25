from multiprocessing import Process
import os
import time

from processor import processor
engine = processor()

# call for multiprocessing, could probably be done better
def callProcessor(throughput): # intent & args
    engine.processAction(throughput[0], args = throughput[1])

# good ol' python2 
if __name__ == '__main__':
    # run input loop for ever
    while True:
        # proper input to added later
        x = input('x :   ')
        # seperate sys command function hardwired
        if x == 'stop':
            try:
                p.terminate()
                x = input('x :  ')
            except:
                x = input('x :  ')
        arg = input('arg : ')
        l = [x, arg]

        # run with input as args processor function
        if len(x) != 0:
            try:
                p.terminate()
            except:
                print()

            p = Process(target=callProcessor, args=(l,))
            p.start()
            print(p)
            print(os.getpid())
            time.sleep(1)
        
        else:
            pass
    p.join() # cleanup I guess
        
    

        
                