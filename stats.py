fhand=open("StudentExercise.csv")
ls_hrsex=list()
next(fhand)
for line in fhand:
    nums=line.split(',')
    ls_hrsex.append(nums[0])
ls_hrsex.sort()
print(ls_hrsex)

import matplotlib.pyplot as plt
ls_new=list()
for num in ls_hrsex:
    if num!='':
      num=float(num)
      ls_new.append(num)
ls_new.sort()
plt.hist(ls_new,bins=7)
plt.ylabel('Currency of hours')
plt.title('Number of hours of exercise')
#plt.xticks([0,2,4,6,8,10,12,14,18,20,22,24])
plt.show()

def average(ls):
    total=0
    count=0
    for num in ls:
        if num!='':
            num=float(num)
            total+=num
            count+=1
    return total/count
x=average(ls_new)
print("avg is {:.2f}".format(x))

def prop_above(ls):
    x=average(ls)
    tot_students=len(ls)
    n_students=0
    for student in ls:
        if student!='':
            if float(student)>x:
                n_students+=1
    return n_students/tot_students
y=prop_above(ls_new)
print("percent above avg is {0:.0%}".format(y))

def median(ls):
    ls.sort()
    n=len(ls)
    if n%2==0:
        return (float(ls[n//2-1])+float(ls[n//2]))/2
    else:
        return float(ls[n//2])
print('The median of the data is:',median(ls_new))
