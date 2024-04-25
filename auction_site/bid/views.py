from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db import connection
from datetime import datetime

def get_item_details(item_id):
    '''
    Returns the end date of the auction as a datetime and the current item price
    '''
    # Connect to the database
    try:
        with connection.cursor() as cursor:
            # Call the stored procedure and pass validated form data
            cursor.callproc('getItemDetails', [int(item_id)])
            results = cursor.fetchone()
        
    except Exception as e:
        # Log the exception for debugging
        # For production, you might want to return a custom error message
        print(f"Error when inserting item: {e}")
    
    END_DATE_INDEX = 5
    ITEM_PRICE_INDEX = 3
    auction_end_date = results[END_DATE_INDEX]
    item_price = int(results[ITEM_PRICE_INDEX])
    return auction_end_date, item_price

def place_bid(item_id, bidder_username, bid_price):
    '''
    Places a bid on an item for the given price
    '''
    try:
        with connection.cursor() as cursor:
            # Call the stored procedure and pass validated form data
            cursor.callproc('placeBid', [int(item_id), int(bid_price), bidder_username])
            results = cursor.fetchone()
            return results[0]   # This is true on success
        
    except Exception as e:
        # Log the exception for debugging
        # For production, you might want to return a custom error message
        print(f"Error when placing bid: {e}")

    # If we make it here, something has gone wrong
    return False


def bid_on_item(request, item_id, bid_price):
    '''
    Allow the user to place a bid on the item corresponding to item id
    '''
    # Ensure the user is logged in
    if 'username' not in request.session:
        return redirect('login')
    
    # Get the username of the user
    bidder_username = request.session['username']

    # Get the end date and current price of the auction
    auction_end_date, current_price = get_item_details(item_id)

    # Reject bid if current time is later than the auction end time
    if (datetime.now() > auction_end_date):
        messages.error(request, 'Bid not accepted: Auction has already expired')
        return redirect(f"/get_items/item/{item_id}/")
    
    # Check to see if bid price is higher than the current price
    if (bid_price <= current_price):
        messages.error(request, 'Bid not accepted: Insufficient bid price')
        return redirect(f"/get_items/item/{item_id}/")
    
    # If bid it otherwise valid, place the bid and refresh the page
    if place_bid(item_id, bidder_username, bid_price):
        messages.success(request, 'Bid placed successfully')
    else:
        messages.error(request, "Bid not accepted: Unknown error, Try again")
    return redirect(f"/get_items/item/{item_id}/")

