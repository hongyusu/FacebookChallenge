




# Wrapper function to run developed Random Spanning Tree Approximation algorithm parallelly on interactive cluster, for the purpose of multiple parameters and datasets.
# The script uses Python thread and queue package.
# Implement worker class and queuing system.
# The framework looks at each parameter combination as a job and pools all job_queue in a queue.
# It generates a group of workers (computing nodes). 
# Each worker will always take and process the first job from the queue.
# In case that job is not completed by the worker, it will be push back to the queue, and will be processed later on.


import math
import re
import Queue
from threading import ThreadError
from threading import Thread
import os
import sys
import commands
sys.path.append('/cs/taatto/group/urenzyme/workspace/netscripts/')
from get_free_nodes import get_free_nodes
import multiprocessing
import time
import logging
import random
logging.basicConfig(format='%(asctime)s %(filename)s %(funcName)s %(levelname)s:%(message)s', level=logging.INFO)


job_queue = Queue.PriorityQueue()

# Worker class
# job is a tuple of parameters
class Worker(Thread):
  def __init__(self, job_queue, node):
    Thread.__init__(self)
    self.job_queue  = job_queue
    self.node = node
    self.penalty = 0 # penalty parameter which prevents computing node with low computational resources getting job_queue from job queue
    pass # def
  def run(self):
    all_done = 0
    while not all_done:
      try:
        time.sleep(random.randint(5000,6000) / 1000.0)  # get some rest :-)
        time.sleep(self.penalty*120) # bad worker will rest more
        job = self.job_queue.get(0)
        add_penalty = singleJob(self.node, job)
        self.penalty += add_penalty
        if self.penalty < 0:
          self.penalty = 0
      except Queue.Empty:
        all_done = 1
      pass # while
    pass # def
  pass # class


global_rundir = ''

# function to check if the result file already exist in the destination folder
def checkfile(filename):
  file_exist = 0
  file_exist += os.path.isfile(filename)
  if file_exist > 0:
    return 1
  else:
    return 0
  pass # checkfile


def singleJob(node, job):
  (priority, job_detail) = job
  (paramind,K,k,c,g,outfilename) = job_detail
  filename = outfilename
  try:
    if checkfile(filename):
      logging.info('\t--< (priority) %d (node)%s (filename) %s' %(priority, node, filename))
      fail_penalty = 0
    else:
      logging.info('\t--> (priority) %d (node)%s (filename) %s' %(priority, node, filename))
      #os.system(""" ssh -o StrictHostKeyChecking=no %s 'cd /cs/taatto/group/urenzyme/workspace/FacebookChallenge/Learning/Bin/; nohup matlab -nodisplay -nosplash -r "with_svm_train '%s' '%s' '%s' '%s' '%s' '%s'"'  """ % (node,paramind,K,k,c,g,outfilename) )
      os.system(""" ssh -o StrictHostKeyChecking=no %s 'cd /cs/taatto/group/urenzyme/workspace/FacebookChallenge/Learning/Bin/; nohup matlab -nodisplay -nosplash -r "with_svm_train '%s' '%s' '%s' '%s' '%s' '%s'" > /var/tmp/tmp'  """ % (node,paramind,K,k,c,g,outfilename) )
      logging.info('\t--| (priority) %d (node)%s (filename) %s' %(priority, node, filename))
      fail_penalty = -1
      time.sleep(1)
  except Exception as excpt_msg:
    print excpt_msg
    job_queue.put((priority, job_detail))
    logging.info('\t--= (priority) %d (node)%s (filename) %s' %(priority, node, filename))
    fail_penalty = 1
  if not checkfile(filename):
    job_queue.put((priority,job_detail))
    logging.info('\t--x (priority) %d (node)%s (filename) %s' %(priority, node, filename))
    fail_penalty = 1
  time.sleep(5)
  return fail_penalty
  pass # def


def run():
  logging.info('\t\tGenerating priority queue.')
  paramind = 0
  K = 10 
  for c in ['0.01','0.05','0.1','0.5','1','5','10','50','100','1000']:
    for g in ['0.0001','0.001','0.005','0.01','0.05','0.1','0.5','1','5','10','50','100']:
      for k in range(1,(K+1)):
        paramind += 1
        outfilename = '../../Learning/Results/ParameterSelection/%d' % paramind
        if checkfile(outfilename):
          continue
        job_queue.put((paramind,(str(paramind),str(K),str(k),c,g,outfilename)))
  # get computing node
  cluster = get_free_nodes()[0]
  #cluster = ['ukko133.hpc'] 
  # run jobs
  job_size = job_queue.qsize()
  logging.info( "\t\tProcessing %d job_queue" % (job_size))
  is_main_run_factor=1
  # running job_queue
  threads = []
  workerload = 6 
  for i in range(len(cluster)):
    for j in range(workerload):
      if job_queue.empty():
        break
      t = Worker(job_queue, cluster[i])
      time.sleep(is_main_run_factor)
      try:
        t.start()
        threads.append(t)
      except ThreadError:
        logging.warning("\t\tError: thread error caught!")
    pass
  for t in threads:
    t.join()
    pass
  pass # def


# It's actually not necessary to have '__name__' space, but whatever ...
if __name__ == "__main__":
  run()
  pass


