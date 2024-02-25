import json

if __name__ == '__main__':
    f = open('companies.json')
    data = json.load(f)
    for i in data['name']:
        print(i)

    f.close()