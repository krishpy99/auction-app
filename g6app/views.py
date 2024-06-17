import datetime
from django.shortcuts import redirect, render, get_object_or_404
from .models import Users, Auctions, Auctioneditems, Bids
from django.contrib import messages


def testmysql(request):
    user = Users.objects.all()
    context = {
    'userid': user[1].userid,
    'name': user[1].name,
    }
    return render(request, 'home.html', context)

def auctions(request):
    auctions = Auctions.objects.all()

    # Pass the auctions queryset to the template for rendering
    return render(request, 'auctions.html', {'auctions': auctions})

def auction(request, auctionid):
    #auction_items = Auctioneditems.objects.filter(auctionid=auctionid)
    auction_items = Auctioneditems.objects.filter(auctionid=auctionid)
    
    # Initialize an empty list to store the final 2D list
    item_list = []
    print(auction_items)
    # Loop through each auction item
    for item in auction_items:
        print(item.itemid)
        # Retrieve the product name associated with the current auction item
        product_name = item.productid.name
        # Append a sublist with the itemid and product name to the final list

        print(item)
        item_list.append([item.itemid, product_name])

    print(item_list)
    return render(request, 'auction.html', {'auctionid': auctionid, 'item_list': item_list})

def auctionitem(request, itemid):
    auctionitem = get_object_or_404(Auctioneditems, itemid=itemid)
    
    bids = Bids.objects.filter(itemid=itemid)
    return render(request, 'auctionitem.html', {'auctionitem': auctionitem, 'bids': bids})

def placebid(request):
    if request.method == 'POST':
        bid_amount = float(request.POST.get('bid_amount'))
        itemid = request.POST.get('itemid')  # Assuming you have a hidden input field in your form containing the item ID
        
        # Validate bid_amount if necessary
        bids = Bids.objects.filter(itemid=itemid)
        latest_bid = bids.order_by('-bidtimestamp').first()
        
        for bid in bids:
            print(bid.bidid, bid.amount, bid.bidtimestamp)

        if(bid_amount > latest_bid.amount):
            # Get the auction item
            auctionitem = get_object_or_404(Auctioneditems, itemid=itemid)
            user = get_object_or_404(Users, userid=14)
            # Create a new Bid object and save it
            bid = Bids(amount=bid_amount, itemid=auctionitem, bidderid=user, bidtimestamp=datetime.datetime.now()) #change when authentication is done
            bid.save()
            return redirect('auctionitem', itemid=itemid)
     
    # Handle GET requests or invalid form submissions
    messages.warning(request, 'Your bid amount is too low.')
    return redirect('auctionitem', itemid=itemid)