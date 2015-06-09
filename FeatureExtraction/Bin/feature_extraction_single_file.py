


import sys
import re

filename = sys.argv[1]

def get_global_feature(n,filename,fout):
  auctionlist = []
  auctions = {}
  if not n in [6,10,11,12,13,14]:
    ind = 0
    for line in open('../../Preprocessing/Results/bids_%d.csv' % n):
      auctionlist.append(str(ind))
      auctions[str(ind)] = 0
      ind += 1
  else:
    for line in open('../../Preprocessing/Results/bids_%d.csv' % n):
      auctionlist.append(line.strip())
      auctions[line.strip()]= 0
  for line in open('../../FeatureExtraction/Results/bids/%s' % filename):
    words = line.strip().split(',')
    auctions[words[n-1]] += 1
  s = ''
  for auction in auctionlist:
    if auctions[auction] > 0:
      if s=='':
        s = '%s:%d' % (auction,auctions[auction])
      else:
        s += ',%s:%d' % (auction,auctions[auction])
  fout.write("%s\n" % s)
  pass

def get_local_auction_feature(filename,fout):
  fout.write('#auction\n')
  auctionnamelist = []
  for line in open('../../FeatureExtraction/Results/auctioninformation'):
    words = line.strip().split(',')
<<<<<<< HEAD
    if eval(words[4]) < 2:
=======
    if eval(words[3]) < 5:
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
      continue
    auctionnamelist.append(words[0])
  # process
  biddername = re.sub('.*_|\..*','',filename)
  for auctionname in auctionnamelist:
    try:
      s = process_single_auction_bidderfile(auctionname,biddername)
      fout.write('%s\n' % s)
    except Exception as err:
      #print err
      fout.write('0,0,0,0,0,0\n')
  pass

def process_single_auction_bidderfile(auctionname,biddername):
  lineind = -1
  merchandiselist = []
  devicelist = []
  countrylist = []
  iplist = []
  urllist = []
  minutelist = []
  hourlist = []
  daylist = []
  intervallist = []
  for line in open('../../FeatureExtraction/Results/AuctionBidder/%s/%s_%s.csv' % (auctionname,auctionname,biddername)):
    lineind += 1
    words = line.strip().split(',')

    merchandiselist.append(words[3])
    devicelist.append(words[4])
    countrylist.append(words[6])
    iplist.append(words[7])
    urllist.append(words[8])
    minutelist.append(words[9])
    hourlist.append(words[10])
    daylist.append(words[11])
    intervallist.append(words[13])

  s = []
  s.append( str(lineind+1) )
  #s.append( str(len(set(merchandiselist))) )
  s.append( str(len(set(devicelist))) )
  s.append( str(len(set(countrylist))) )
  s.append( str(len(set(iplist))) )
  s.append( str(len(set(urllist))) )
  #s.append( str(len(set(minutelist))) )
  #s.append( str(len(set(hourlist))) )
  #s.append( str(len(set(daylist))) )
  s.append( str(len(set(intervallist))) )
  #s.append( '%.2f' % (float(sum(map(int, intervallist))) / len(intervallist)) )
  #print auctionname, biddername,s
  
  return ','.join(s)
  pass


def get_local_hour_feature(filename,fout):
  fout.write('#hour\n')
  hournamelist = []
  for line in open('../../FeatureExtraction/Results/hourinformation'):
    words = line.strip().split(',')
    hournamelist.append(words[0])
  # process
  biddername = re.sub('.*_|\..*','',filename)
  for hourname in hournamelist:
    try:
      s = process_single_hour_bidderfile(hourname,biddername)
      fout.write('%s\n' % s)
    except Exception as err:
      #print err
<<<<<<< HEAD
      fout.write('0,0,0,0,0,0,0\n')
=======
      fout.write('0,0,0,0,0\n')
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
  pass

def process_single_hour_bidderfile(hourname,biddername):
  lineind = -1
<<<<<<< HEAD
  auctionlist = []
=======
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
  merchandiselist = []
  devicelist = []
  countrylist = []
  iplist = []
  urllist = []
  minutelist = []
  hourlist = []
  daylist = []
  intervallist = []
  for line in open('../../FeatureExtraction/Results/HourBidder/%s/%s_%s.csv' % (hourname,hourname,biddername)):
    lineind += 1
    words = line.strip().split(',')

<<<<<<< HEAD
    auctionlist.append(words[2])
=======
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    merchandiselist.append(words[3])
    devicelist.append(words[4])
    countrylist.append(words[6])
    iplist.append(words[7])
    urllist.append(words[8])
    minutelist.append(words[9])
    hourlist.append(words[10])
    daylist.append(words[11])
    intervallist.append(words[13])

  s = []
  s.append( str(lineind+1) )
<<<<<<< HEAD
  s.append( str(len(set(auctionlist))) )
  s.append( str(len(set(merchandiselist))) )
  s.append( str(len(set(devicelist))) )
  s.append( str(len(set(countrylist))) )
  s.append( str(len(set(iplist))) )
  s.append( str(len(set(urllist))) )
  #s.append( str(len(set(minutelist))) )
  #s.append( str(len(set(hourlist))) )
  #s.append( str(len(set(daylist))) )
  #s.append( str(len(set(intervallist))) )
  #s.append( '%.2f' % (float(sum(map(int, intervallist))) / len(intervallist)) )
  #print auctionname, biddername,s
  
  return ','.join(s)
  pass

def get_local_minute_feature(filename,fout):
  fout.write('#minute\n')
  minutenamelist = []
  for line in open('../../FeatureExtraction/Results/minuteinformation'):
    words = line.strip().split(',')
    minutenamelist.append(words[0])
  # process
  biddername = re.sub('.*_|\..*','',filename)
  for minutename in minutenamelist:
    try:
      s = process_single_minute_bidderfile(minutename,biddername)
      fout.write('%s\n' % s)
    except Exception as err:
      #print err
      fout.write('0,0,0,0,0,0,0\n')
  pass

def process_single_minute_bidderfile(minutename,biddername):
  lineind = -1
  auctionlist = []
  merchandiselist = []
  devicelist = []
  countrylist = []
  iplist = []
  urllist = []
  minutelist = []
  hourlist = []
  daylist = []
  intervallist = []
  for line in open('../../FeatureExtraction/Results/MinuteBidder/%s/%s_%s.csv' % (minutename,minutename,biddername)):
    lineind += 1
    words = line.strip().split(',')

    auctionlist.append(words[2])
    merchandiselist.append(words[3])
    devicelist.append(words[4])
    countrylist.append(words[6])
    iplist.append(words[7])
    urllist.append(words[8])
    minutelist.append(words[9])
    hourlist.append(words[10])
    daylist.append(words[11])
    intervallist.append(words[13])

  s = []
  s.append( str(lineind+1) )
  s.append( str(len(set(auctionlist))) )
  s.append( str(len(set(merchandiselist))) )
=======
  #s.append( str(len(set(merchandiselist))) )
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
  s.append( str(len(set(devicelist))) )
  s.append( str(len(set(countrylist))) )
  s.append( str(len(set(iplist))) )
  s.append( str(len(set(urllist))) )
  #s.append( str(len(set(minutelist))) )
  #s.append( str(len(set(hourlist))) )
  #s.append( str(len(set(daylist))) )
  #s.append( str(len(set(intervallist))) )
  #s.append( '%.2f' % (float(sum(map(int, intervallist))) / len(intervallist)) )
  #print auctionname, biddername,s
  
  return ','.join(s)
  pass


if __name__ == '__main__':
  filename = sys.argv[1]
  fout = open('../../FeatureExtraction/Results/BidderFeatures/%s' % filename, 'w')
  # global feature
<<<<<<< HEAD
  #for featureind in [3,4,5,6,7,8,9,10,11,12,13,14]:
  for featureind in [3,4,5,6,7,8,9]:
=======
  for featureind in [3,4,5,6,7,8,9,10,11,12,13,14]:
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    get_global_feature(featureind,filename,fout)
  # local feature
  get_local_auction_feature(filename,fout)
  get_local_hour_feature(filename,fout)
<<<<<<< HEAD
  get_local_minute_feature(filename,fout)
=======
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
  fout.close()








