import json

from helpers.AoCHelper import *

inputlines = read_input_lines('day12/input1.txt')

# print(str(sum([sum([i for i in j]) for j in extract_numbers(inputlines)])))


def sumInJson(jsonstring):
    isJson = True
    try:
        json_object = json.loads(str(jsonstring).replace("'", '"'))
    except Exception as e:
        json_object = jsonstring
        isJson = False

    if str(json_object).replace('-','').isdigit():
        return int(json_object)

    elif isinstance(json_object, list):
        return sum([sumInJson(i) for i in json_object])

    elif isinstance(json_object, dict):
        # if 'red' in json_object.values():
        #     return 0
        # else:
        return sum([sumInJson(v) for v in json_object.values()])

    elif not isJson:
        return 0

    res = 0


    for j in json_object:
        # try:
        #     if 'red' in j.values():
        #         continue
        # except:
        #     try:
        #         if json_object[j] == 'red':
        #             continue
        #     except:
        #         something = 0

        res += sumInJson(j)

    return res

# print(sumInJson('["green", [ { "e": "green", "a": 77, "d": {}, "c": "yellow", "h": "red", "b": 144, "g": {}, "f": "orange", "i": "orange" }, 49, [ { "c": { "e": "violet", "a": -44, "d": 115, "c": 117, "h": 194, "b": { "e": -17, "a": 172, "d": "green", "c": 197, "h": 53, "b": 106, "g": "violet", "f": -10 }, "g": "red", "f": "orange" }, "a": -49, "b": [ "violet", "orange", "blue" ] } ], "green" ]]'))
# print(sumInJson('[1,2,3]'))
# print(sumInJson('[1,{"c":"red","b":2},3]'))
# print(sumInJson('{"d":"red","e":[1,2,3,4],"f":5}'))
# print(sumInJson('[1,"red",5]'))

sumOfIntegers = sumInJson(list_to_string(read_input_lines('day12/input1.txt')))

print(sumOfIntegers)