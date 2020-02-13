import time
import numpy as np

def analyse_data(data):
    """This is just a dummy function to represent something that is 
    slow and CPU intensive"""
    c = np.corrcoef(data[:, 0], data[:, 1])[0,1]
    time.sleep(0.1)
    return c

if __name__=='__main__':
    data = np.random.normal(0,1,(10,10))
    print(analyse_data(data))