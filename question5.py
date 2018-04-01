from common_functions import get_csv_reader
from common_functions import find_second_biggest_sum_in_dict


def run(f):
    result = find_second_biggest_sum_in_dict(sum_ide_users(f))
    print('The most wanted framework to work in is: "' + result['name'].lower().capitalize() +
          '" with a total count of ' + str(result['sum']) + ' users.')


def sum_ide_users(f):
    csv_data = get_csv_reader(f)
    player_counter = {}
    for row in csv_data:
        player_counter.setdefault(row[91], 0)
        player_counter[row[91]] += 1
    return player_counter
