import FWCore.ParameterSet.Config as cms

pfLinker = cms.EDProducer("PFLinker",
                          PFCandidate = cms.InputTag("particleFlow"),
                          GsfElectrons = cms.InputTag("gsfElectrons"),
                          Photons = cms.InputTag("pfPhotonTranslator:pfphot"),
#                          Muons = cms.InputTag("muons"),
                          ProducePFCandidates = cms.bool(True),
                          OutputPF = cms.string(""),
                          ValueMapElectrons = cms.string("electrons"),                              
                          ValueMapPhotons = cms.string("photons"))