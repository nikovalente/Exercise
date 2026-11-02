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
plt.show()
