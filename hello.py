from numba import njit
from numba.openmp import openmp_context as openmp
from numba.openmp import omp_get_num_threads, omp_get_num_devices, omp_get_thread_num, omp_get_team_num, omp_get_num_teams
import numpy as np
@njit()
def test():
    with openmp("parallel"):
        print("Hello from thread", omp_get_thread_num(), "/", omp_get_num_threads())
      
test()

print("DONE")
