

# name, num_of_crooks, crooks_power, money, territory, mafia_number
from mafiaClass import Mafia
import random

mafia_1 = Mafia("Ndraghy", 19, 18, 100_000, 4.5, 1)
mafia_2 = Mafia("Maldora", 24, 14, 100_000, 4.6, 2)
mafia_3 = Mafia("Fuoky", 21, 13, 100_000, 5.7, 3)
mafia_4 = Mafia("Ragdolls", 10, 34, 100_000, 3.2, 4)
mafia_5 = Mafia("Braks", 40, 7, 100_000, 2.8, 5)
new_maf = Mafia("Ndraffffghy", 129, 128, 1_200_000, 4.5, 6)

# list of existing mafias
list_of_mafia_objects = [mafia_1, mafia_2, mafia_3, mafia_4, mafia_5, new_maf]
# list of mafias in play
playing_mafias_list = [mafia_1, mafia_2, mafia_3, mafia_4, mafia_5]


# NOTE: list_of_mafia_objects = global mafias list = "total" list
# NOTE: playing_mafias_list = playing mafias list = "playing" list

# translates "playing" or "total" in either the list of mafias in play
# or the full list of existing mafias
def check_if_playing_list_or_total(string):
    if string.casefold() == "playing":
        return playing_mafias_list
    if string.casefold() == "total":
        return list_of_mafia_objects


# for testing, prints all mafia names from the global mafias list
def test_print_all_mafias_from_list():
    for x in list_of_mafia_objects:
        print(x.name)


# returns the mafia object that has the player tag (is_player = True)
def get_players_mafia():
    for x in playing_mafias_list:
        if x.is_player:
            return x


# simply returns the highest mafia number value from the global mafias list
def check_highest_mafia_number_in_mafia_list():
    highest = 0
    for x in list_of_mafia_objects:
        check = getattr(x, Mafia.define_stat("number"))
        if check > 0:
            highest = check
    return highest


# sets a mafia object's player tag (is_player) to true, given a mafia number
def set_mafia_as_player_by_mafia_no(num):
    check_element_by_number_attribute(num, playing_mafias_list).is_player = True


# asks which mafia the player will choose, selected by its number
def input_prompt_for_mafia_selection():
    num = input("Select a mafia No: ")
    set_mafia_as_player_by_mafia_no(num)


# returns the full info about the player's mafia
# IMPORTANT: remember to print the information
def see_players_mafia_info():
    return get_players_mafia().full_details()


# adds a new mafia to the global mafias list with info given as input
# uses check_highest_mafia_number_in_mafia_list() to automatically assign the mafia number
def add_new_mafia_to_list():
    name = input("enter name: ")
    num_of_crooks = int(input("enter number of crooks: "))
    crooks_power = int(input("enter crooks power: "))
    money = float(input("enter money: "))
    territory = float(input("enter territory: "))
    mafia_number = check_highest_mafia_number_in_mafia_list() + 1
    new_obj = Mafia(name,
                    int(num_of_crooks),
                    int(crooks_power),
                    int(money),
                    float(territory),
                    int(mafia_number))
    list_of_mafia_objects.append(new_obj)


# prints out a detailed list of info about all the mafias in a given list
# the given list can be either the "total" one or the "playing" one
# specify the interested list as a string using those two keywords
def see_full_details_of_all_mafias_in_list(string):
    lst = check_if_playing_list_or_total(string)
    for x in lst:
        print(x.full_details())


# given a mafia number, it will return a mafia object associated with it
# from a given list ("total" or "playing")
def check_element_by_number_attribute(num, lst):
    for x in lst:
        if int(num) == getattr(x, Mafia.define_stat("number")):
            return x


# takes in a given list ("total" or "playing") and returns a list with all the
# available mafia numbers
def numbers_list(string):
    new_list = []
    for x in check_if_playing_list_or_total(string):
        new_list.append(x.mafia_number)
    return new_list


# add a mafia object from the "total" list to the "playing" list
# takes in an integer that will be viewed as a mafia number
# the mafia object associated with the mafia number entered
# will be added
def add_mafia_to_playing_from_mafia_list_by_number(num):
    mafia_to_add = check_element_by_number_attribute(int(num), list_of_mafia_objects)
    mafia_list_numbers = numbers_list("playing")
    if mafia_to_add not in mafia_list_numbers:
        playing_mafias_list.append(mafia_to_add)


# checks weather there's any "eliminated" tag (is_eliminated = True) in the
# playing list and removes it from that list
def remove_eliminated_mafias_from_playing_list():
    for x in check_if_playing_list_or_total("playing"):
        if getattr(x, Mafia.define_stat("eliminated")):
            check_if_playing_list_or_total("playing").remove(x)


# apply the comprehensive_yearly_process() function to all mafia objects in the
# "playing" list
def apply_comprehensive_yearly_process_to_all_mafias_in_list():
    for x in check_if_playing_list_or_total("playing"):
        x.comprehensive_yearly_process()
        if x.money <= 0 or x.num_of_crooks <= 0 or x.territory <= 0:
            x.is_eliminated = True
        remove_eliminated_mafias_from_playing_list()


# get a list with every stat instance from the list of mafias currently playing
# takes in a parameter that will be translated into an attribute of the mafia object
def get_stat_list_from_mafia_list(string):
    stat_list = []
    for x in check_if_playing_list_or_total("playing"):
        stat_list.append(getattr(x, Mafia.define_stat(string)))
    return stat_list


# prints out the list gotten from the get_stat_list_from_mafia_list function
# it takes in the attribute that will be printed out
def print_stat_list(string):
    for x in get_stat_list_from_mafia_list(string):
        print(str(x))


# generates a random number between 0.35  and 1.05, with the odds
# falling in the middle rather than being completely random
# this expression will be used for the num_of_crooks yearly growth
def make_random_zero35():
    return ((random.random() + 1)
            * (random.random() + 1)
            + (random.random() + 1)) \
           * 0.175


# testing proper functionality of the make_random_zero35 function
# using 1 as an example as it should be very unlikely to get >=1

def whzero():
    i = 1
    while i < 100000:
        rand_zero35 = make_random_zero35()
        print(rand_zero35)
        if rand_zero35 >= 1:
            print("ONE ONEEEEEEEEEEEEEEEEEEE " + str(i))
            i = 100000
        i += 1


# whzero()


# data sample using the zero35 function 5000 times
# // 5 result >= 1
# // 113 result >= 0.9 && a < 1
# // 543 result >= 0.8 && a < 0.9
# // 1077 result >= 0.7 && a < 0.8
# // 1528 result >= 0.6 && a < 0.7
# // 1322 result >= 0.5 && a < 0.6
# // 395 result >= 0.4 && a < 0.5
# // 17 result >= 0.2 && a < 0.4


# this expression will be used for the crooks_power yearly growth
def random_number_with_external_variable(f):
    return ((((random.random() + 1) * 0.1)
             * ((random.random() + 1) * 0.1))
            + ((random.random() + 1) * 0.1)
            * (((random.random() + 1) * 0.5)
               * f))


# 0.646875 should be the mid-range when f is 5
# 1.29375 should be the mid-range when f is 10
# 2.5875 should be the mid-range when f is 20
# as f increases the result fluctuates more and more
# print(random_power_increase_based_on_territory(5))
# print(random_power_increase_based_on_territory(10))
# print(random_power_increase_based_on_territory(20))

# the territory parameter should be passed
def formula_money_gain(f):
    return (f * 70_000) * ((random.random() + random.randrange(2, 4)) * 0.7)


# def formula_attack_power_gain():

def test_add_new_mafia_to_list():
    name = "cf"
    num_of_crooks = 10
    crooks_power = 10
    money = 100_000
    territory = 10
    mafia_number = check_highest_mafia_number_in_mafia_list() + 1
    new_obj = Mafia(name,
                    int(num_of_crooks),
                    int(crooks_power),
                    int(money),
                    float(territory),
                    int(mafia_number))
    list_of_mafia_objects.append(new_obj)


''' List of all usable functions: 
get_players_mafia()
see_players_mafia_info()
add_new_mafia_to_list()
see_full_details_of_all_mafias_in_list(string)
check_element_by_number_attribute(num, lst)
numbers_list(string)
add_mafia_to_playing_from_mafia_list_by_number(num)
remove_eliminated_mafias_from_playing_list()
apply_comprehensive_yearly_process_to_all_mafias_in_list()
print_stat_list(string)

Mafia methods:
change_stat(self, number, stat_to_change, operation)
send_crooks_to_war(self, number)
update_total_power(self)
update_costs(self)
cost_processing(self)
increase_crooks_numbers_yearly_rate(self)
increase_crooks_power_yearly_rate(self)
increase_money_yearly_rate(self)
comprehensive_yearly_process(self)
full_details(self)
'''
'''
see_full_details_of_all_mafias_in_list("total")
test_add_new_mafia_to_list()
see_full_details_of_all_mafias_in_list("total")
add_mafia_to_playing_from_mafia_list_by_number(7)
see_full_details_of_all_mafias_in_list("playing")
input_prompt_for_mafia_selection()
print(see_players_mafia_info())
mafia_1.change_stat(100_000, "crooks", "subtract")
'''
