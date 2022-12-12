#!/usr/bin/env python3
# ----------------------------------------------------
# Mateus Araujo (116290) e Rafael Mendes (116336)
# PSR Typing Test, December 2022
# ----------------------------------------------------


import argparse
import time      
import random    

from readchar import readkey
from colorama import Fore, Style
from collections import namedtuple
from pprint import pprint


def main():

    #Argument parser
    parser = argparse.ArgumentParser(description='PSR Typing Test | Mateus Araujo e Rafael Mendes')
    parser.add_argument('-utm', '--use_time_mode', type=int,required=True, 
                        help='Max number of seconds for Time Mode or maximum number of inputs for Input Mode.')
    parser.add_argument('-mv', '--max_value', action='store_true', required=False,
                        help='With this argument included, it enables Input Mode based on number inserted previously.')

    args = vars(parser.parse_args())

    value = args['use_time_mode']


    #Creating namedtuple
    Input = namedtuple('Input',
                        'requested received duration')


    #Variables initialization
    test_start = 0
    test_end = 0
    test_duration = 0

    number_of_types = 0
    number_of_hits = 0

    accuracy = 0

    type_average_duration = []
    type_hit_average_duration = []
    type_miss_average_duration = []

    inputs = []


    #Game header
    print(Style.BRIGHT + Fore.MAGENTA + 'PSR Typing Test' + Fore.RESET + Style.RESET_ALL)
    print(Style.BRIGHT + 'Mateus Araujo e Rafael Mendes | Novembro 2022' + Style.RESET_ALL + '\n')


    #Input limit GAME MODE
    if args['max_value'] == True:
        
        print(Style.NORMAL + 'Test running up to ' + str(value) + ' inputs' + Style.RESET_ALL + '\n')
        print(Style.DIM + 'Press any key to start the Typing Test, to cancel press SPACE' + Style.RESET_ALL)
        start_or_cancel = readkey()

        if start_or_cancel == ' ':
            print(Style.BRIGHT + Fore.RED + 'Test canceled!' + Fore.RESET + Style.RESET_ALL)
            exit()

        test_start = time.time()
        start_date = time.ctime()

        for i in range(value):
            
            #Generate random letters
            key_asked = chr(random.randint(ord('a'), ord('z')))
            print('Type letter ' + Fore.BLUE + str(key_asked) + Fore.RESET)
            
            type_start = time.time()
            
            key_received = readkey()
            number_of_types = number_of_types + 1

            type_end = time.time()
            type_average_duration.append(type_end - type_start)
            
            if key_received == ' ':
                print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'SPACE key pressed by user!' + Fore.RESET + Style.RESET_ALL)
                break;
            elif key_received == key_asked:
                print('You typed letter ' + Fore.GREEN + str(key_received) + Fore.RESET)

                number_of_hits = number_of_hits + 1

                type_hit = time.time()
                type_hit_average_duration.append(type_hit - type_start)
            else:
                print('You typed letter ' + Fore.RED + str(key_received) + Fore.RESET)

                type_miss = time.time()
                type_miss_average_duration.append(type_miss - type_start)

            i = Input(key_asked, key_received, type_end - type_start)
            inputs.append(i)
            
        test_end = time.time()
    
    #Time limit GAME MODE
    else:

        print(Style.NORMAL + 'Test running up to ' + str(value) + ' seconds' + Style.RESET_ALL + '\n')
        print(Style.DIM + 'Press any key to start the Typing Test, to cancel press SPACE' + Style.RESET_ALL)
        start_or_cancel = readkey()

        if start_or_cancel == ' ':
            print(Style.BRIGHT + Fore.RED + 'Test canceled!' + Fore.RESET + Style.RESET_ALL)
            exit()
        
        test_start = time.time()
        start_date = time.ctime()


        while test_end - test_start  < value: 

            #Generate random letters
            key_asked = chr(random.randint(ord('a'), ord('z')))
            print('Type letter ' + Fore.BLUE + str(key_asked) + Fore.RESET)
            
            type_start = time.time()
            
            key_received = readkey()
            number_of_types = number_of_types + 1

            type_end = time.time()
            type_average_duration.append(type_end - type_start)
            
            if key_received == ' ':
                print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'SPACE key pressed by user!' + Fore.RESET + Style.RESET_ALL)
                break;
            elif key_received == key_asked:
                print('You typed letter ' + Fore.GREEN + str(key_received) + Fore.RESET)

                number_of_hits = number_of_hits + 1
                
                type_hit = time.time()
                type_hit_average_duration.append(type_hit - type_start)
            else:
                print('You typed letter ' + Fore.RED + str(key_received) + Fore.RESET)
                
                type_miss = time.time()
                type_miss_average_duration.append(type_miss - type_start)

            test_end = time.time()


            i = Input(key_asked, key_received, type_end - type_start)
            inputs.append(i)

    end_date = time.ctime()
    #Test finish message
    print(Style.BRIGHT + Fore.MAGENTA + 'Test finished!' + Fore.RESET + Style.RESET_ALL)
    
    #Calculations
    test_duration = test_end - test_start
    
    if number_of_hits == 0 and sum(type_miss_average_duration) == 0:
        accuracy = 0
        average_hit_duration = 0
        average_miss_duration = 0

    elif number_of_hits == 0:
        accuracy = 0
        average_hit_duration = 0
        average_miss_duration = sum(type_miss_average_duration) / len(type_miss_average_duration)
    
    elif sum(type_miss_average_duration) == 0:
        accuracy = (number_of_hits / number_of_types) * 100
        average_miss_duration = 0
        average_hit_duration = sum(type_hit_average_duration) / len(type_hit_average_duration)
    
    else:
        accuracy = (number_of_hits / number_of_types) * 100
        average_hit_duration = sum(type_hit_average_duration) / len(type_hit_average_duration)
        average_miss_duration = sum(type_miss_average_duration) / len(type_miss_average_duration)
        
    average_type_duration = sum(type_average_duration) / len(type_average_duration)

    #Test Report Dictionary
    test_report = {
        'accuracy': accuracy,
        'inputs': inputs,
        'number_of_hits': number_of_hits,
        'number_of_types': number_of_types,
        'test_duration': test_duration,
        'test_end': end_date,
        'test_start': start_date,
        'type_average_duration': average_type_duration,
        'type_hit_average_duration': average_hit_duration,
        'type_miss_average_duration': average_miss_duration
    }

    pprint(test_report)


if __name__ == '__main__':
    main()