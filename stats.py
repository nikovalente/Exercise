fhand=open("StudentExercise.csv")
ls_hrsex=list()
next(fhand)
for line in fhand:
    nums=line.split(',')
    ls_hrsex.append(nums[0])
print(ls_hrsex)
