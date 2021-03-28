import os
from getpass import getpass

def win():
    print(f'\nBJP = {bjp}')
    print(f'Congress = {congress}')
    print(f'Shivsena = {shivsena}')
    print(f'Aam Aadmi Party = {aap}')
    print(f'Nota = {nota}\n')

    if bjp > congress and bjp > shivsena and bjp > aap and bjp > nota :
        print('\n\nBJP Wins')
        print(f'Votes : {bjp}\n\n')

    elif congress > bjp and congress > shivsena and congress > nota and  congress > aap:
        print('\n\nCongress Wins')
        print(f'Votes : {congress}\n\n')

    elif aap > bjp and aap > congress and aap > shivsena and aap > nota:
        print('\n\nAam Aadmi Party Wins')
        print(f'Votes : {aap}\n\n')

    elif shivsena > bjp and shivsena > aap and shivsena > congress and shivsena > nota :
        print('\n\nShivsena Wins')
        print(f'Votes : {shivsena}\n\n')

    elif nota > bjp and nota > aap and nota > congress and nota > shivsena:
        print('\n\nNOTA has highest votes')
        print(f'Votes : {nota}\n\n')

    else:
        print('\n\nCan\'t be Decided\n\n')

global bjp, congress, aap, shivsena

bjp = 0
congress = 0
aap = 0
shivsena = 0
nota = 0

while 1 == 1:
    voter = input('\nEnter your name :- ')
    file = open('votes.txt', 'a')
    file1 = open('votes.txt', 'r')
    content = file1.read()

    if voter  in content:
        print('\nAlready Voted\n\n')

    else:
        voting_Party = input('''\n\n
        1. BJP
        2. Congress
        3. Aam Aadmi Party
        4. Shivsena
        5. NOTA
        6. Help
        7. Number of votes

        Enter the name of Party here : ''')

        
        if voting_Party == '1':
            data = [f'{voter}', 'BJP']
            file.writelines(f'{data}')
            file.writelines('\n\n')
            file.close
            print(f'\nSuccessfully voted to BJP\n')
            bjp = bjp + 1
            close = input('Press any key to Submit vote ')
            os.system('cls')
            
        elif voting_Party == '2':
            data = [f'{voter}', 'Congress']
            file.writelines(f'{data}')
            file.writelines('\n\n')
            file.close
            print(f'\nSuccessfully voted to Congress\n')
            congress = congress + 1
            close = input('Press any key to Submit vote ')
            os.system('cls')
            
        elif voting_Party == '3':
            data = [f'{voter}', 'Aam Aadmi Party']
            file.writelines(f'{data}')
            file.writelines('\n\n')
            file.close
            print(f'\nSuccessfully voted to Aam Aadmi Party\n')
            aap = aap + 1
            close = input('Press any key to Submit vote ')
            os.system('cls')
            
        elif voting_Party == '4':
            data = [f'{voter}', 'Shivsena']
            file.writelines(f'{data}')
            file.writelines('\n\n')
            file.close
            print(f'\nSuccessfully voted to Shivsena\n')
            shivsena = shivsena + 1
            close = input('Press any key to Submit vote ')
            os.system('cls')
            
        elif voting_Party == '5':
            data = [f'{voter}', 'NOTA']
            file.writelines(f'{data}')
            file.writelines('\n\n')
            file.close
            print('Successfully Voted to Nota')
            nota = nota + 1
            close = input('Press any key to Submit vote ')
            os.system('cls')
            
        elif voting_Party == '7':
            code = getpass('\nEnter code to see confidenciery Information of Voting :- ')
            if code == 'black_code':
                win()
                close = input('Press Enter if you have read it ')
                os.system('cls')
            
            else:
                print('Not entered Correct Code')

        else:
            print('Enter Valid Input')
            os.system('cls')



