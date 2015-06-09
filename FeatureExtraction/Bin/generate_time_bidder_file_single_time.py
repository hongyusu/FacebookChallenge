


import sys
import os


def process_single_hour_file(hourid):
  # process one hour: read in all data
  bidderdata = {}
  for line in open('../../FeatureExtraction/Results/Hours/hour_%s.csv' % hourid):
    words = line.strip().split(',')
    if not words[1] in bidderdata.keys():
      bidderdata[words[1]] = []
    bidderdata[words[1]].append(line.strip())

  # write hour bidder file 
  for bidder in bidderdata.keys():
    if not os.path.exists('../../FeatureExtraction/Results/HourBidder/%s' % hourid):
      os.mkdir('../../FeatureExtraction/Results/HourBidder/%s' % hourid)
    fout = open('../../FeatureExtraction/Results/HourBidder/%s/%s_%s.csv' % (hourid,hourid,bidder),'w')
    for line in bidderdata[bidder]:
      fout.write('%s\n' % (line))
    fout.close()
  pass

if __name__ == '__main__':
    process_single_hour_file(sys.argv[1]) 








