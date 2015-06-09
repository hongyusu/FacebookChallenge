
import commands
import os

def get_tmp_file():
    '''
    bider
    '''
    os.system(''' cat ../../Preprocessing/Results/bids.csv | sort -t, -k 2,2n  | sed 's/ /,/g' > tmp ''' )

def get_small_files():
    bidder = ''
    for line in open('tmp'):
        words = line.strip().split(',')
        if not words[1] == bidder:
            bidder = words[1]
            try:
                fout.close()
            except:
                next 
            fout = open('../../FeatureExtraction/Results/bids/bids_%s.csv' % bidder,'w')
        fout.write(line)
    fout.close()

            



if __name__ == '__main__':
    get_tmp_file()
    get_small_files()
