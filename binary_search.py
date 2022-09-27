
def binary_search(list, target):
    
    start = 0
    middle = 0
    end = len(list)
    step = 0
    
    while start <= end :
        print(f'\nStep {step}: {str(list[start:end+1])}')
        
        step += 1
        middle = (start + end) // 2
        
        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        
    return -1

my_list = list(range(50))
target = 47

binary_search(my_list, target)