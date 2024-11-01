
Name1=['A','B','C','D']
Name2=['A','B','C']
absent= set(Name1)-set(Name2)
sorted_absent=sorted(absent)
print(sorted_absent , " are absent")
present= (set(Name1)- absent)
sorted_present=sorted(present)
print(sorted_present ," are present")