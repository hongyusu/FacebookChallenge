


import sys
import os


def process_single_minute_file(minuteid):
  # process one minute: read in all data
  bidderdata = {}
  for line in open('../../FeatureExtraction/Results/Minutes/minute_%s.csv' % minuteid):
    words = line.strip().split(',')
    if not words[1] in bidderdata.keys():
      bidderdata[words[1]] = []
    bidderdata[words[1]].append(line.strip())

  # write minute bidder file 
  for bidder in bidderdata.keys():
    if not os.path.exists('../../FeatureExtraction/Results/MinuteBidder/%s' % minuteid):
      os.mkdir('../../FeatureExtraction/Results/MinuteBidder/%s' % minuteid)
    fout = open('../../FeatureExtraction/Results/MinuteBidder/%s/%s_%s.csv' % (minuteid,minuteid,bidder),'w')
    for line in bidderdata[bidder]:
      fout.write('%s\n' % (line))
    fout.close()
  pass

if __name__ == '__main__':
    process_single_minute_file(sys.argv[1]) 








