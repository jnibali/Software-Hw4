def Average(lst):
    if sum(lst) == 0:
        return 0
    else:
        return sum(lst) / len(lst)
  
# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
  
# Printing average of the list
print("Average of the list =", round(average, 2))