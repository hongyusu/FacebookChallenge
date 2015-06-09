
import sys
import numpy
import os


class prettyfloat(float):
  def __repr__(self):
    return "%0.2f" % self

                    
def process_kth_feature_summary(line,lineind):
  words = line.strip().split(',')
  res = []
  name = []
  for word in words:
    [ind,num] = word.split(':')
    res.append(eval(num))
    name.append(eval(ind))
  if lineind == 0:
    s = '%d,%d,%d,%d,%.2f'  % (sum(res),len(res),min(res),max(res),float(sum(res))/len(res))
  else:
    s = ',%d,%d,%d,%.2f'    % (len(res),min(res),max(res),float(sum(res))/len(res))
    if lineind == 11:
      s += ',%d,%d,%d,%.2f' % (len(name),min(name),max(name),float(sum(list(numpy.array(res)*numpy.array(name))))/sum(res)) 
  return s

def get_feature_matrix(filename):
  fout = open('../../FeatureExtraction/Results/%s.csv' % filename,'w')
  for line in open('../../Preprocessing/Results/%s.csv' % filename):
    if filename == 'train':
      [bidder,account,address,label] = line.strip().split(',')
    if filename == 'test':
      [bidder,account,address] = line.strip().split(',')
    try:
      # generate feature
      s = ''
      lineind = -1
      auctionind = 0
      auctionstatistics = numpy.array([0,0,0,0,0,0])
<<<<<<< HEAD
      hourind = 0
      hourstatistics = numpy.array([0,0,0,0,0,0,0])
      minuteind = 0
      minutestatistics = numpy.array([0,0,0,0,0,0,0])
      featuretype = ''
      cinformation = ''
      for line in open('../../FeatureExtraction/Results/BidderFeatures/bids_%s.csv' % bidder):
        if line.startswith('#'):
          featuretype = line.strip()
=======
      timeind = 0
      timestatistics = numpy.array([0,0,0,0,0])
      timefeature = 0
      for line in open('../../FeatureExtraction/Results/BidderFeatures/bids_%s.csv' % bidder):
        if line.startswith('#auction'):
          timefeature = 0
          continue
        if line.startswith('#hour'):
          timefeature = 1
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
          continue
        lineind += 1
        if lineind > 1000000:
          break
        if lineind in [-1,-2]:
          continue
<<<<<<< HEAD
        if lineind >= 7 and featuretype == '#auction':
=======
        if lineind >= 12 and timefeature == 0:
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
          words = line.strip().split(',')
          if not eval(words[0]) == 0:
            auctionind += 1
            auctionstatistics += numpy.array(map(float,words))
<<<<<<< HEAD
          continue
        if lineind >= 7 and featuretype == '#hour':
          words = line.strip().split(',')
          if not eval(words[0]) == 0:
            hourind += 1
            hourstatistics += numpy.array(map(float,words))
          continue
        if lineind >= 7 and featuretype == '#minute':
          words = line.strip().split(',')
          if not eval(words[0]) == 0:
            minuteind += 1
            minutestatistics += numpy.array(map(float,words))
          continue
        s += process_kth_feature_summary(line,lineind)
        if lineind in [2,4]:
          cdata = {}
          cnamelist = []
          lind = -1
          for cline in open('../../Preprocessing/Results/bids_%d.csv' % (lineind+3) ):
            lind += 1
            cdata[lind] = 0
            cnamelist.append(lind)
          for words in line.strip().split(','):
            [cname,ccount] = words.split(':')
            cdata[eval(cname)] = eval(ccount)
          for cname in cnamelist:
            cinformation += ',%d' % cdata[cname]
      if auctionind == 0:
        auctionind = 1
      if hourind == 0:
        hourind = 1
      if minuteind == 0:
        minuteind = 1
      averageauctionstatistics = ['%.2f' % i for i in list(auctionstatistics/float(auctionind))]
      auctionstatistics        = map(str,list(auctionstatistics))
      averagehourstatistics    = ['%.2f' % i for i in list(hourstatistics/float(hourind))]
      averageminutestatistics  = ['%.2f' % i for i in list(minutestatistics/float(minuteind))]
      s += ',%s,%s,%s,%s' % ( auctionstatistics[0], ','.join(averageauctionstatistics), ','.join(averagehourstatistics), ','.join(averageminutestatistics))
      s += '%s' % cinformation
=======
            #print words,auctionstatistics
          #s += ','
          #s += line.strip()
          continue
        if lineind >= 12 and timefeature ==1:
          words = line.strip().split(',')
          if not eval(words[0]) == 0:
            timeind += 1
            timestatistics += numpy.array(map(float,words))
            #print bidder,words,timestatistics 
          continue
        s += process_kth_feature_summary(line,lineind)
      if auctionind == 0:
        auctionind = 1
      if timeind == 0:
        timeind = 1
      averageauctionstatistics = ['%.2f' % i for i in list(auctionstatistics/float(auctionind))]
      auctionstatistics = map(str,list(auctionstatistics))
      averagetimestatistics = ['%.2f' % i for i in list(timestatistics/float(timeind))]
      s += ',%s,%s,%s' % ( auctionstatistics[0], ','.join(averageauctionstatistics), ','.join(averagetimestatistics))
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    except Exception as msg:
      print msg,bidder
      s = '0' 
    if filename == 'train':
      fout.write("%s,%s,%s\n" % (bidder,s,label))
    if filename == 'test':
      fout.write("%s,%s\n" % (bidder,s))
  fout.close()
  pass

def fix_feature_matrix(filename):
  # fix
  fout = open('../../FeatureExtraction/Results/%s.csv.tmp' % filename,'w')
  lineind = -1
  s=''
  featurelen = 0
  if filename == 'train':
    featurelen_fix = 3
  if filename == 'test':
    featurelen_fix = 2
  for line in open('../../FeatureExtraction/Results/%s.csv' % filename):
    lineind += 1
    words = line.strip().split(',')
    if lineind == 0:
      featurelen = len(words)-featurelen_fix+1
      fout.write(line)
    else:
      if len(words) > featurelen_fix:
        fout.write(line)
      else:
        if filename == 'train':
          fout.write( '%s%s,%s\n' %(words[0],',0'*featurelen,words[2]))
        if filename == 'test':
          fout.write( '%s%s\n' %(words[0],',0'*featurelen))
  fout.close()
  os.system('mv ../../FeatureExtraction/Results/%s.csv.tmp ../../FeatureExtraction/Results/%s.csv' % (filename,filename))
  pass


if __name__ == '__main__':
  get_feature_matrix('train')
  fix_feature_matrix('train')
  get_feature_matrix('test')
  fix_feature_matrix('test')
