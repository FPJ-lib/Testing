# https://www.supplychaindataanalytics.com/monte-carlo-simulation-of-stock-prices-using-python/

print('\n\n')

# declare list with fictional daily stock closing prices
history_prices = [180,192,193,195,191,199,198,200,199,203,205,207,205,208,201,203,204,201,205,206,207]
print(history_prices)


# import statistics for calculating e.g. standard deviation of price history
import statistics as stat
# import pyplot for plotting
import matplotlib.pyplot as plt
# import random for random number generations
import random as rnd



relative_prices = []
for i in range(0,len(history_prices)):
    if i == 0:
        pass
    else:
        relative_prices.append((history_prices[i]-history_prices[i-1])/(history_prices[i-1])) 

print()
print(relative_prices)

std_prices = stat.stdev(relative_prices)
print('\nStd Dev:\t', round(std_prices*100,2))




# modeling a random price walk over 100 days
# -- conduct calculation, define function
def randomWalk(stdev,pastPrices):
    days = [i for i in range(1,101)]
    prices = []
    price = pastPrices[-1]
    for i in range(1,101):
        price = price + price*rnd.normalvariate(0,stdev)
        prices.append(price)
    return([days,prices])
# -- conduct calculation, use function
prices = randomWalk(std_prices,history_prices)
print('\nPrice:\n', prices)


# -- visualize random walk in a line plot
plt.plot(prices[0],prices[1])
plt.title("random price walk")
plt.xlabel("day")
plt.ylabel("stock price")
#plt.show()



plt.figure()
for i in range(0,30):
    prices = randomWalk(std_prices,history_prices)
    plt.plot(prices[0],prices[1])
plt.title("monte-carlo simulation of stock price development")
plt.xlabel("day")
plt.ylabel("stock price")
#plt.show()




print('\n\n')