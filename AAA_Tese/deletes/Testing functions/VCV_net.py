
#Easier with COV() Function initially

import numpy as np
import math

stdv = {"ABC":0.3,"XYZ":0.2}

tickersCorr = ["ABC","XYZ"]

# Assuming a 0.5 correlation here is the correlation matrix
c = [[1,0.5],[0.5,1]]

def varCovarMatrix(stocksInPortfolio):
    cm = np.array(c)
    vcv = []
    for eachStock in stocksInPortfolio:
        row = []
        for ticker in stocksInPortfolio:
            if eachStock == ticker:
                variance = math.pow(stdv[ticker],2)
                row.append(variance)
            else:
                cov = stdv[ticker]*stdv[eachStock]* cm[tickersCorr.index(ticker)][tickersCorr.index(eachStock)]
                row.append(cov)
        vcv.append(row)

    vcvmat = np.mat(vcv)

    return vcvmat


print(varCovarMatrix(["ABC","XYZ"]))