from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db import connection
from datetime import datetime
from .forms import UserForm

def get_item_details(item_id):
    '''
    Returns the end date of the auction as a datetime and the current item price
    '''
    raise NotImplementedError()

def get_bid_price(request):
    '''
    Returns the price that the user bid for the item
    '''
    raise NotImplementedError()

def place_bid(item_id, bidder_username, bid_price):
    '''
    Places a bid on an item for the given price
    '''
    raise NotImplementedError()

def bid_on_item(request, item_id):
    '''
    Allow the user to place a bid on the item corresponding to item id
    '''
    # Ensure the user is logged in
    if 'username' not in request.session:
        return redirect('login')
    
    # Get the username of the user
    bidder_username = request.session['username']

    # Get the price the user is bidding
    bid_price = get_bid_price(request)

    # Get the end date and current price of the auction
    auction_end_date, current_price = get_item_details(item_id)

    # Reject bid if current time is later than the auction end time
    if (datetime.now() > auction_end_date):
        messages.error(request, 'Bid not accepted: Auction has already expired')
        return redirect(f"get_items/{item_id}/")
    
    # Check to see if bid price is higher than the current price
    if (bid_price <= current_price):
        messages.error(request, 'Bid not accepted: Insufficient bid price')
        return redirect(f"get_items/{item_id}/")
    
    # If bid it otherwise valid, place the bid and refresh the page
    if place_bid(item_id, bidder_username, bid_price):
        messages.success(request, 'Bid placed successfully')
    else:
        messages.error(request, "Bid not accepted: Unknown error, Try again")
    return redirect(f"get_items/{item_id}/")

