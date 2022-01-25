import sys
import json

file_1 = open(sys.argv[1], 'r', encoding='UTF-8')
file_2 = open(sys.argv[2], 'r', encoding='UTF-8')


def find_key(list_dict, key, key_value, value_value):
    for dictionary in list_dict:
        if dictionary[key] == key_value:
            dictionary['value'] = value_value
        elif 'values' in dictionary:
            find_key(dictionary['values'], key, key_value, value_value)


with open('report.json', 'w') as f_result:
    tests = json.load(file_1)['tests']
    values = json.load(file_2)['values']
    file_1.close()
    file_2.close()
    for value in values:
        find_key(tests, 'id', value['id'], value['value'])
    json.dump(tests, f_result, indent=4)
