########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Monday 28 June 2010 18:00:49 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /mnt/raid/services/cvs/python/packages/share1.5/AutoDockTools/VisionInterface/Adt/Macro/ComputeGrids.py,v 1.8 2010/07/02 00:23:00 jren Exp $
#
# $Id: ComputeGrids.py,v 1.8 2010/07/02 00:23:00 jren Exp $
#

from NetworkEditor.macros import MacroNode
from NetworkEditor.macros import MacroNode
class ComputeGrids(MacroNode):
    '''
    First runs Prepare GPF on remote server to prepare a GPF based on the ligand library,
    then runs Autogrid on the remote server

    Inputs:
    port 1: LigandDB object containing info about the ligand library
    port 2: receptor_prepared object containing info about a receptor PDBQT file
    port 3: dpf_template object containing info about DPF template
    
    Outputs: 
    port 1: autogrid_results object containing info about autogrid results
    port 2: string to autogrid result URL

    '''

    def __init__(self, constrkw={}, name='ComputeGrids', **kw):
        kw['name'] = name
        MacroNode.__init__(*(self,), **kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        net.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass

    def afterAddingToNetwork(self):
        masterNet = self.macroNetwork
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        ## building macro network ##
        ComputeGrids_18 = self
        from traceback import print_exc
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            ## saving node input Ports ##
            input_Ports_19 = self.macroNetwork.ipNode
            input_Ports_19.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork")
            print_exc()
            input_Ports_19=None

        try:
            ## saving node output Ports ##
            output_Ports_20 = self.macroNetwork.opNode
            output_Ports_20.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
            output_Ports_20.move(217, 471)
        except:
            print("WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork")
            print_exc()
            output_Ports_20=None

        try:
            ## saving node GetComputeGridsInputs ##
            from Vision.StandardNodes import Generic
            GetComputeGridsInputs_21 = Generic(constrkw={}, name='GetComputeGridsInputs', library=stdlib)
            self.macroNetwork.addNode(GetComputeGridsInputs_21,217,79)
            GetComputeGridsInputs_21.addInputPort(*(), **{'singleConnection': True, 'name': 'ligands', 'cast': True, 'datatype': 'LigandDB', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'rect', 'color': '#FFCCFF', 'originalDatatype': 'None'})
            GetComputeGridsInputs_21.addInputPort(*(), **{'singleConnection': True, 'name': 'receptor_pdbqt', 'cast': True, 'datatype': 'receptor_prepared', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'triangle', 'color': '#009900', 'originalDatatype': 'None'})
            GetComputeGridsInputs_21.addInputPort(*(), **{'singleConnection': True, 'name': 'gpf_obj', 'cast': True, 'datatype': 'gpf_template', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'triangle', 'color': '#FF3333', 'originalDatatype': 'None'})
            GetComputeGridsInputs_21.addOutputPort(*(), **{'name': 'gpf_template_path', 'datatype': 'string', 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white'})
            GetComputeGridsInputs_21.addOutputPort(*(), **{'name': 'filter_file', 'datatype': 'string', 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white'})
            GetComputeGridsInputs_21.addOutputPort(*(), **{'name': 'ligand_lib', 'datatype': 'string', 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white'})
            GetComputeGridsInputs_21.addOutputPort(*(), **{'name': 'prepared_receptor', 'datatype': 'string', 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white'})
            code = """def doit(self, ligands, receptor_pdbqt, gpf_obj):
        gpf_path = gpf_obj.fullpath

        if not(os.path.exists(gpf_path)):
            print "ERROR: GPF template " + gpf_path + " does not exist!"
            return '''stop'''

        filter_file = ligands.filter_file
        ligand_lib = ligands.loc
        prepared_receptor = receptor_pdbqt.path

        pass

        self.outputData(gpf_template_path=gpf_path, filter_file=filter_file, ligand_lib=ligand_lib, prepared_receptor=prepared_receptor)

## to ouput data on port gpf_template_path use
## self.outputData(gpf_template_path=data)
## to ouput data on port filter_file use
## self.outputData(filter_file=data)
## to ouput data on port ligand_lib use
## self.outputData(ligand_lib=data)
## to ouput data on port prepared_receptor use
## self.outputData(prepared_receptor=data)






"""
            GetComputeGridsInputs_21.configure(function=code)
            GetComputeGridsInputs_21.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore Generic named GetComputeGridsInputs in network self.macroNetwork")
            print_exc()
            GetComputeGridsInputs_21=None

        try:
            ## saving node prepareGPF_kryptonite_nbcr_net ##
            from NetworkEditor.items import FunctionNode
            prepareGPF_kryptonite_nbcr_net_22 = FunctionNode(functionOrString='prepareGPF_kryptonite_nbcr_net', host="http://kryptonite.nbcr.net/opal2", namedArgs={'singlelib': '', 'r_url': '', 'zpoints': '', 'filter_file_url': '', 'lib': '', 'ypoints': '', 'filter_file': '', 'gpf': '', 'xcenter': 'auto', 'urllib': '', 'p': '', 'r': '', 'o': '', 'zcenter': 'auto', 'v': False, 'userlib': '', 'xpoints': '', 'localRun': False, 'ycenter': 'auto', 'execPath': ''}, constrkw={'functionOrString': "'prepareGPF_kryptonite_nbcr_net'", 'host': '"http://kryptonite.nbcr.net/opal2"', 'namedArgs': {'singlelib': '', 'r_url': '', 'zpoints': '', 'filter_file_url': '', 'lib': '', 'ypoints': '', 'filter_file': '', 'gpf': '', 'xcenter': 'auto', 'urllib': '', 'p': '', 'r': '', 'o': '', 'zcenter': 'auto', 'v': False, 'userlib': '', 'xpoints': '', 'localRun': False, 'ycenter': 'auto', 'execPath': ''}}, name='prepareGPF_kryptonite_nbcr_net', library=wslib)
            self.macroNetwork.addNode(prepareGPF_kryptonite_nbcr_net_22,217,141)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['singlelib'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r_url'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['zpoints'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file_url'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['lib'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['ypoints'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['gpf'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['xcenter'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['urllib'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['p'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['o'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['zcenter'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['v'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['userlib'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['xpoints'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['localRun'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['ycenter'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['execPath'].configure(*(), **{'defaultValue': None})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['singlelib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r_url'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['zpoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file_url'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['lib'].widget.configure(*(), **{'choices': ('sample', 'NCIDS_SC', 'NCI_DS1', 'NCI_DS2', 'oldNCI', 'human_metabolome', 'chembridge_building_blocks', 'drugbank_nutraceutics', 'drugbank_smallmol', 'fda_approved')})
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['lib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['ypoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file'].rebindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['filter_file'].unbindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['gpf'].rebindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['gpf'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['gpf'].unbindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['xcenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['urllib'].rebindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['urllib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['urllib'].unbindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['p'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r'].rebindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['r'].unbindWidget()
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['o'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['zcenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['v'].widget.set(0, run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['userlib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['xpoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['localRun'].widget.set(0, run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['ycenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_22.inputPortByName['execPath'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_22.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore FunctionNode named prepareGPF_kryptonite_nbcr_net in network self.macroNetwork")
            print_exc()
            prepareGPF_kryptonite_nbcr_net_22=None

        try:
            ## saving node autogrid_kryptonite_nbcr_net ##
            from NetworkEditor.items import FunctionNode
            autogrid_kryptonite_nbcr_net_23 = FunctionNode(functionOrString='autogrid_kryptonite_nbcr_net', host="http://kryptonite.nbcr.net/opal2", namedArgs={'p_url': '', 'infile_url': '', 'l': 'output.glg', 'o': False, 'p': '', 'localRun': False, 'inFile': '', 'execPath': ''}, constrkw={'functionOrString': "'autogrid_kryptonite_nbcr_net'", 'host': '"http://kryptonite.nbcr.net/opal2"', 'namedArgs': {'p_url': '', 'infile_url': '', 'l': 'output.glg', 'o': False, 'p': '', 'localRun': False, 'inFile': '', 'execPath': ''}}, name='autogrid_kryptonite_nbcr_net', library=wslib)
            self.macroNetwork.addNode(autogrid_kryptonite_nbcr_net_23,251,292)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p_url'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['infile_url'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['l'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['o'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['localRun'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['inFile'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['execPath'].configure(*(), **{'defaultValue': None})
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p_url'].rebindWidget()
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p_url'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p_url'].unbindWidget()
            autogrid_kryptonite_nbcr_net_23.inputPortByName['infile_url'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['l'].widget.set(r"output.glg", run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['o'].widget.set(0, run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['p'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['localRun'].widget.set(0, run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['inFile'].rebindWidget()
            autogrid_kryptonite_nbcr_net_23.inputPortByName['inFile'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_23.inputPortByName['inFile'].unbindWidget()
            autogrid_kryptonite_nbcr_net_23.inputPortByName['execPath'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_23.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore FunctionNode named autogrid_kryptonite_nbcr_net in network self.macroNetwork")
            print_exc()
            autogrid_kryptonite_nbcr_net_23=None

        try:
            ## saving node GetMainURLFromList ##
            from WebServices.VisionInterface.WSNodes import GetMainURLFromListNode
            GetMainURLFromList_24 = GetMainURLFromListNode(constrkw={}, name='GetMainURLFromList', library=wslib)
            self.macroNetwork.addNode(GetMainURLFromList_24,251,348)
            GetMainURLFromList_24.inputPortByName['urls'].configure(*(), **{'defaultValue': None})
            GetMainURLFromList_24.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore GetMainURLFromListNode named GetMainURLFromList in network self.macroNetwork")
            print_exc()
            GetMainURLFromList_24=None

        try:
            ## saving node MakeAutogridResultObj ##
            from Vision.StandardNodes import Generic
            MakeAutogridResultObj_25 = Generic(constrkw={}, name='MakeAutogridResultObj', library=stdlib)
            self.macroNetwork.addNode(MakeAutogridResultObj_25,121,402)
            MakeAutogridResultObj_25.addInputPort(*(), **{'singleConnection': True, 'name': 'autogrid_result_url', 'cast': True, 'datatype': 'string', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white', 'originalDatatype': 'None'})
            MakeAutogridResultObj_25.addOutputPort(*(), **{'name': 'autogrid_result_obj', 'datatype': 'autogrid_results', 'height': 8, 'width': 12, 'shape': 'triangle', 'color': '#FF33CC'})
            code = """def doit(self, autogrid_result_url):
        from AutoDockTools.VisionInterface.Adt.autogrid_results import autogrid_results

        agro = autogrid_results(autogrid_result_url, '''url''')
        
	pass
## to ouput data on port autogrid_result_obj use
        self.outputData(autogrid_result_obj=agro)

"""
            MakeAutogridResultObj_25.configure(function=code)
            MakeAutogridResultObj_25.configure(*(), **{'paramPanelImmediate': 1, 'expanded': False})
        except:
            print("WARNING: failed to restore Generic named MakeAutogridResultObj in network self.macroNetwork")
            print_exc()
            MakeAutogridResultObj_25=None

        try:
            ## saving node GetURLFromList ##
            from WebServices.VisionInterface.WSNodes import GetURLFromListNode
            GetURLFromList_26 = GetURLFromListNode(constrkw={}, name='GetURLFromList', library=wslib)
            self.macroNetwork.addNode(GetURLFromList_26,110,198)
            GetURLFromList_26.inputPortByName['urllist'].configure(*(), **{'defaultValue': None})
            GetURLFromList_26.inputPortByName['ext'].configure(*(), **{'defaultValue': None})
            GetURLFromList_26.inputPortByName['ext'].widget.set(r"gpf", run=False)
            GetURLFromList_26.configure(*(), **{'paramPanelImmediate': 1})
        except:
            print("WARNING: failed to restore GetURLFromListNode named GetURLFromList in network self.macroNetwork")
            print_exc()
            GetURLFromList_26=None

        #self.macroNetwork.run()
        self.macroNetwork.freeze()

        ## saving connections for network ComputeGrids ##
        input_Ports_19 = self.macroNetwork.ipNode
        if input_Ports_19 is not None and GetComputeGridsInputs_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_19, GetComputeGridsInputs_21, "new", "ligands", blocking=True
                    , splitratio=[0.25038057532685992, 0.40242243717082576])
            except:
                print("WARNING: failed to restore connection between input_Ports_19 and GetComputeGridsInputs_21 in network self.macroNetwork")
        if input_Ports_19 is not None and GetComputeGridsInputs_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_19, GetComputeGridsInputs_21, "new", "receptor_pdbqt", blocking=True
                    , splitratio=[0.31642654296910228, 0.49356822236979669])
            except:
                print("WARNING: failed to restore connection between input_Ports_19 and GetComputeGridsInputs_21 in network self.macroNetwork")
        if input_Ports_19 is not None and GetComputeGridsInputs_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_19, GetComputeGridsInputs_21, "new", "gpf_obj", blocking=True
                    , splitratio=[0.57570983312901203, 0.33826779179418875])
            except:
                print("WARNING: failed to restore connection between input_Ports_19 and GetComputeGridsInputs_21 in network self.macroNetwork")
        if GetComputeGridsInputs_21 is not None and prepareGPF_kryptonite_nbcr_net_22 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetComputeGridsInputs_21, prepareGPF_kryptonite_nbcr_net_22, "gpf_template_path", "gpf", blocking=True
                    , splitratio=[0.37911517364560754, 0.49588454022594075])
            except:
                print("WARNING: failed to restore connection between GetComputeGridsInputs_21 and prepareGPF_kryptonite_nbcr_net_22 in network self.macroNetwork")
        if GetComputeGridsInputs_21 is not None and prepareGPF_kryptonite_nbcr_net_22 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetComputeGridsInputs_21, prepareGPF_kryptonite_nbcr_net_22, "filter_file", "filter_file", blocking=True
                    , splitratio=[0.51555458245420727, 0.58910990532612562])
            except:
                print("WARNING: failed to restore connection between GetComputeGridsInputs_21 and prepareGPF_kryptonite_nbcr_net_22 in network self.macroNetwork")
        if GetComputeGridsInputs_21 is not None and prepareGPF_kryptonite_nbcr_net_22 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetComputeGridsInputs_21, prepareGPF_kryptonite_nbcr_net_22, "ligand_lib", "urllib", blocking=True
                    , splitratio=[0.45378244060628786, 0.49829462092378918])
            except:
                print("WARNING: failed to restore connection between GetComputeGridsInputs_21 and prepareGPF_kryptonite_nbcr_net_22 in network self.macroNetwork")
        if GetComputeGridsInputs_21 is not None and prepareGPF_kryptonite_nbcr_net_22 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetComputeGridsInputs_21, prepareGPF_kryptonite_nbcr_net_22, "prepared_receptor", "r", blocking=True
                    , splitratio=[0.30158184825681655, 0.46256232709378253])
            except:
                print("WARNING: failed to restore connection between GetComputeGridsInputs_21 and prepareGPF_kryptonite_nbcr_net_22 in network self.macroNetwork")
        if GetComputeGridsInputs_21 is not None and autogrid_kryptonite_nbcr_net_23 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetComputeGridsInputs_21, autogrid_kryptonite_nbcr_net_23, "prepared_receptor", "inFile", blocking=True
                    , splitratio=[0.63016045430148715, 0.62091422998177115])
            except:
                print("WARNING: failed to restore connection between GetComputeGridsInputs_21 and autogrid_kryptonite_nbcr_net_23 in network self.macroNetwork")
        if autogrid_kryptonite_nbcr_net_23 is not None and GetMainURLFromList_24 is not None:
            try:
                self.macroNetwork.connectNodes(
                    autogrid_kryptonite_nbcr_net_23, GetMainURLFromList_24, "result", "urls", blocking=True
                    , splitratio=[0.4713453370864038, 0.73699665503637379])
            except:
                print("WARNING: failed to restore connection between autogrid_kryptonite_nbcr_net_23 and GetMainURLFromList_24 in network self.macroNetwork")
        if GetMainURLFromList_24 is not None and MakeAutogridResultObj_25 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetMainURLFromList_24, MakeAutogridResultObj_25, "newurl", "autogrid_result_url", blocking=True
                    , splitratio=[0.37530325590010172, 0.67260462300696811])
            except:
                print("WARNING: failed to restore connection between GetMainURLFromList_24 and MakeAutogridResultObj_25 in network self.macroNetwork")
        output_Ports_20 = self.macroNetwork.opNode
        if MakeAutogridResultObj_25 is not None and output_Ports_20 is not None:
            try:
                self.macroNetwork.connectNodes(
                    MakeAutogridResultObj_25, output_Ports_20, "autogrid_result_obj", "new", blocking=True
                    , splitratio=[0.54860274312929591, 0.61692487705230459])
            except:
                print("WARNING: failed to restore connection between MakeAutogridResultObj_25 and output_Ports_20 in network self.macroNetwork")
        if GetMainURLFromList_24 is not None and output_Ports_20 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetMainURLFromList_24, output_Ports_20, "newurl", "new", blocking=True
                    , splitratio=[0.56961778623989434, 0.55443680742298707])
            except:
                print("WARNING: failed to restore connection between GetMainURLFromList_24 and output_Ports_20 in network self.macroNetwork")
        if prepareGPF_kryptonite_nbcr_net_22 is not None and GetURLFromList_26 is not None:
            try:
                self.macroNetwork.connectNodes(
                    prepareGPF_kryptonite_nbcr_net_22, GetURLFromList_26, "result", "urllist", blocking=True
                    , splitratio=[0.38550670487593142, 0.45424125807822219])
            except:
                print("WARNING: failed to restore connection between prepareGPF_kryptonite_nbcr_net_22 and GetURLFromList_26 in network self.macroNetwork")
        if GetURLFromList_26 is not None and autogrid_kryptonite_nbcr_net_23 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetURLFromList_26, autogrid_kryptonite_nbcr_net_23, "url", "p_url", blocking=True
                    , splitratio=[0.65566147293832433, 0.57782517914212228])
            except:
                print("WARNING: failed to restore connection between GetURLFromList_26 and autogrid_kryptonite_nbcr_net_23 in network self.macroNetwork")
        self.macroNetwork.runOnNewData.value = False

        ## modifying MacroInputNode dynamic ports
        input_Ports_19 = self.macroNetwork.ipNode
        input_Ports_19.outputPorts[1].configure(name='GetComputeGridsInputs_ligands')
        input_Ports_19.outputPorts[2].configure(name='GetComputeGridsInputs_receptor_pdbqt')
        input_Ports_19.outputPorts[3].configure(name='GetComputeGridsInputs_gpf_obj')

        ## modifying MacroOutputNode dynamic ports
        output_Ports_20 = self.macroNetwork.opNode
        output_Ports_20.inputPorts[1].configure(singleConnection='auto')
        output_Ports_20.inputPorts[2].configure(singleConnection='auto')
        output_Ports_20.inputPorts[1].configure(name='MakeAutogridResultObj_autogrid_result_obj')
        output_Ports_20.inputPorts[2].configure(name='GetMainURLFromList_newurl')
        ## configure MacroNode input ports
        ComputeGrids_18.inputPorts[0].configure(name='GetComputeGridsInputs_ligands')
        ComputeGrids_18.inputPorts[0].configure(datatype='LigandDB')
        ComputeGrids_18.inputPorts[1].configure(name='GetComputeGridsInputs_receptor_pdbqt')
        ComputeGrids_18.inputPorts[1].configure(datatype='receptor_prepared')
        ComputeGrids_18.inputPorts[2].configure(name='GetComputeGridsInputs_gpf_obj')
        ComputeGrids_18.inputPorts[2].configure(datatype='gpf_template')
        ## configure MacroNode output ports
        ComputeGrids_18.outputPorts[0].configure(name='MakeAutogridResultObj_autogrid_result_obj')
        ComputeGrids_18.outputPorts[0].configure(datatype='autogrid_results')
        ComputeGrids_18.outputPorts[1].configure(name='GetMainURLFromList_newurl')
        ComputeGrids_18.outputPorts[1].configure(datatype='string')

        ComputeGrids_18.shrink()

        ## reset modifications ##
        ComputeGrids_18.resetTags()
        ComputeGrids_18.buildOriginalList()
