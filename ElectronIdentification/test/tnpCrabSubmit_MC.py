import CRABClient
from CRABClient.UserUtilities import config #getUsernameFromSiteDB
import sys
config = config()

submitVersion = "ntuple_PFID_Run3Summer21_forPR_test"
mainOutputDir = '/store/group/phys_egamma/akapoor/%s' % submitVersion

# config.General.transferLogs = False

config.General.transferOutputs = True
config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/afs/cern.ch/user/a/akapoor/workspace/2020/EGamma_ggAnalysis_Ntuplizer/CMSSW_12_0_0/src/RecoEgamma/ElectronIdentification/test/testElectronMVA_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.Data.allowNonValidInputDataset = True

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_CH_CERN'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from http.client import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabdevCommand('submit', config = config)
        except HTTPException as hte:
            print("Failed submitting task: %s" % (hte.headers))
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 20
    config.Data.allowNonValidInputDataset = True
    
    
    samples=[
        
        ('/ZprimeToEE_M-3000_TuneCP5_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
         'ZprimeToEE_M-3000_TuneCP5_14TeV-pythia8'),
        
        # ('/ZprimeToEE_M-4000_TuneCP5_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'ZprimeToEE_M-4000_TuneCP5_14TeV-pythia8'),
        
        # ('/DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'DYJets_incl_MLL-50_TuneCP5_14TeV-madgraphMLM-pythia8'),
        
        # ('/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8'),
        
        # ('/GJet_Pt-10to40_DoubleEMEnriched_TuneCP5_14TeV_Pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'GJet_Pt-10to40_DoubleEMEnriched_TuneCP5_14TeV_Pythia8'),
        
        # ('/GJet_Pt-40toInf_DoubleEMEnriched_TuneCP5_14TeV_Pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'GJet_Pt-40toInf_DoubleEMEnriched_TuneCP5_14TeV_Pythia8'),
        
        # ('/QCD_Pt-10to30_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-10to30_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-30to50_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-50to80_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt-80to120_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt-120to170_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v3/MINIAODSIM',
        #  'QCD_Pt-170to300_EMEnriched_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt-300toInf_EMEnriched_TuneCP5_14TeV_pythia8'),
         
        # ('/QCD_Pt_15to20_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_15to20_bcToE_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt_20to30_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_20to30_bcToE_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt_30to80_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt_30to80_bcToE_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt_80to170_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt_80to170_bcToE_TuneCP5_14TeV_pythia8'),

        # ('/QCD_Pt_170to250_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'QCD_Pt_170to250_bcToE_TuneCP5_14TeV_pythia8'),
        
        # ('/QCD_Pt_250toInf_bcToE_TuneCP5_14TeV_pythia8/Run3Summer21MiniAOD-FlatPU0to70_rndm_120X_mcRun3_2021_realistic_v5-v1/MINIAODSIM',
        #  'QCD_Pt_250toInf_bcToE_TuneCP5_14TeV_pythia8'),
        
        # ('/TauGun_Pt-5to15_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'TauGun_Pt-5to15_14TeV-pythia8'),
        
        # ('/TauGun_Pt-15to500_14TeV-pythia8/Run3Summer21MiniAOD-FlatPU0to70_120X_mcRun3_2021_realistic_v5-v2/MINIAODSIM',
        #  'TauGun_Pt-15to500_14TeV-pythia8')
    ]
        
    for sample in samples:
        print(sample[0])
        config.Data.inputDataset=sample[0]
        config.General.requestName=sample[1]
        submit(config)
