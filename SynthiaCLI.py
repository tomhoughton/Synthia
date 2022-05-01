# Imports:
import time
import os
import platform
import pandas as pd
from InputSynthiaV2 import run_input
from SynthiaDataAugment import DataAugmentor
from SynthiaDataAugmentV2 import Augmentor
from SynthiaStats import SynthiaStats

def display_title():
    line_01 = '░██████╗██╗░░░██╗███╗░░██╗████████╗██╗░░██╗██╗░█████╗'

    for c in line_01:
        print(c, end=' ')
        time.sleep(0.13)

def display_data_augment_title():
    print('██████╗░░█████╗░████████╗░█████╗░  ░█████╗░██╗░░░██╗░██████╗░███╗░░░███╗███████╗███╗░░██╗████████╗')
    print('██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░██║██╔════╝░████╗░████║██╔════╝████╗░██║╚══██╔══╝')
    print('██║░░██║███████║░░░██║░░░███████║  ███████║██║░░░██║██║░░██╗░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░')
    print('██║░░██║██╔══██║░░░██║░░░██╔══██║  ██╔══██║██║░░░██║██║░░╚██╗██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░')
    print('██████╔╝██║░░██║░░░██║░░░██║░░██║  ██║░░██║╚██████╔╝╚██████╔╝██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░')
    print('╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░')

def consistency_title():
    # Display consistency title:
    print('---------------------------------------------------------------------------------------')
    print('░█████╗░░█████╗░███╗░░██╗░██████╗██╗░██████╗████████╗███████╗███╗░░██╗░█████╗░██╗░░░██╗')
    print('██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝')
    print('██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔██╗██║██║░░╚═╝░╚████╔╝░')
    print('██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚████║██║░░██╗░░╚██╔╝░░')
    print('╚█████╔╝╚█████╔╝██║░╚███║██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚███║╚█████╔╝░░░██║░░░')
    print('░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░')
    print('---------------------------------------------------------------------------------------')

def brightness_title():
    print('------------------------------------------------------------------------------')
    print('██████╗░██████╗░██╗░██████╗░██╗░░██╗████████╗███╗░░██╗███████╗░██████╗░██████╗')
    print('██╔══██╗██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝████╗░██║██╔════╝██╔════╝██╔════╝')
    print('██████╦╝██████╔╝██║██║░░██╗░███████║░░░██║░░░██╔██╗██║█████╗░░╚█████╗░╚█████╗░')
    print('██╔══██╗██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗')
    print('██████╦╝██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██║░╚███║███████╗██████╔╝██████╔╝')
    print('╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░')
    print('------------------------------------------------------------------------------')

def dynamics_title():
    print('----------------------------------------------------------------')
    print('██████╗░██╗░░░██╗███╗░░██╗░█████╗░███╗░░░███╗██╗░█████╗░░██████╗')
    print('██╔══██╗╚██╗░██╔╝████╗░██║██╔══██╗████╗░████║██║██╔══██╗██╔════╝')
    print('██║░░██║░╚████╔╝░██╔██╗██║███████║██╔████╔██║██║██║░░╚═╝╚█████╗░')
    print('██║░░██║░░╚██╔╝░░██║╚████║██╔══██║██║╚██╔╝██║██║██║░░██╗░╚═══██╗')
    print('██████╔╝░░░██║░░░██║░╚███║██║░░██║██║░╚═╝░██║██║╚█████╔╝██████╔╝')
    print('╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚════╝░╚═════╝░')
    print('----------------------------------------------------------------')

def clear_console():
    # Get the os that the user is using:
    usr_os = platform.system()

    if (usr_os == 'Darwin'):
        clear = lambda: os.system('clear')
        clear()
    elif (usr_os == 'Linux'):
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
    usr_input_2 = input('Press [y] to export the statistical summaries, press [n] to leave it: ')

    # Handle the usr_input:
    if (usr_input_2 == 'y'):
        usr_input_2 = True
    else:
        usr_input_2 = False
    
    # Get and store the dataframe the user would like:
    df = pd.read_csv(os.path.join(df_path, datasets[usr_input]))

    # Create a new Synthia Stats class and provide it with the selected dataframe:
    S_Stats = SynthiaStats(data=df, is_exporting=usr_input_2)
    
    # Display the dataframe
    S_Stats.display_dataframe()
    # x = input('...')

    # Get the type count:
    S_Stats.type_count()
    # x = input('...')

    # Get the binary combination counts:
    combination_counts = S_Stats.get_combination_counts()
    print(combination_counts)
    # x = input('...')

    consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm = S_Stats.get_descriptor_degrees_min_max_mean()
    
    S_Stats.display_decriptor_stats(consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm)

    # Call the export function:
    S_Stats.export_statistics()

    usr_input = input('Type [exit] to go back to the main menu')

    if (usr_input == 'exit'):
        return ''
 

    return ''


def data_augment(delay):

    # Clear the console:
    clear_console() 

    # Display the data augment title:
    display_data_augment_title()    

    """REPEATING CODE"""
    # Get the path to the datasets:
    df_path = os.path.join('TrainingData', 'Datasets')
    
    # Get a list of all of the datasets:
    datasets = os.listdir(df_path)

    # Display all of the datasets:
    for dataset, x in enumerate(datasets):
        print(x, ': ', dataset)

    usr_input = int(input('Select which dataset you would like to summarise: '))
    
    print('USR INPUT: ')
    print(datasets[usr_input])
    x = input('...')

    date = datasets[usr_input]
    # Get and store the dataframe the user would like:
    df = pd.read_csv(os.path.join(df_path, datasets[usr_input]))
    
    # Right we need to generate the statistics based of the dataset that we want to use:
    # I would do it where we pick the stats that we want to use but lets try do this automatically.

    print('Are you exporting? y or n')
    x = input('=> ')

    export_stats = None
    if x == "y":
        export_stats = True
    elif x == "n":
        export_stats = False

    S_Stats = SynthiaStats(data=df, is_exporting=export_stats)
    
    # Display the dataframe:
    clear_console()
    display_data_augment_title()
    S_Stats.display_dataframe()
    # x = input('...')

    # Get the type count:
    clear_console()
    display_data_augment_title()
    S_Stats.type_count()
    # x = input('...')

    # Get the binary combination counts:
    clear_console()
    display_data_augment_title()
    combination_counts = S_Stats.get_combination_counts()
    print(combination_counts)
    x = input('...')

    # clear_console()
    # display_data_augment_title()

    # Get the descriptor degrees min max and mean
    cons_mmm, dyna_mmm, brigh_mmm, evol_mmm = S_Stats.get_descriptor_degrees_min_max_mean()
    # S_Stats.display_decriptor_stats(consistency=cons_mmm, dynamics=dyna_mmm, brightness=brigh_mmm, evolution=evol_mmm)
    # x = input('...')

    # Now we must export the statistics:
    clear_console()
    display_data_augment_title()
    print('Exorting the statistics: ')
    S_Stats.export_statistics()

    # Create an augmentor object:
    augmentor = Augmentor(df=df, date=S_Stats.export_folder_name)

    # Sort the min max and stats paths:
    clear_console()
    display_data_augment_title()
    print('Now we are sorting the statistics into ascending order in accordance of the descriptor degree')
        # print('Consistency')
    consistency_stats = augmentor.sort_min_max_stats_paths(augmentor.consistency_path)
    # print('Dynamics')
    dynamics_stats = augmentor.sort_min_max_stats_paths(augmentor.dynamics_path)
    # print('Brightness')
    brightness_stats = augmentor.sort_min_max_stats_paths(augmentor.brightness_path)
    # print('Evolution')
    evolution_stats = augmentor.sort_min_max_stats_paths(augmentor.evolution_path)
    # We now need to set the statistics using the function in the augmentor:
    augmentor.set_descriptor_stats(
        consistency=consistency_stats,
        dynamics=dynamics_stats,
        brightness=brightness_stats,
        evolution=evolution_stats    
    )
    # This is now where we will augment the data:
    augmentor.augment()
    # # Augment the data:
    # augmentor.augment(method='method', margin=0.2) 
    # # augmentor.augment_min_max(augment_margin=1)

    x = input('...')


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
            return '...'

main()
