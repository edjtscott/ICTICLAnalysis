from os import system

def run(cmd, dry=False):
    print cmd
    if not dry: system(cmd)

#inputDir = '/eos/cms/store/user/amagnan/HGCAL/TiCL/210325/CloseByPhotons'
#inputDir = '/eos/cms/store/user/amagnan/HGCAL/TiCL/210406/CloseByPhotonsFromVtx/'
inputDir = '/eos/cms/store/user/amagnan/HGCAL/TiCL/210420/CloseByPhotonsFromVtx'
pts = [3,5,10,15,20,30,40,50,75,100,150,200]
#etas = [17,19,21,23,25,27]
etas = [21]
nRuns=10

