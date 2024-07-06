print('Hello! My name is Serpentine. I will be helping you through the day.')
YN = input('First, what is your name? ')
while YN == '':
    print('It seems you did not input a name. Please try again. ')
    YN = input('')
if YN not in {'', ' '}:
    print('Okay, great! ' + YN + ', we can now begin!')
    tasks = ['brushing teeth', 'showering', 'cooking', 'making rice', ]
    while True:
        action = input('What are the tasks you want to do today, ' + YN + '? Please list them one by one. ')
        tasks.append(action)
        if action in {'done', 'n', 'no', 'none', 'Done', 'N', 'No', 'None'}:
            value = False
            print('Here are your tasks today: ')
            print(tasks)
            tasks_index = 0
            while tasks_index < len(tasks) - 1:
                input('Task done? ')
                print(tasks[tasks_index] + ' done')
                tasks_index += 1
                if tasks_index == (len(tasks) - 1):
                    print('All tasks done!')
                    print('Please choose what you would like to do now, ' + YN + '.')
                    print('''A. Write a story/poem
B. Practice an instrument
C. Code a new project
D. Read a book
E. something else''')
                    new_task = input('')
                    if new_task in {'A', 'a'}:
                        input('Which instrument? ')

