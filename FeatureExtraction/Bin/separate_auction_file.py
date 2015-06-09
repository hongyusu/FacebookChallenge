
import commands
import os

def get_bids_by_auctions_files():
    '''
    organize data, sorted by auction then time 
    '''
    os.system(''' cat ../../Preprocessing/Results/bids.csv | sort -t, -k3,3n -k6,6n   > ../../FeatureExtraction/Results/bids_auction_group.csv''' )
    pass

def get_small_auction_files():
    '''
    split data into small files
    '''
    bidder = ''
    for line in open('../../FeatureExtraction/Results/bids_auction_group.csv'):
        words = line.strip().split(',')
        if not words[2] == bidder:
            bidder = words[2]
            try:
                fout.close()
            except:
                next 
            fout = open('../../FeatureExtraction/Results/Auctions/auction_%s.csv' % bidder,'w')
        fout.write(line)
    fout.close()
    pass

def get_information_for_each_auction():
    # read in auction id
    auctionidlist = []
    lineind = -1
    for line in open('../../Preprocessing/Results/bids_3.csv'):
        lineind += 1
        auctionidlist.append(lineind)
    # process each file
    fout = open('../../FeatureExtraction/Results/auctioninformation','w')
    for auctionid in auctionidlist:
       auctioninfor = process_auction(auctionid) 
       fout.write('%s\n' % (','.join(auctioninfor)))
    fout.close()
    pass


def process_auction(auctionid):
    bidder = []
    startingtime = 0
    endingtime = 0
    
    lineind = -1
    for line in open('../../FeatureExtraction/Results/Auctions/auction_%d.csv' % auctionid):
        lineind += 1
        words = line.strip().split(',')
        if lineind == 0:
            startingtime = eval(words[5])
        endingtime = eval(words[5])
        bidder.append(words[1])
<<<<<<< HEAD
    result = [str(auctionid),str(startingtime), str(endingtime), str(len(set(bidder))), str(lineind+1)]
=======
    result = [str(auctionid),str(startingtime), str(endingtime), str(len(set(bidder))), str(lineind)]
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    return result
    pass



if __name__ == '__main__':
    get_bids_by_auctions_files()
    get_small_auction_files()
    get_information_for_each_auction()
