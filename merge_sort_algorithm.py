try_list = [1,2,3,21,3,213,2132,3,23213,4221,32,432,32,19,239,92,313,46,376,23,78]

def merge_algorithm(list):
    i,j,k=0,0,0
    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sep(left_half)
        merge_sep(right_half)

        while i < len(left_half) and j < len(right_half):

            if left_half[i] <= right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list[k] = left_half[i]
            i +=1
            k +=1
        while j < len(right_half):
            list[k] = right_half[j]
            j +=1
            k +=1

    return list
a = merge_algorithm(try_list)
print(a)
#output : [1, 2, 3, 3, 3, 19, 21, 23, 32, 32, 46, 78, 92, 213, 239, 313, 376, 432, 2132, 4221, 23213]
