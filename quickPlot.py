#!/usr/bin/env python

import ROOT as r
r.gROOT.SetBatch(True)
from collections import OrderedDict as od
from commonDefs import pts

enRatioGraph = r.TGraph()
enRatioGraph.GetXaxis().SetTitle('Photon pt')
enRatioGraph.GetYaxis().SetTitle('Mean energy ratio all ts to CP, eta 2.1')
iGraph = 0

for pt in pts:
    enRatioHist = r.TH1F('EtsOvEcp_pt%g_eta21'%pt,'EtsOvEcp_pt%g_eta21'%pt, 80, 0., 2.)
    enRatioHist.GetXaxis().SetTitle('En all ts / En CP')
    inFile = r.TFile('trees/unconverted_pt%g_eta21.root'%pt)
    tree = inFile.Get('ticlTree/TSTree_EM3')
    tsEnergy = od()
    cpEnergy = od()
    print 'ED DEBUG on file %s, tree has %g entries'%(inFile.GetName(), tree.GetEntries())
    iEntry = 0
    nEntries = tree.GetEntries()
    while iEntry < nEntries:
        tree.GetEntry(iEntry)
        iEnergy = iEntry
        iEntry += 1
        nTS = tree.nTS
        if nTS<1: continue
        ts_en = tree.ts_energy
        cp_en = tree.cp_energy
        tsEnergy[iEnergy] = ts_en
        cpEnergy[iEnergy] = cp_en
        for i in range(nTS-1):
            tree.GetEntry(iEntry+i)
            tsEnergy[iEnergy] += ts_en
            iEntry+=1
    for evt,ts_tot in tsEnergy.iteritems():
        ratio = ts_tot / cpEnergy[evt]
        enRatioHist.Fill(ratio)
    canv = r.TCanvas()
    enRatioHist.Draw('hist')
    enRatioHist.Fit('gaus')
    fit = enRatioHist.GetFunction('gaus')
    mean = fit.GetParameter(1)
    canv.SaveAs('plots/EtsOvEcp_pt%g_eta21.pdf'%pt)
    canv.SaveAs('plots/EtsOvEcp_pt%g_eta21.png'%pt)
    enRatioGraph.SetPoint(iGraph,pt,mean)
    iGraph +=1
    inFile.Close()

canv = r.TCanvas()
enRatioGraph.Draw()
canv.SaveAs('plots/EnergyContainmentVsPt_eta21.pdf')
canv.SaveAs('plots/EnergyContainmentVsPt_eta21.png')
