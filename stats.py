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
        if num!='':
            num=float(num)
            total+=num
            count+=1
    return total/count
print('The average is:',average(ls_hrsex))

def prop_above(ls):
    x=average(ls)
    tot_students=len(ls)
    n_students=0
    for student in ls:
        if student!='':
            if float(student)>x:
                n_students+=1
    return n_students/tot_students
print('The proportion of the students above the average is:',prop_above(ls_hrsex))
