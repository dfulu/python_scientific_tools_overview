import time
import numpy as np
import numba as nb

def analyse_data(data):
    """This is just a dummy function to represent something that is 
    slow and CPU intensive"""
    c = np.corrcoef(data[:, 0], data[:, 1])[0,1]
    time.sleep(0.1)
    return c

def lorenz(x, y, z, nsteps, dt, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       Series of coords for lorenz attractor
    '''
    coords = np.zeros((nsteps,3))
    coords[0] = x, y, z
    for i in range(1, nsteps): 
        x += s*(y - x)*dt
        y += (r*x - y - x*z)*dt
        z += (x*y - b*z)*dt
        coords[i] = x, y, z
    return coords

def run_lorenz(start_position):
    x, y, z = start_position
    return lorenz(x, y, z, nsteps=10000, dt=0.01)


if __name__=='__main__':
    data = np.random.normal(0,1,(10,10))
    print(analyse_data(data))
    
    sim = run_lorenz((1,1.05,0))
    print(sim)