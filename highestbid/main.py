from art import logo

print(logo)

bidders_dict = {}

end_budding = False


def find_highest_bidder(bidders_dict):
    highest_bid = 0
    highest_bidder_name = ""
    for bidder in bidders_dict:
        if bidders_dict[bidder] > highest_bid:
            highest_bid = bidders_dict[bidder]
            highest_bidder_name=bidder
    print(f"The highest bidder is {highest_bidder_name} with {bidders_dict[highest_bidder_name]}")


while not end_budding:

    username = input("Enter your name\n")
    amount_to_bid = int(input("Enter the amount that you would like to bid\n"))

    bidders_dict[username] = amount_to_bid

    continue_next = input("Do u want to continue?Enter yes or no")
    if continue_next == "no":
        end_budding = True
        find_highest_bidder(bidders_dict)
    elif continue_next == "yes":
        continue
    else:
        print("Invalid option:Try again")

