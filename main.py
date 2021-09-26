import pandas as pd
import itertools

 
def getOverlap(a, b):
    temp = min(a[1], b[1]) - max(a[0], b[0])
    return max(0, temp.total_seconds())

# Function to print the intersection
def findIntersection(vet):

    sum = 0
    subseq = itertools.combinations(vet, 2)

    for i in subseq:
        a = i[0]
        b = i[1]
        sum += getOverlap(a,b)

    return sum

# intialise data of lists.
data = {'S':["1/1/2018 05-05-05", "1/1/2018 05-10-05", "1/1/2018 05-25-05"],
        'E':["1/1/2018 06-05-05", "1/1/2018 06-10-05", "1/1/2018 06-15-05"]}
df = pd.DataFrame(data)
df["S"] = pd.to_datetime(df["S"], format='%d/%m/%Y %H-%M-%S')
df["E"] = pd.to_datetime(df["E"], format='%d/%m/%Y %H-%M-%S')
df["Int"] = df.apply(lambda x: [x[0], x[1]], axis=1)
#df = df.drop(['S', 'E'], axis=1)
intervals = df["Int"].to_list()

sum = findIntersection(intervals)

kk = (df["E"]-df["S"]).sum().total_seconds()

print(sum)
print(kk)
print(kk-sum)