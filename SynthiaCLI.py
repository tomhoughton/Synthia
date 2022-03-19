# Imports:
import time
import os
import platform
from InputSynthiaV2 import run_input
import pandas as pd
from SynthiaStats import SynthiaStats

def display_title():
    line_01 = '░██████╗██╗░░░██╗███╗░░██╗████████╗██╗░░██╗██╗░█████╗'

    for c in line_01:
        print(c, end=' ')
        time.sleep(0.13)

def clear_console():
    # Get the os that the user is using:
    usr_os = platform.system()

    if (usr_os == 'Darwin'):
        clear = lambda: os.system('clear')
        clear()
    elif (usr_os == 'Windows'):
        clear = lambda: os.system('cls')
        clear()

def input_data(delay):
    print('Input Data')

    # Clear the console:
    clear_console()

    print('██╗███╗░░██╗██████╗░██╗░░░██╗████████╗  ██████╗░░█████╗░████████╗░█████╗░')
    time.sleep(delay)
    print('██║████╗░██║██╔══██╗██║░░░██║╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗')
    time.sleep(delay)
    print('██║██╔██╗██║██████╔╝██║░░░██║░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║')
    time.sleep(delay)
    print('██║██║╚████║██╔═══╝░██║░░░██║░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║')
    time.sleep(delay)
    print('██║██║░╚███║██║░░░░░╚██████╔╝░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║')
    time.sleep(delay)
    print('╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝')
    time.sleep(delay)

    # Run the input function:
    run_input()

def exit(delay):

    # Clear the console:
    clear_console()

    # Display exit screen:
    print('░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗')
    time.sleep(delay)
    print('██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝')
    time.sleep(delay)
    print('██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░')
    time.sleep(delay)
    print('██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░')
    time.sleep(delay)
    print('╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗')
    time.sleep(delay)
    print('░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝')
    time.sleep(delay)


def data_summary(delay):

    # Clear the console:
    clear_console()

    print('██████╗░░█████╗░████████╗░█████╗░  ░██████╗██╗░░░██╗███╗░░░███╗███╗░░░███╗░█████╗░██████╗░██╗░░░██╗')
    time.sleep(delay)
    print('██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔════╝██║░░░██║████╗░████║████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝')
    time.sleep(delay)
    print('██║░░██║███████║░░░██║░░░███████║  ╚█████╗░██║░░░██║██╔████╔██║██╔████╔██║███████║██████╔╝░╚████╔╝░')
    time.sleep(delay)
    print('██║░░██║██╔══██║░░░██║░░░██╔══██║  ░╚═══██╗██║░░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗░░╚██╔╝░░')
    time.sleep(delay)
    print('██████╔╝██║░░██║░░░██║░░░██║░░██║  ██████╔╝╚██████╔╝██║░╚═╝░██║██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░')
    time.sleep(delay)
    print('╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░')
    time.sleep(delay)

    # Get the path to the datasets:
    df_path = os.path.join('TrainingData', 'Datasets')
    
    # Get a list of all of the datasets:
    datasets = os.listdir(df_path)

    # Display all of the datasets:
    for dataset, x in enumerate(datasets):
        print(x, ': ', dataset)

    usr_input = int(input('Select which dataset you would like to summarise: '))

    df = pd.read_csv(os.path.join(df_path, datasets[usr_input]))

    S_Stats = SynthiaStats(data=df)
    S_Stats.type_count()
    combination_counts = S_Stats.get_combination_counts()
    S_Stats.display_dataframe()
    print(combination_counts)
    print('------ Min and Max Test -----')
    S_Stats.get_combination_min_max()


    return ''


    


def data_augment(delay):

    print('██████╗░░█████╗░████████╗░█████╗░  ░█████╗░██╗░░░██╗░██████╗░███╗░░░███╗███████╗███╗░░██╗████████╗')
    print('██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░██║██╔════╝░████╗░████║██╔════╝████╗░██║╚══██╔══╝')
    print('██║░░██║███████║░░░██║░░░███████║  ███████║██║░░░██║██║░░██╗░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░')
    print('██║░░██║██╔══██║░░░██║░░░██╔══██║  ██╔══██║██║░░░██║██║░░╚██╗██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░')
    print('██████╔╝██║░░██║░░░██║░░░██║░░██║  ██║░░██║╚██████╔╝╚██████╔╝██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░')
    print('╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░')

def root_menu(delay):
    # Clear the console:
    clear_console()

    # Display the title:
    print('░██████╗██╗░░░██╗███╗░░██╗████████╗██╗░░██╗██╗░█████╗')
    time.sleep(delay)
    print('██╔════╝╚██╗░██╔╝████╗░██║╚══██╔══╝██║░░██║██║██╔══██╗')
    time.sleep(delay)
    print('╚█████╗░░╚████╔╝░██╔██╗██║░░░██║░░░███████║██║███████║')
    time.sleep(delay)
    print('░╚═══██╗░░╚██╔╝░░██║╚████║░░░██║░░░██╔══██║██║██╔══██║')
    time.sleep(delay)
    print('██████╔╝░░░██║░░░██║░╚███║░░░██║░░░██║░░██║██║██║░░██')
    time.sleep(delay)
    print('╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═')
    time.sleep(delay)

    # Display the menu:
    print('-----------------------------------------------------')
    print('     Select [1] for Input Data                       ')
    print('     Select [2] for Data Summary                     ')
    print('     Select [3] for Data Augmentation                ')
    print('     Select [4] for Machine Learning                 ')
    print('     Select [5] for Server                           ')
    print('     Type [exit] to exit                             ')
    print('-----------------------------------------------------')


def main():
    delay = 0.13 # Delay for the title display.
    isActive = True # Bool to control if the program should continue running.


    while isActive == True:
        root_menu(delay=delay)

        # Get the user input:
        usr_input = input('==>')
        
        if usr_input == '1':
            input_data(delay=delay)
        elif usr_input == '2':
            data_summary(delay=delay)
        elif usr_input == '3':
            data_augment(delay=delay)
        elif usr_input == 'exit':
            exit(delay=delay)

main()


