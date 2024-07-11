# Ask the users developer-made questions and keep score.
score = 0
cor = 'You are correct!'
incor = 'You are incorrect!'
n = input('Hello contestant! What is your name? ')
while n in {'', ' '}:
    print('It seems you did not input a name. Please try again!')
    n = input('')
if n not in {'', ' '}:
    print("Okay, " + n + ". Today, we will be having a small trivia game. Let's see how many you can get right!")
    print('1. What is a piece of native American culture that is believed to catch the nightmares of those who sleep? ')
    print('''A. Dream catcher 
B. Nightmare catcher 
C. Night light 
D. Poppet ''')
    A1 = input('')
    if A1 in {'A', 'a'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('2. He was a Post-Impressionists painter whose art was only globally recognized after his death.')
    print('''A. Leonardo Davinci
B. Vincent Van Gogh
C. Igor Stravinsky
D. Antonio Vivaldi''')
    A2 = input('')
    if A2 in {'B', 'b'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print("3. In the popular anime 'Kimetsu no Yaiba', who is considered the main antagonist?")
    print('''A. Kibutsuji Muzan
B. Michael Jackson
C. Kamado Tanjiro
D. Ubuyashiki Kagaya''')
    A3 = input('')
    if A3 in {'A', 'a'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('4. Which terrestrial planet is the largest?')
    print('''A. Jupiter
B. Venus
C. Saturn
D. Earth''')
    A4 = input('')
    if A4 in {'D', 'd'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('5. Which of the following is NOT a Shakespearean play?')
    print('''A. Othello
B. Hamlet
C. The Queen of The Night
D. Henry IV''')
    A5 = input('')
    if A5 in {'C', 'c'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('6. Who was the last queen of Egypt?')
    print('''A. Neithhotep
B. Cleopatra
C. Nefertiti
D. Hapshetsut''')
    A6 = input('')
    if A6 in {'B', 'b'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('7. In Greek mythology, who is portrayed as the ruler of the underworld?')
    print('''A. Satan
B. Lucifer
C. Pluto
D. Hades''')
    A7 = input('')
    if A7 in {'D', 'd'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('8. In Christian belief, what is the story behind the many languages of the world?')
    print('''A. Wisdom of Solomon
B. The Tower of Babel
C. Samson and Delilah
D. Noah's Ark''')
    A8 = input('')
    if A8 in {'B', 'b'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('9. What exact date was slavery abolished in England?')
    print('''A. August 1, 1834
B. June 12, 1898
C. June 28, 1919
D. December 16, 1773''')
    A9 = input('')
    if A9 in {'A', 'a'}:
        score += 1
        print(cor)
    else:
        print(incor)
    print('10. In poetry, a poem that has a certain text structure which often creates shapes, outlines, or visual art'
          'objects using the placement or arrangement of words or symbols is typically called what?')
    print('''A. Word art
B. Free-form poem
C. Concrete poem
D. Lyrical poem''')
    A10 = input('')
    if A10 in {'C', 'c'}:
        score += 1
        print(cor)
    else:
        print(incor)
    if score in range(8, 11):
        print('Wow, ', n, '! You did so well! Your score is: ', score)
    elif score in range(4, 8):
        print('Good job, ', n, '. Your score is:', score)
    elif score in range(0, 4):
        print('Aww, better luck next time, ', n, '! Your score is: ', score)
    print('Thank you for playing! Please share me with your friends, ', n, '!')
    input('')
