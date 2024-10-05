def probFour():
    numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)
    
    for i in range(len(numbers)):
        count = 0
        is_counted = False
        
        for k in range(i):
            if numbers[k] == numbers[i]:
                is_counted = True
                break
                
        if not is_counted:
            for j in range(len(numbers)):
                if numbers[i] == numbers[j]:
                    count += 1
            if count > 1:
                print(f'{numbers[i]} appeared in the tuple {count} times')
