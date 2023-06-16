def find_first_unique(lst):
    for i in range(len(lst)):
       temp = []
       for j in range(len(lst)):
           if(i == j):
               continue
           temp.append(lst[j])
       if lst[i] not in temp:
           return lst[i]
       temp.clear()
           
           


print(find_first_unique([4, 5, 1, 2, 0, 4]))
print(find_first_unique([9, 2, 3, 2, 6, 6]))