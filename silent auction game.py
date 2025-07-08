import os

print("*****Welcome to the silent auction program*****")

def heighest_bid(bidding_details):
    highest_price=0
    winner=''
    for bidder in bidding_details:
        bidding_price=bidding_details[bidder]
        if bidding_price>highest_price:
            highest_price=bidding_price
            winner=bidder
    print(bidder)
    print(f"highest bidding price: {winner}")

auction_dict={}
end_of_bidding=False
while not end_of_bidding:
    name=input("Enter your name")
    price=int(input("Enter your price"))

    auction_dict[name]=price

    more_data=input(f"any other price,press 'y'for yes and 'n' for no")

    if more_data== 'n':
        heighest_bid(auction_dict)
    elif more_data=='y':
        print('\n'*100)




