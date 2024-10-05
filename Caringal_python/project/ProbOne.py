def probOne():
    students = {'John', 'Maria', 'David', 'Samantha'} 

    while True:
        try:
            index = int(input('Enter index: '))
            
            current_index = 0
            student = None
            
            for stud in students:
                if current_index == index:
                    student = stud
                    break
                current_index += 1
            
            if student is not None:
                print(f'Student at index {index} is {student}.')
            else:
                raise IndexError('Enter only between -4 and 3')
            break
        except ValueError:
            print('Enter only integer numbers\n')
        except IndexError as ie:
            print(f'Error: {ie}\n')
