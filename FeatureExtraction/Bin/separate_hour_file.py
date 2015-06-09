
import commands
import os

def get_bids_by_times_files():
    '''
    organize data, sorted by hour then second 
    '''
    os.system(''' cat ../../Preprocessing/Results/bids.csv | sort -t, -k11,11n -k6,6n   > ../../FeatureExtraction/Results/bids_hours_group.csv''' )
    pass

def get_small_time_files():
    '''
    split data into small files
    '''
    bidder = ''
    for line in open('../../FeatureExtraction/Results/bids_hours_group.csv'):
        words = line.strip().split(',')
        if not words[10] == bidder:
            bidder = words[10]
            try:
                fout.close()
            except:
                next 
            fout = open('../../FeatureExtraction/Results/Hours/hour_%s.csv' % bidder,'w')
        fout.write(line)
    fout.close()
    pass

def get_information_for_each_hour():
    # read in auction id
    houridlist = []
    lineind = -1
    for line in open('../../Preprocessing/Results/bids_11.csv'):
        lineind += 1
        houridlist.append(eval(line.strip()))
    # process each file
    fout = open('../../FeatureExtraction/Results/hourinformation','w')
    for hourid in houridlist:
       hourinfor = process_hour(hourid) 
       fout.write('%s\n' % (','.join(hourinfor)))
    fout.close()
    pass


def process_hour(hourid):
    bidder = []
    startingtime = 0
    endingtime = 0
    
    lineind = -1
    for line in open('../../FeatureExtraction/Results/Hours/hour_%d.csv' % hourid):
        lineind += 1
        words = line.strip().split(',')
        if lineind == 0:
            startingtime = eval(words[5])
        endingtime = eval(words[5])
        bidder.append(words[1])
    result = [str(hourid),str(startingtime), str(endingtime), str(len(set(bidder))), str(lineind+1)]
    return result
    pass



if __name__ == '__main__':
    get_bids_by_times_files()
    get_small_time_files()
    get_information_for_each_hour()
