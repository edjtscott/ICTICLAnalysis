#!/usr/bin/env python

from commonDefs import *

for pt in pts:
    for eta in etas:
        files = ''
        for iRun in range(nRuns):
            files += 'file:%s/step3ticl_pt%g_eta%g_run%g.root,'%(inputDir,pt,eta,iRun)
        files = files[:-1] ##remove trailing comma
        
        #theCmd = 'cmsRun TiCLTreeProducer/test/run_tree_cfg.py inputFiles=%s outputFile=trees/unconverted_pt%g_eta%g.root'%(files, pt, eta)
        theCmd = 'cmsRun TiCLTreeProducer/test/run_tree_cfg.py inputFiles=%s outputFile=trees/fromvtx_pt%g_eta%g.root'%(files, pt, eta)
        run(theCmd)
