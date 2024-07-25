#!/usr/bin/python3
from art import logo
import os
from ast import literal_eval
print(logo)


def find_highest_bidder(bidding_record):
    # find the highest value from the dictionary.
    if not bidding_record:
        return None
    highest_bid = max(bidding_record, key=bidding_record.get)
    return highest_bid, bidding_record[highest_bid]


def clear():
    # clear the console wind.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    bids = {}
    bidding_finished = False
    while not bidding_finished:

        name = input('Enter your name?')
        price = literal_eval(input('Enter your bid amount?'))

        bids[name] = price
        should_continue = input(
            "Are there any bidders? Type 'Yes' or 'No ").lower()
        if should_continue == 'no':
            bidding_finished = True
        elif should_continue == 'yes':
            clear()

    print("The Winner is: ", find_highest_bidder(bids))


main()
