from chap_1.day_9.art import logo

bids = {}

bidding_finished = False

while not bidding_finished:
    name = input("What's your name ? ")
    price = int(input("What's your bid ? $ "))
    bids[name] = price
    should_continue = input("Are there other bidders, types YES OR NO ? ").lower()
    if should_continue == "no":
        bidding_finished = True

print(bids)