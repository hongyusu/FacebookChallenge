


import sys
import os


def process_single_auction_file(auctionid):
  # process one auction: read in all data
  bidderdata = {}
  for line in open('../../FeatureExtraction/Results/Auctions/auction_%s.csv' % auctionid):
    words = line.strip().split(',')
    if not words[1] in bidderdata.keys():
      bidderdata[words[1]] = []
    bidderdata[words[1]].append(line.strip())

  # write auction bidder file 
  for bidder in bidderdata.keys():
    if not os.path.exists('../../FeatureExtraction/Results/AuctionBidder/%s' % auctionid):
      os.mkdir('../../FeatureExtraction/Results/AuctionBidder/%s' % auctionid)
    fout = open('../../FeatureExtraction/Results/AuctionBidder/%s/%s_%s.csv' % (auctionid,auctionid,bidder),'w')
    for line in bidderdata[bidder]:
      fout.write('%s\n' % (line))
    fout.close()
  pass

if __name__ == '__main__':
    process_single_auction_file(sys.argv[1]) 








