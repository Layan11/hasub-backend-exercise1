import json


def how_many_workers(json_data):
    # stopping rule
    if 'subordinates' not in json_data.keys():
        return 1
    sum = 0
    for subordinate in json_data['subordinates']:
        sum += how_many_workers(subordinate)
    return 1 + sum


def get_cto_data_json(json_data):
    if json_data['name'] == 'CTO':
        return json_data
    if 'subordinates' in json_data.keys():
        for subordinates in json_data['subordinates']:
            res = get_cto_data_json(subordinates)
            if res:
                return res


def how_many_under_cto(json_data):
    # get the CTO json data
    cto_json_data = get_cto_data_json(json_data)
    num_workers = how_many_workers(cto_json_data)
    return num_workers - 1


def how_many_developers(json_data):
    is_developer = int('developer' in json_data['name'].lower())
    # stopping rule
    if 'subordinates' not in json_data.keys():
        return is_developer
    sum = 0
    for sub in json_data['subordinates']:
        sum += how_many_developers(sub)

    return is_developer + sum


def how_many_departments(json_data):
    if 'subordinates' not in json_data.keys():
        return 0

    sum = 0
    for sub in json_data['subordinates']:
        sum += how_many_departments(sub)

    return 1 + sum


if __name__ == '__main__':
    with open('companies.json') as f:
        data = json.load(f)
        for organization in data:
            num_workers = how_many_workers(data[organization])
            cto_workers = how_many_under_cto(data[organization])
            developers_num = how_many_developers(data[organization])
            departments_num = how_many_departments(data[organization])
            print("The number of workers is: " + str(num_workers))
            print("The number of workers under the CTO is: " + str(cto_workers))
            print("The number of developers is: " + str(developers_num))
            print("The number of departments is: " + str(departments_num))