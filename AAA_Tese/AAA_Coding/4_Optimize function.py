import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize



def CAL(ret1,ret2,var1,var2,cov):
    def portVar(x):
        return (1-x/100)**2*var1+(x/100)**2*var2+2*(1-x/100)*(x/100)*cov
    returns = [(1-x/100)*ret1+(x/100)*ret2 for x in range(0,101)]
    variances = [portVar(x) for x in range(0,101)]
    standardDevs = [x**.5 for x in variances]
    allocations = [(1-x/100) for x in range(0,101)]

    con1 = {'type': 'ineq',
       'fun': lambda x: -(x-1)}
    con2 = {'type': 'ineq',
       'fun': lambda x: x}

    minVarX = scipy.optimize.minimize(portVar,0,constraints=[con1,con2])["x"][0]
    print('MinVar\n', minVarX)
    minVarSD = portVar(minVarX)**.5
    minVarReturn = (1-minVarX/100)*ret1+(minVarX/100)*ret2
    
    plt.plot(allocations,returns)
    plt.xlabel("Amount in Asset 1")
    plt.ylabel("Return")
    plt.title("Capital Allocation Line ")
    plt.plot(1-minVarX/100,minVarReturn,"ro")
    #plt.show()


    plt.plot(allocations,standardDevs)
    plt.xlabel("Amount in Asset 1")
    plt.ylabel("Standard Deviation")
    plt.title("Capital Allocation Line ")
    plt.plot(1-minVarX/100,minVarSD,"ro")
    #plt.show()

CAL(.03,.09,.55,.45,-.1)