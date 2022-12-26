import random
import matplotlib.pyplot as plt

commonStatTime = 500  # time to collect statistics
statPeriod = 1  # statistics step
statSize = int(commonStatTime / statPeriod)  # number of stat steps

# duplication options
duplicationMean = 75
duplicationDispersion = duplicationMean * 0.27
duplicationMinTime = 5  # min time chosen randomly > 0


# duplication time random generation (Gauss)
# more distribution modelling in py: https://docs.python.org/3/library/random.html#random.betavariate
def genDuplicationTime():
  duplication = random.normalvariate(duplicationMean, duplicationDispersion)
  return max(duplication, duplicationMinTime)


# array to collect statistics
population = [0 for a in range(statSize)]

# array with time of cell creation
duplProc = []
duplProc.append(0)
# array with number of created cells on each step(later summarized to all cells created to each step)
population[0] = 1
i = 0
while (i < len(duplProc)):
  currentTime = duplProc[i]
  duplNext = currentTime + genDuplicationTime()
  if duplNext < commonStatTime:
    duplProc.append(duplNext)
    duplProc.append(duplNext)
    statInd = int(duplNext / statPeriod)
    if statInd < statSize:
      population[statInd] += 1
  i += 1
for i in range(1, statSize):
  population[i] += population[i - 1]

plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(population)
plt.show()
