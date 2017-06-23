try_list = [1,42,12,83,34,87,5,8,55]
list_backwards = [10,9,8,7,6,5,4,3,2,1] #Hardest case measuring by space complexity


def bubble_sort(list):
    iteration_helper = len(list)-1
    for i in range(iteration_helper):
        for i in range(iteration_helper):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
        iteration_helper -= 1
    return list

a = bubble_sort(try_list)
b = bubble_sort(list_backwards)
print(a)
print(b)

#OUTPUT: 
[1, 5, 8, 12, 34, 42, 55, 83, 87]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
