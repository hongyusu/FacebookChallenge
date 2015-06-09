
import sys

def form_submission(filename):
  ind = 0
  ind2bidder = {}
  for line in open('../../Preprocessing/Results/train_1.csv'):
    ind2bidder[str(ind)] = line.strip()
    ind += 1
  fout = open(filename + '_format','w')
  fout.write('bidder_id,prediction\n')
  for line in open(filename):
    words = line.strip().split(',')
    fout.write('%s,%s\n' % (ind2bidder[words[0]],words[1]))
  fout.close()
 

if __name__ == '__main__':
  form_submission(sys.argv[1])