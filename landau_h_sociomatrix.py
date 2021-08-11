import string
import numbers as num
import pandas as pd
from functools import reduce


# function to calculate landau's h
def landau_h(n, v):
    result = reduce(lambda a, x: a + ((x - ((n - 1) / 2)) ** 2), [0] + v)
    h = (12 / ((n ** 3) - n)) * result

    return h


# function to calculate deVrie's correction h'
def devrie_correction_h(n, u, v):
    result = reduce(lambda a, x: a + ((x - ((n - 1) / 2)) ** 2), [0] + v)
    h = ((12 / ((n ** 3) - n)) * result)
    hprime = (6 / ((n ** 3)) * u) + h

    return hprime


# a function to create a list of alphabet labels ranging from A to however many labels you need
def alpha_list_maker(alphabet_size):
    current_count = 0
    alphabet_letters = string.ascii_uppercase
    alphabet_list = list()

    while current_count < alphabet_size < 26:
        alphabet_list.append(alphabet_letters[current_count])
        current_count += 1

    while current_count < 26 < alphabet_size:
        alphabet_list.append(alphabet_letters[current_count])
        current_count += 1

    for letter_1 in alphabet_letters:
        for letter_2 in alphabet_letters:
            if current_count < alphabet_size:
                alphabet_list.append(letter_1 + letter_2)
                current_count += 1

    return alphabet_list


def check_float(string_value):
    try:
        float(string_value)
        return True
    except ValueError:
        return False


# asks for a valid amount of animals in the society
while True:
    try:
        n_int = int(input('Enter the number of animals in the society: '))
        if n_int != 0:
            break
        else:
            print('Please enter a valid number for the amount of animals in the society!')
    except ValueError:
        print('Please enter a valid number for the amount of animals in the society!')

alpha_labels = alpha_list_maker(n_int)
df = pd.DataFrame(index=alpha_labels, columns=alpha_labels)  # assign alphabet as column

print('')
print('If you dont know the winner, type: unknown', '\n')
jagged_start_index = 0  # the number that the row starts on the diagonal line
unknown_pairs = 0

# fill out half the sociomatrix, automatically fill the other half with the opposite value
for row_mouse in range(len(df.index)):
    row_name = alpha_labels[row_mouse]
    total_row_victories = 0
    for col_mouse in range(jagged_start_index, len(df.columns)):
        col_name = alpha_labels[col_mouse]
        if row_name == col_name:
            df.at[row_name, col_name] = '-'
        else:
            while True:
                print('For row animal', row_name, 'vs column animal', col_name)
                print('Did', row_name, 'win?')
                winner = input('Type: yes, no, unknown, or enter the mean wins: ')
                print('\n')
                if winner == 'yes':
                    df.at[row_name, col_name] = 1
                    df.at[col_name, row_name] = 0
                    break
                elif winner == 'no':
                    df.at[row_name, col_name] = 0
                    df.at[col_name, row_name] = 1
                    break
                elif winner == 'unknown':
                    df.at[row_name, col_name] = '?'
                    df.at[col_name, row_name] = '?'
                    unknown_pairs += 1
                    break
                elif check_float(winner):
                    if 0 <= float(winner) <= 1:
                        df.at[row_name, col_name] = float(winner)
                        df.at[col_name, row_name] = 1 - float(winner)
                        break
                else:
                    print('You entered the wrong row information for:', row_name, 'vs', col_name)
                    print('Please re-enter the information for:', row_name, 'vs', col_name, '\n')
    jagged_start_index += 1

# shows the total victories for all the animals in the society
df_victories = pd.DataFrame(index=alpha_labels, columns=['Total Victories'], dtype=float)
row_victory_list = list()
for row in df.index:
    total_row_victories = 0
    for col in df.columns:
        if isinstance(df.at[row, col], num.Number):
            total_row_victories += df.at[row, col]
    df_victories.at[row, 'Total Victories'] = total_row_victories
    row_victory_list.append(total_row_victories)

# landau's h and deVrie's correction
landau = landau_h(n_int, row_victory_list)
devrie = devrie_correction_h(n_int, unknown_pairs, row_victory_list)

# generates visualisation of sociomatrix
print('')
print('Sociomatrix')
print('-----------')
print(df)
print('-----------', '\n')

print(df_victories, '\n')
print("The Landau's h value is:", landau)
print("The DeVries Correction h' value is:", devrie)
