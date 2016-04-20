import math
import numpy as np
 
values = range(1, 100)
probs = [1.0 / 99] * 99
 
for x, prob in enumerate(probs):
    # if x > 3 and x < 20:
    #     probs[x] = probs[x] * (1 + math.log(x + 1))
    # if x > 20 and x < 40:
    #     probs[x] = probs[x] * (1 + math.log((40 - x) + 1))
    if x > 80 and x < 96:
    	probs[x] = probs[x] * (1 + math.log((96 - x) + 1))
 
probs = [p / sum(probs) for p in probs]
sample =  np.random.choice(values, 5000, p=probs)
# rounded = round(sample,2)
# TypeError: type numpy.ndarray doesn't define __round__ method
print (sample[:10])

np.savetxt("output.csv", sample, fmt="%1.3f", delimiter=",")
# import csv

# def csv_writer(sample, path):
# 	with open(path, "w", newline='') as csv_file:
# 		writer = csv.writer(csv_file, delimiter=',')
# 		for values in sample:
# 			writer.writerow(values)
# path = "output.csv"
# csv_writer(sample, path)

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
 
# binwidth = 2
# plt.hist(sample, bins=np.arange(min(sample), max(sample) + binwidth, binwidth))
# plt.xlim([0, max(sample)])
# plt.show()
# http://www.markhneedham.com/blog/2015/03/30/python-creating-a-skewed-random-discrete-distribution/
# http://stackoverflow.com/questions/24854965/create-random-numbers-with-left-skewed-probability-distribution
# http://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.random.choice.html
# http://stackoverflow.com/questions/17043393/setting-the-fmt-option-in-numpy-savetxt