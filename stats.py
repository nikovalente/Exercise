fhand=open("StudentExercise.csv")
ls_hrsex=list()
for line in fhand:
    nums=line.split(',')
    ls.hrsex.append(nums[0])
print(ls_hrsex)
