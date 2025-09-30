from matplotlib import pyplot
import numpy


def linear(x, y, lr=0.001): # a simple linear regression model

    # initialize weights, biases and steps
    w, b = 0, 0
    db, dw = 0, 0
    error = numpy.mean((y - (w * x + b)) ** 2) # mean squared error
    
    while error > 0.0001: # arbitrary threshold; tweak to personal satisfaction
    
        # calculate steps
        dw += (-2) * numpy.mean(x * (y - (w * x + b))) 
        db += (-2) * numpy.mean(y - (w * x + b))
        
        # adjust weights and biases
        w = w - lr * dw
        b = b - lr * db
        
        # re-evaluate error
        error = numpy.mean((y - (w * x + b))**2)
        
    return float(w), float(b)


def main():

    x = numpy.array([1, 2, 3])
    y = numpy.array([2, 4, 6])
    print(linear(x, y))


if __name__ == '__main__':

    main()




