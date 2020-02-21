'''
This Dori Dong's Sokara self-rated Soraka performance indicatorself.
Data is taken from the past 10 games I played using the Champion Soraka in the game League of Ledgends.
Each pluged-in data is hand calculated using the history found in my game history
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    # KA = kill and assist grade after calculation
    #D = death
    plt.xlabel('K&A')
    plt.ylabel('D')

    #function to show plotting
    plt.show()

def main():
    #observations
    #x= death
    #y= 1(kill)+0.5(assist kill)
    x = np.array([2, 2, 11, 8, 8, 15, 11, 1, 6, 4])
    y = np.array([6.5, 11, 10.5, 27, 19, 21.5, 2, 6.5, 2, 5.5])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
