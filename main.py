import json
from utils import get_rates, print_currencies, transfer, get_decision
import os

running = True

while running:
    # clear cosole before every 'run'
    os.system('cls' if os.name == 'nt' else 'clear')

    rates = get_rates()

    # get list of currencies
    print_currencies(rates)

    cur1 = input('Select your base currency: ')
    cur1 = cur1.upper()

    amt_cur1 = int(input('How much do you want to transfer: '))

    cur2 = input('Select second currency: ')
    cur2 = cur2.upper()

    transfer(rates, amt_cur1, cur1, cur2)

    decision = input('Do you want to continue [y/N]? ').lower()
    running = get_decision(decision)
