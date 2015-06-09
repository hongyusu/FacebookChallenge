
import numpy
import os

def fix_time():
    fout = open('../../Preprocessing/Results/mybids.csv','w')
    lineind = -1
    for line in open('../../Data/bids.csv'):
        lineind += 1
        if lineind == 0:
            continue
        words = line.strip().split(',')
        timeindex = words[5]
        words[5] = str((eval(timeindex)-9631916842105263)/52631578)
        words.append(str((eval(timeindex)-9631916842105263)/52631578/60))
        words.append(str((eval(timeindex)-9631916842105263)/52631578/60/60))
        words.append(str((eval(timeindex)-9631916842105263)/52631578/60/60/24))
        words.append(str((eval(timeindex)-9631916842105263)/52631578/60/60%24))
        fout.write('%s\n' % (','.join(words)))
    fout.close()
    os.system('cat ../../Preprocessing/Results/mybids.csv | sort -t, -k3,3 -k6,6n > tmp; mv tmp ../../Preprocessing/Results/mybids.csv')
    pass

def get_time_interval():
    fout = open('tmp','w')
    auctionname = ''
    items = []
    numbers = []
    for line in open('../../Preprocessing/Results/mybids.csv'):
        words = line.strip().split(',')
        if auctionname == '':
            auctionname = words[2]
        if not auctionname == words[2]:
            # output
            tmpa = numpy.array(numbers[0:(len(numbers)-1)])
            tmpb = numpy.array(numbers[1:len(numbers)])
            numbers = [0] + list(tmpb-tmpa)
            itemind = -1
            for item in items:
                itemind += 1
                fout.write('%s,%d\n' % (item,numbers[itemind]))
            # clear variable
            items = []
            numbers = []
            auctionname = words[2]
        items.append(line.strip())
        numbers.append(eval(words[5]))
    # output
    tmpa = numpy.array(numbers[0:(len(numbers)-1)])
    tmpb = numpy.array(numbers[1:len(numbers)])
    numbers = [0] + list(tmpb-tmpa)
    itemind = -1
    for item in items:
        itemind += 1
        fout.write('%s,%d\n' % (item,numbers[itemind]))
    fout.close()
    os.system('mv tmp ../../Preprocessing/Results/mybids.csv')



def process_train_and_test_files():
    for i in [1,2,3]:
        print i
        os.system(''' cat ../../Data/t*csv | sed /^bidder_id/d | awk -F',' '{print $%d}'|sort|uniq > ../../Preprocessing/Results/train_%d.csv ''' % (i,i))

def process_bid_file():
    for i in [3,4,5,6,7,8,9,10,11,12,13,14]:
        print i
        os.system('''cat ../../Preprocessing/Results/mybids.csv| awk -F',' '{print $%d}'|sort -n|uniq > ../../Preprocessing/Results/bids_%d.csv''' % (i,i))

def map_train_and_test_file():
    bider = {}
    ind = 0
    for line in open('../../Preprocessing/Results/train_1.csv'):
        bider[line.strip()] = ind
        ind += 1
    address = {}
    ind = 0
    for line in open('../../Preprocessing/Results/train_3.csv'):
        address[line.strip()] = ind
        ind += 1
    account = {}
    ind = 0
    for line in open('../../Preprocessing/Results/train_2.csv'):
        account[line.strip()] = ind
        ind += 1
    fout = open('../../Preprocessing/Results/train.csv','w')
    for line in open('../../Data/train.csv'):
        if line.startswith('bidder'):
            continue
        words = line.strip().split(',')
        fout.write('%d,%d,%d,%s\n' % (bider[words[0]],account[words[1]],address[words[2]],words[3]))
    fout.close()
    fout = open('../../Preprocessing/Results/test.csv','w')
    for line in open('../../Data/test.csv'):
        if line.startswith('bidder'):
            continue
        words = line.strip().split(',')
        fout.write('%d,%d,%d\n' % (bider[words[0]],account[words[1]],address[words[2]]))
    fout.close()

def map_bids_file():
    bider = {}
    ind = 0
    for line in open('../../Preprocessing/Results/train_1.csv'):
        bider[line.strip()] = ind
        ind += 1
    auction = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_3.csv'):
        auction[line.strip()] = ind
        ind += 1
    merchandise = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_4.csv'):
        merchandise[line.strip()] = ind
        ind += 1
    device = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_5.csv'):
        device[line.strip()] = ind
        ind += 1
    country = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_7.csv'):
        country[line.strip()] = ind
        ind += 1
    ip = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_8.csv'):
        ip[line.strip()] = ind
        ind += 1
    url = {}
    ind = 0
    for line in open('../../Preprocessing/Results/bids_9.csv'):
        url[line.strip()] = ind
        ind += 1
    fout = open('../../Preprocessing/Results/bids.csv','w')
    for line in open('../../Preprocessing/Results/mybids.csv'):
        if line.startswith('bid_id'):
            continue
        words = line.strip().split(',')
        fout.write('%s,%d,%d,%d,%d,%s,%d,%d,%d,%s\n' % (words[0],bider[words[1]],auction[words[2]],merchandise[words[3]],device[words[4]],words[5],country[words[6]],ip[words[7]],url[words[8]],','.join(words[9:14])))
    fout.close()
             

if __name__ == '__main__':
    #fix_time()
    get_time_interval()
    process_train_and_test_files()
    process_bid_file()
    map_train_and_test_file()
    map_bids_file()

