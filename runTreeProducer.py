#!/usr/bin/env python

from os import system
def run(cmd, dry=False):
    print cmd
    if not dry: system(cmd)

#inputDir = '/eos/cms/store/user/amagnan/HGCAL/TiCL/210325/CloseByPhotons'
inputDir = '/eos/cms/store/user/amagnan/HGCAL/TiCL/210406/CloseByPhotonsFromVtx/'
pts = [3,5,10,15,20,30,40,50,75,100,150,200]
#etas = [17,19,21,23,25,27]
etas = [21]
nRuns=10

for pt in pts:
    for eta in etas:
        files = ''
        for iRun in range(nRuns):
            files += 'file:%s/step3ticl_pt%g_eta%g_run%g.root,'%(inputDir,pt,eta,iRun)
        files = files[:-1] ##remove trailing comma
        
        #theCmd = 'cmsRun TiCLTreeProducer/test/run_tree_cfg.py inputFiles=%s outputFile=unconverted_pt%g_eta%g.root'%(files, pt, eta)
        theCmd = 'cmsRun TiCLTreeProducer/test/run_tree_cfg.py inputFiles=%s outputFile=converted_pt%g_eta%g.root'%(files, pt, eta)
        run(theCmd)
