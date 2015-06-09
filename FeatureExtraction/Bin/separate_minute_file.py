
import commands
import os

def get_bids_by_times_files():
    '''
    organize data, sorted by minute then second 
    '''
    os.system(''' cat ../../Preprocessing/Results/bids.csv | sort -t, -k10,10n -k6,6n   > ../../FeatureExtraction/Results/bids_minutes_group.csv''' )
    pass

def get_small_time_files():
    '''
    split data into small files
    '''
    bidder = ''
    for line in open('../../FeatureExtraction/Results/bids_minutes_group.csv'):
        words = line.strip().split(',')
        if not words[9] == bidder:
            bidder = words[9]
            try:
                fout.close()
            except:
                next 
            fout = open('../../FeatureExtraction/Results/Minutes/minute_%s.csv' % bidder,'w')
        fout.write(line)
    fout.close()
    pass

def get_information_for_each_minute():
    # read in auction id
    minuteidlist = []
    lineind = -1
    for line in open('../../Preprocessing/Results/bids_10.csv'):
        lineind += 1
        minuteidlist.append(eval(line.strip()))
    # process each file
    fout = open('../../FeatureExtraction/Results/minuteinformation','w')
    for minuteid in minuteidlist:
       minuteinfor = process_minute(minuteid) 
       fout.write('%s\n' % (','.join(minuteinfor)))
    fout.close()
    pass


def process_minute(minuteid):
    bidder = []
    startingtime = 0
    endingtime = 0
    
    lineind = -1
    for line in open('../../FeatureExtraction/Results/Minutes/minute_%d.csv' % minuteid):
        lineind += 1
        words = line.strip().split(',')
        if lineind == 0:
            startingtime = eval(words[5])
        endingtime = eval(words[5])
        bidder.append(words[1])
    result = [str(minuteid),str(startingtime), str(endingtime), str(len(set(bidder))), str(lineind+1)]
    return result
    pass



if __name__ == '__main__':
    get_bids_by_times_files()
    get_small_time_files()
    get_information_for_each_minute()
