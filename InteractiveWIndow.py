import maya.cmds as cmds
import sys
import importlib

#Find Parameters Archive
sys.path.append(str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')))
import ConfigDef
importlib.reload(ConfigDef)

#Get current data stored in config file
ConfigParams = ConfigDef.CustomAppConfig()
ConfigParams.LoadFromFile()

# Create a window
window = cmds.window(title="Project Settings Setup", widthHeight=(550, 160))

# Create a column layout
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'left', 20), columnWidth=[(1, 250), (2, 250)] )
cmds.text( label='Project Max Poly Count')
PolyCount = cmds.textField(tx=ConfigParams.CFG_PolyCount)
cmds.text( label='Max Project Materials per Model' )
MaxMaterials = cmds.textField(tx=ConfigParams.CFG_MaxMaterials)
cmds.text( label='Number of Ngons in Model' )
Ngons = cmds.textField(tx=ConfigParams.CFG_Ngons)
cmds.text( label='Max Number of UV Sets per Model' )
UVSets = cmds.textField(tx=ConfigParams.CFG_UVSets)
cmds.text( label='Duplicated Vertices' )
DuplicatedVertices = cmds.textField(tx=ConfigParams.CFG_2Vertex)
cmds.text( label='Duplicated Vertices Threshold' )
VertexThresold = cmds.textField(tx=ConfigParams.CFG_VertexThreshold)
cmds.columnLayout(adjustableColumn=True)

# Function to print the text field value
def print_text(*args):
	ConfigParams = ConfigDef.CustomAppConfig()
	ConfigParams.SaveToFile(cmds.textField(PolyCount, q=1, text=1),cmds.textField(MaxMaterials, q=1, text=1),cmds.textField(Ngons, q=1, text=1),cmds.textField(UVSets, q=1, text=1),cmds.textField(DuplicatedVertices, q=1, text=1),cmds.textField(VertexThresold, q=1, text=1))
	import ReportGenerator
	importlib.reload(ReportGenerator)

# Create a button that prints the text field value when clicked
cmds.button(label="Execute Script", command=print_text)

# Show the window
cmds.showWindow(window)