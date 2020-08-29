#function histogram to take in integer inputs and outputing * corresponding to number of inputs
def histogram(items):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

#format of histogram        
histogram([5, 6, 8, 3])
