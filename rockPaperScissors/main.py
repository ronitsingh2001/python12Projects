import random

def play():
    '''
    (NoneType) -> str

    Start the game.
    '''
    user = input("What's your choice? 'r' for rock, 'p' for scissors, 's' for scissors :")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    '''
    (str, str) -> bool

    Return true only and only if one of condition comparing str and str is true.
    '''
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())