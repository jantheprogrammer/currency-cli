import json
import requests


def get_rates():
    # get currency rates from api
    try:
        payload = requests.get(
            'https://api.ratesapi.io/api/latest', params={'base': 'CZK'})

        # parse response to json
        data = json.loads(payload.text)

        # save lastest rates to file
        save_rates(data)
    except:
        try:
            # if there is no internet connection
            # program will try to load rates from file
            with open('rates.json', 'r+') as f:
                data = json.load(f)
        except:
            print('Rates could not be loaded!')

    return data


def save_rates(data):
    with open('rates.json', 'w+') as file:
        # jump to beggining of the file
        file.seek(0)
        # put data into the file
        json.dump(data, file, indent=2, sort_keys=True)
        # if new data are shorter than previous one
        # truncate overlapping data
        file.truncate()


def print_currencies(rates):
    # number of currencies listed in one row
    CURR_IN_ROW = 10
    # dictionary of currencies
    dict_of_currencies = rates['rates'].keys()
    # retyped list of currencies from dict.
    list_of_currencies = list(dict_of_currencies)
    lenght = len(list_of_currencies)

    # how many rows is going to be displayed
    display = CURR_IN_ROW
    # loop for displaying currency options
    for i in range(0, lenght, CURR_IN_ROW):
        # printing list without brackets and with coma sepparator
        print(*list_of_currencies[i:display], sep=', ')
        # next iteration is going to show next part of currencies
        display += CURR_IN_ROW


def transfer(data, amt, cur1, cur2):
    rates = data['rates']

    if cur1 == cur2:
        rate = 1
    else:
        rate = rates[cur2]/rates[cur1]

    result = amt * rate

    print(' /' + '-' * 46 + '\\ ')
    print('/' + '-' * 48 + '\\')
    print(' ' * 4 + f'For {amt} {cur1} you get {result} {cur2}')
    print('\\' + '-' * 48 + '/')
    print(' \\' + '-' * 46 + '/ ')


def get_decision(desicion):
    yes_decisions = ['y', 'yes', 'true', '1']
    if desicion in yes_decisions:
        return True
    else:
        return False
