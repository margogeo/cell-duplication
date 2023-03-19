import random
import math
import matplotlib.pyplot as plt
from scipy.stats import expon

# statistics collection parameters
commonStatTime = 20  # time to collect statistics
statPeriod = 1  # statistics step
statSize = int(commonStatTime / statPeriod)  # number of stat steps
iStat = 0  # current index in stat array

# process parameters
betaM = 20  # RNA transcription
gammaM = 2  # RNA dilution
betaP = 8  # protein translation
gammaP = 4  # protein dilution

# initial amount of RNA and protein
mRna = 10
mProtein = 20

currentTime = 0
transitionTime = 1  # Initial value, not used

# arrays to collect statistics - average
RnaPopulation = [0 for a in range(statSize)]
ProtPopulation = [0 for a in range(statSize)]

# arrays to collect statistics - per trajectory
RnaTrajStat = []
ProtTrajStat = []

plt.xlabel("Time")
plt.ylabel("RNA")


def initTrajectory():
    global mRna, mProtein, currentTime, iStat, RnaTrajStat, ProtTrajStat
    mRna = 10
    mProtein = 20
    currentTime = 0
    iStat = 0
    RnaTrajStat = [0 for _ in range(statSize)]
    ProtTrajStat = [0 for _ in range(statSize)]


# calculate propensities, transition time, data change type
# return 1 when time limit exceeds
def calcStep():
    global mRna, mProtein, currentTime, iStat, RnaTrajStat, ProtTrajStat, transitionTime
    pRnaTransition = betaM
    pRnaDilution = gammaM * mRna
    pProtTranslation = betaP * mRna
    pProtDilution = gammaP * mProtein
    p2 = pRnaTransition + pRnaDilution
    p3 = p2 + pProtTranslation
    pSum = p3 + pProtDilution  # 4 propensities sum
    transitionTime = expon.rvs(scale=1.0 / pSum)  # random time
    pRand = random.random() * pSum  # calculate random change direction
    if pRand < p2:
        if pRand < pRnaTransition:
            mRna += 1
        else:
            mRna -= 1
    else:
        if pRand > p3:
            mProtein -= 1
        else:
            mProtein += 1
    currentTime += transitionTime
    tStat = math.floor(currentTime / statPeriod)
    if tStat >= statSize:
        return 1
    if tStat > iStat:
        iStat = tStat
        RnaTrajStat[iStat] = mRna
        ProtTrajStat[iStat] = mProtein
    return 0


nTrajectories = 30

print("Trajectory: ", end='')
for i in range(nTrajectories):
    initTrajectory()
    while calcStep() == 0:
        continue
    for j in range(statSize):
        RnaPopulation[j] += RnaTrajStat[j]
        ProtPopulation[j] += ProtTrajStat[j]
        if i % 5 == 0:
            plt.plot(RnaTrajStat, color='#08f', linewidth=0.3)
    print((i + 1), " ", end='')

for j in range(statSize):
    RnaPopulation[j] /= nTrajectories
    ProtPopulation[j] /= nTrajectories

calcRnoLevel = betaM / gammaM
plt.axhline(y=calcRnoLevel, color='#fa0', linestyle='-')
plt.plot(RnaPopulation, color='r', linewidth=1.5)
plt.show()
