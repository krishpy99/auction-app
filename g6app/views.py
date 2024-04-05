from django.shortcuts import render, get_object_or_404
from .models import Users, Auctions, Auctioneditems, Bids
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
    # for item in auction_items:
    #     print(item.itemid)
    #     # Retrieve the product name associated with the current auction item
    #     product_name = "asdf"#item.productid.name
    #     # Append a sublist with the itemid and product name to the final list

    #     print(item)
    #     item_list.append([item.itemid, product_name])

    print(item_list)
    return render(request, 'auction.html', {'auctionid': auctionid, 'item_list': item_list})

def auctionitem(request, itemid):
    auctionitem = get_object_or_404(Auctioneditems, itemid=itemid)
    
    bids = Bids.objects.filter(itemid=itemid)
    return render(request, 'auctionitem.html', {'auctionitem': auctionitem, 'bids': bids})