import os

from art import logo

print(logo)

bids = {}
bidding_finished = False


def clear():
    """
    Clears the terminal screen.

    Detects the operating system and uses the appropriate
    command to clear the terminal screen. On Windows, it uses 'cls', and on
    Unix-based systems (including macOS), it uses 'clear'.

    Note: Set the 'TERM' environment variable to 'xterm-256color' to
    avoid a potential exception.

    Example:
    >>> clear()

    :raise OSError: If the 'clear' command execution fails for the OS.
    :raise TerminalError: If the 'TERM' environment variable is not set.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no': ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
