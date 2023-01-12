import matplotlib.pyplot as plt
from scipy.stats import norm

commonStatTime = 5000  # time to collect statistics
statPeriod = 1  # statistics step
statSize = int(commonStatTime / statPeriod)  # number of stat steps

# duplication options
duplicationMean = 75
duplicationDisp = duplicationMean * 0.27
duplicationMinTime = 5

duplicationDensity = [0 for a in range(duplicationMinTime)]
icd = duplicationMinTime

prevSum = 0
cds = 0
# calculating distribution density per minute until it reaches 99%
while cds < 0.99:
    cds = norm.cdf(icd, duplicationMean, duplicationDisp)
    duplicationDensity.append(cds - prevSum)
    prevSum = cds
    icd += 1

# array to collect statistics
population = [0 for a in range(statSize)]
population[0] = 1

arrLength = icd * 2
newbornCells = [0 for a in range(arrLength)]
newbornCells[0] = 1
curTime = 0
curIndex = 0
# calculation of newborn cells per minute in a cyclic array
while curTime < commonStatTime:
    for i in range(duplicationMinTime, icd):
        newCells = newbornCells[curIndex]
        newbornCells[(i + curIndex) % arrLength] += newCells * duplicationDensity[i] * 2
    population[int(curTime / statPeriod)] += newCells / 2
    # clear the cell because it will be reused later
    newbornCells[curIndex] = 0
    curIndex = (curIndex + 1) % arrLength
    curTime += 1

# count population cumulative
for i in range(1, statSize):
    population[i] += population[i - 1]

plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(population)
plt.show()

print('Processed ', commonStatTime, ' minutes')
print('Final number of cells: ', population[statSize - 1])
