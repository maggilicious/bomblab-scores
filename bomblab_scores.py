
def list_file_contents(file_obj):
    das_list = []
    for line in file_obj:
        das_list.append(line.split())
    return das_list

def get_important_info(a_list):
    good_dict = {}
    bomb_num = 1
    phases_defused = 6
    explosions = 7
    for item in a_list:
        good_dict[item[bomb_num]] = (item[phases_defused], item[explosions])
    return good_dict

def count_phases(a_dict):
    phases_0_count = 0
    phases_1_count = 0
    phases_2_count = 0
    phases_3_count = 0
    phases_4_count = 0
    phases_5_count = 0
    phases_6_count = 0
    secret_phase_count = 0

    for value in a_dict.values():
        if value[0] == "7":
            secret_phase_count += 1
        elif value[0] == "6":
            phases_6_count += 1
        elif value[0] == "5":
            phases_5_count += 1
        elif value[0] == "4":
            phases_4_count += 1
        elif value[0] == "3":
            phases_3_count += 1
        elif value[0] == "2":
            phases_2_count += 1
        elif value[0] == "1":
            phases_1_count += 1
        elif value[0] == "0":
            phases_0_count += 1
    return (secret_phase_count, phases_6_count, phases_5_count, phases_4_count, phases_3_count, phases_2_count, phases_1_count, phases_0_count)

def count_bombs(a_dict):
    bombs_sum = 0
    for value in a_dict.values():
        try:
            bombs_sum += int(value[1])
        except ValueError:
            continue
    return bombs_sum

def display_nicely(a_tuple, bombs_total):
    print("Scoreboard summed up:\n{} total bombs exploded.\n--------------------".format(bombs_total))
    print("{} people finished Secret phase.\n{} people finished phase 6.\n{} people finished phase 5.\
        \n{} people finished phase 4.\n{} people finished phase 3.\n{} people finished phase 2.\
        \n{} people finished phase 1.\n{} people finished no phases.".format(a_tuple[0], a_tuple[1], a_tuple[2], \
        a_tuple[3], a_tuple[4], a_tuple[5], a_tuple[6], a_tuple[7],))

def wall_of_shame(a_dict):
    print("WALL OF SHAME! ( ͡° ͜ʖ ͡°)╭∩╮\n----------------------------")
    for key, value in a_dict.items():
        try:
            if (int(value[1]) >= 5):
                print("{} defused {} phases and exploded {} times.".format(key, value[0], value[1]))
        except ValueError:
            continue



# MAIN #
file_stream = open("blab_scoreboard.txt", "r")

whole_list = list_file_contents(file_stream)
#print(whole_list)

nice_info_dict = get_important_info(whole_list)
#print(nice_info_dict)

phases_tuple = count_phases(nice_info_dict)
#print(phases_tuple)
print("\n")
total_bombs = count_bombs(nice_info_dict)
#print(total_bombs)

display_nicely(phases_tuple, total_bombs)
print("\n")
wall_of_shame(nice_info_dict)