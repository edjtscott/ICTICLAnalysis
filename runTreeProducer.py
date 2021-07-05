#!/usr/bin/env python

from os import system, listdir

def run(cmd, dry=False):
    print cmd
    if not dry: system(cmd)

nRuns = 10

inDir = '/eos/cms/store/group/dpg_hgcal/comm_hgcal/escott/TICLstudies/Pass0/CloseByPhotonsFromVtx'

fileStr = 'inputFiles='
for fName in listdir(inDir):
    if not fName.count('step3ticl'): continue
    fileStr += '%s/file:%s,'%(inDir,fName)
fileStr = fileStr[:-1]    

run('cmsRun TiCLTreeProducer/test/run_tree_cfg.py %s outputFile=trees/edtestPU.root'%fileStr)
