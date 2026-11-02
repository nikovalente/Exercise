fhand=open("StudentExercise.csv")
ls_hrsex=list()
next(fhand)
for line in fhand:
    nums=line.split(',')
    ls_hrsex.append(nums[0])
ls_hrsex.sort()
print(ls_hrsex)

import matplotlib.pyplot as plt
plt.hist(ls_hrsex,bins=7)
plt.ylabel('Currency of hours')
plt.title('Number of hours of exercise')
plt.xticks([0,2,4,6,8,10,12,14,18,20,22,24])
plt.show()

def average(ls):
  total=0
  count=0
  for num in ls:
      num=float(num)
      total+=num
      count+=1
  return total/count
print('The average is:',average(ls_hrsex))
