import pandas as pd 
import numpy as numpy

import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.8f}'.format

#Optimization
from scipy.optimize import minimize


print('\n')
''' 
########################################
############# INPUTS ###################
########################################
'''
# To compute the 1st Covariance
drop_first_observations = 70

# For daily, EWMA formula
lambda_k = 0.94


#OPTIMIZATION:
TOLERANCE = 1e-10


#----------------------------------------

''' Got data from Yahoo-Finance '''
#DATES
start_date = '2012-12-31'
end_date = '2021-01-15'


#Tickers
list_tickers = ['^GSPC','GOVT', 'EEM','GLD'] #Added GOLD
name_columns = ['SP', 'Bond','EM', 'Gold']


#FROM 001_continuous.py
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_001.csv')
df = df.set_index('Date')


'''
#####################################
############# FUNCTIONS #############
#####################################
'''

def square(list):
    return [i ** 2 for i in list]

#EWMA:
ewma = []
def compute_ewma(list_returns,column):
    ewma = []
    returns_squared = square(list_returns)

    for row in range(len(list_returns)): # SHOULD BE HERE A +1
        #print(list_returns[row], '\t\t', returns_squared[row])

        if row == 0:
            value_append = df_returns_lost_observations[column][-1] ** 2
            ewma.append(value_append)
        else:
            decay = lambda_k * ewma[-1] 
            added = (1-lambda_k) * (returns_squared[row-1])
            ewma.append(decay + added)
    return ewma 


def compute_cov(list_returns_row, list_returns_col):
    covariance_list = []


    #Check Values
    #print('%.5f' % initial_cov)
    #print(df_returns_lost_observations.cov())

    for row in range(len(list_returns_row)): # SHOULD BE HERE A +1

        if row == 0:
            #1st Estimate:
            initial_cov = df_returns_lost_observations[ticker_row].cov(df_returns_lost_observations[ticker_col])
            covariance_list.append(initial_cov)

        else:
            decay = lambda_k * covariance_list[-1] 
            added = (1-lambda_k) * list_returns_row[row-1] * list_returns_col[row-1]
            covariance_list.append(decay + added)
    
    return covariance_list


def compute_correlation(covariance_list, ewma_row_list, ewma_col_list):
    correlation=[]
    #denominator = std_row_list * std_col_list

    #std_row_list = ewma_row_list ** 0.5
    #std_col_list = ewma_col_list ** 0.5

    #correlation = covariance_list / ((std_row_list) * (std_col_list))

    for row in range(len(covariance_list)):
        value_append = covariance_list[row] / ((ewma_row_list[row]**0.5)*(ewma_col_list[row]**0.5))
        correlation.append(value_append)
    

    return correlation



'''
#######################################################################################
RISK - PARITY FUNCTIONS:
*   Compute risk-parity weights daily
#######################################################################################
'''
#______________________________________________________________________________________
#FIRST: Get the Covariance Matrix:

def build_matrix(date='2021-01-07'):
    
    ewma = df_ewma.loc[date]
    covariance = df_covariances.loc[date]

    #Check inputs
    #print('\nEWMA:\n', ewma)
    #print('\nCovariance:\n', covariance) 

    matrix_list =[]

    for num_row in range(len(name_columns)):
        #Clean next matrix row:
        list_row = []

        #Get the row name:
        ticker_row = name_columns[num_row]

        for num_col in range(len(name_columns)):
        
            #print('\n(ROW,COL):\t (%.0f,%.0f)' % (num_row, num_col)) #Check the numbers in the matrix


            #Get The Column Names
            ticker_col = name_columns[num_col]

            if num_row == num_col:
                #EWMA:
                list_row.append(ewma[ticker_row])

            elif num_row < num_col :
                #Get Covariance:
                cov_name_column = ticker_row + '_' + ticker_col

                list_row.append(covariance[cov_name_column])

            else:
                #Covariance already computed. Get from matrix by switching columns & row numbers:
                list_row.append(matrix_list[num_col][num_row])

        #Append new_ROW to Matrix
        matrix_list.append(list_row)
    
    VCV = np.matrix(matrix_list)
    #print('\n\nMATRIX\n', VCV) #Check Values

    return VCV
        








#______________________________________________________________________________________




''' 
############################################
############# DATA PREPARATION #############
############################################
'''

df_returns = df.pct_change().dropna() #CHANGE TO df_ret

'''
#Check Data ----------
print('Data:\n', df)
print('\nReturns:\n', df_returns*100)
#---------------------
'''



''' Divide the Data '''
#For First EWMA Estimations:
df_returns_lost_observations = df_returns[:drop_first_observations]

#Active Data:
df_returns_new = df_returns[drop_first_observations:]


'''
#Printing --------------
print('\nDropped:\n', df_returns_lost_observations)
print('Dropped Size: \t', df_returns_lost_observations.shape)
print('\nActive Data:\n', df_returns_new)
#-----------------------
'''


'''
############# COMPUTE EWMA + Covariances #############
'''



df_ewma = pd.DataFrame()
#Compute ALL EWMA Volatilities:
for column in name_columns:
    df_ewma[column] = compute_ewma(df_returns_new[column].values, column)

# Tranform them to annual:
#df_ewma = (df_ewma *252) ** 0.5  

#Get the Index. 
'''
df_ewma['Date'] = df_returns_new.index
df_ewma.index = df_ewma['Date']
df_ewma.drop(['Date'], axis=1, inplace=True)
'''
df_ewma.index = df_returns_new.index


#EWMA VALUES
print('EWMA:\n',df_ewma.head(2))


#df_ewma.plot()
#plt.show()


''' COMPUTE COVARIANCES '''

df_covariances = pd.DataFrame()
df_correl = pd.DataFrame()

#print('COVARIANCE for now on...')


#Compute all the covariances in the matrix
for num_row in range(len(name_columns)):
    for num_col in range(num_row+1,len(name_columns)):

        '''Check the Numbers for the matrix'''
        #print('\n#row:\t', num_row)
        #print('#col:\t', num_col)


        #Get The Columns Names
        ticker_row = name_columns[num_row]
        ticker_col = name_columns[num_col]

        #Name of the column in the table ---> does this order matter ? 
        cov_name_column = ticker_row + '_' + ticker_col
        

        #Get Returns to list -----> All about 'Rows' Could be in the superior For
        returns_row = df_returns_new[ticker_row].values
        returns_col = df_returns_new[ticker_col].values

        #Call the function, compute Covariance
        df_covariances[cov_name_column] = compute_cov(returns_row, returns_col)




        df_correl[cov_name_column] = compute_correlation(df_covariances[cov_name_column].values , df_ewma[ticker_row].values, df_ewma[ticker_col].values )
        #df_covariances[cov_name_column]/ ( (df_ewma[ticker_row]**0.5) * (df_ewma[ticker_col]**0.5) )
        


#Index the same as EWMA:
df_covariances.index = df_returns_new.index
df_correl.index = df_returns_new.index


#print('\nCovariances:\n ',df_covariances)
print('\nCorrelations:\n ',df_correl.head(2))

#CHECK - MAX and Mins:
#print('\n\nCorrelation, described (get the MAximuns & minimuns:\n', df_correl.describe())

#PLOT Correlations.
#df_correl.plot()
#plt.show()

'''
################################################################################################
################################################################################################
################################################################################################
USELESS

'''



'''
#############################################################
                    Correlation Stats
#############################################################
'''
df_stats_correlation = pd.DataFrame()
df_stats_correlation['prod_correlation'] = (df_correl**2).sum(axis=1)

#Make it all more volatile:
#df_stats_correlation['prod_correlation'] = 1/ (2**(5*df_stats_correlation['prod_correlation']) )

print('\nTesting some ideas\n',df_stats_correlation.head(2))
print(df_stats_correlation)


'''
CORRELATION GRAPH
'''
df_stats_correlation.plot(title = 'Sum squared Correlations (EWMA method)', legend='corr')

#plt.show()
print('\n\n\n')
'''
_____________________________________________________________________________________________________
'''



'''
RISK Parity Portfolio:
'''
multiply = 0.5

weights_risk_parity = [
                        0.15819 * multiply,
                        0.639923 * multiply,
                        0.084359 * multiply,
                        0.117529 * multiply
                    ] 



import numpy as np

risk_parity_portfolio = pd.DataFrame()
#risk_parity_portfolio = df_returns_new 
#* np.matrix(weights_risk_parity)

risk_parity_portfolio['RP'] = np.dot(df_returns_new, weights_risk_parity)
risk_parity_portfolio.index = df_returns_new.index

#STATS
cumulative = risk_parity_portfolio['RP'].sum() * 100
volatility = risk_parity_portfolio['RP'].std() *100
IS = round(cumulative/volatility /100, 4)

print('\nRisk-Parity Portfolio:\n', risk_parity_portfolio.head(2))
print('\nSum-Returns:\n', cumulative)
print('Volatility\n', volatility)
print('IS\n', IS)

'''
GRAPH CUMULATIVE RETURNS:
'''
((risk_parity_portfolio['RP']+1).cumprod()-1).plot(legend='risk_parity_cumulative')
#plt.show()

multiply = 0.25

w = [
                        0.25 * multiply,
                        0.25 * multiply,
                        0.25 * multiply,
                        0.25 * multiply
                    ] 

import numpy as np

risk_parity_portfolio = pd.DataFrame()
#risk_parity_portfolio = df_returns_new 
#* np.matrix(weights_risk_parity)

risk_parity_portfolio['EW'] = np.dot(df_returns_new, w)
risk_parity_portfolio.index = df_returns_new.index

#STATS
cumulative = risk_parity_portfolio['EW'].sum() * 100
volatility = risk_parity_portfolio['EW'].std() * 100
IS = round(cumulative/volatility /100, 4)

print('\nEqual Weight - returns:\n', risk_parity_portfolio.head(2))
print('\nSum-Returns:\n', cumulative)
print('Volatility\n', volatility)
print('IS\n', IS)


((risk_parity_portfolio['EW']+1).cumprod()-1).plot(legend='EW_cumulative')
#plt.show()


'''
USELESS:
################################################################################################
################################################################################################
################################################################################################
'''


'''
###
++++++++++++++++++++++++++++++
Compute Risk Parity on demand
++++++++++++++++++++++++++++++
###
'''



date_test ='2020-12-07'


def _allocation_risk(weights, VCV):

    # We calculate the risk of the weights distribution
    portfolio_risk = np.sqrt((weights * VCV * weights.T))[0, 0]
    #print('\nPortfolio Risk ( weights, Covvariances):\n', portfolio_risk)

    # It returns the risk of the weights distribution
    return portfolio_risk


def _assets_risk_contribution_to_allocation_risk(weights, VCV):

    # We calculate the risk of the weights distribution
    portfolio_risk = _allocation_risk(weights, VCV)

    # We calculate the contribution of each asset to the risk of the weights
    # distribution
    assets_risk_contribution = np.multiply(weights.T, VCV * weights.T) / portfolio_risk
    #print('\nAssets_risk_contribution (MCR):\n', assets_risk_contribution)

    # It returns the contribution of each asset to the risk of the weights
    # distribution
    return assets_risk_contribution


def _risk_budget_objective_error(weights, args):

    # The covariance matrix occupies the first position in the variable
    VCV = args[0]

    # The desired contribution of each asset to the portfolio risk occupies the
    # second position
    target_mcr = args[1]

    # We convert the weights to a matrix
    weights = np.matrix(weights)

    # We calculate the risk of the weights distribution
    portfolio_risk = _allocation_risk(weights, VCV)

    # We calculate the contribution of each asset to the risk of the weights
    # distribution
    assets_risk_contribution = _assets_risk_contribution_to_allocation_risk(weights, VCV)

    # We calculate the desired contribution of each asset to the risk of the
    # weights distribution
    assets_risk_target = np.asmatrix(np.multiply(portfolio_risk, target_mcr))


    # Error between the desired contribution and the calculated contribution of
    # each asset
    error = sum(np.square( (assets_risk_contribution - assets_risk_target.T) ))[0, 0]

    # It returns the calculated error
    return error


def _get_risk_parity_weights(VCV, target_mcr, initial_weights):

    # Restrictions to consider in the optimisation: only long positions whose
    # sum equals 100%
    constraints = (
                    {'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0},
                    #{'type': 'ineq', 'fun': lambda x: x}
                   )

    # Optimisation process in scipy
    optimize_result = minimize(fun=_risk_budget_objective_error,
    x0=initial_weights,
    args=[VCV, target_mcr],
    method='SLSQP',
    constraints=constraints,
    tol=TOLERANCE,
    options={'disp': False})

    # Recover the weights from the optimised object
    weights = optimize_result.x
    #print(optimize_result)

    # It returns the optimised weights
    return weights


def get_weights(date = date_test):

    print('\nFUNCTION_____:')    
    
    VCV = build_matrix( date=date_test)
    print('VCV:\n', VCV)
    
    print('\n###########COVARIANCES#############\n', VCV)

    # The desired contribution of each asset to the portfolio risk: we want all
    # asset to contribute equally
    target_mcr = [1 / df_ewma.shape[1]] * df_ewma.shape[1]

    print('\nASSET RISK - budget\n', target_mcr)

    # Initial weights: equally weighted
    initial_weights = [1 / df_ewma.shape[1]] * df_ewma.shape[1] # Build a matrix
    print('\ninitial weights:\n', initial_weights)

    # Optimisation process of weights
    weights = _get_risk_parity_weights(VCV, target_mcr, initial_weights)

    # Convert the weights to a pandas Series
    weights = pd.Series(weights, index=df_ewma.columns, name='weight')

    # It returns the optimised weights
    return weights


#GET_RISK-Parity Portfolio:

weights = get_weights(date = date_test)
print('Weights:\n', weights)



df_conditional_returns = pd.DataFrame()
df_conditional_returns = df_returns_new

print(df_conditional_returns)

#TEST THE RETURNS:
df_conditional_returns = df_conditional_returns * weights

df_conditional_returns['Product_Cov > 0.01'] = df_stats_correlation['prod_correlation']
df_conditional_returns['Product_Cov > 0.01'] = df_conditional_returns['Product_Cov > 0.01'] > 0.02




print(df_conditional_returns)
print('COUNT VALUES HIGHER THAN:\n', df_conditional_returns['Product_Cov > 0.01'].sum())












print('\n\n')