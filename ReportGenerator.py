#Import Library
import maya.cmds as pml
import os
import math
import sys
import importlib
import time

class ReportGenerator:
	#Debug 
	start_time = time.time()
	
	#import Config Archive
	sys.path.append(str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')))
	import ConfigDef
	importlib.reload(ConfigDef)
	
	#Active list
	meshList = [pml.listRelatives(i,p=True,pa=True)[0] for i in pml.ls(type='mesh',ni=True) or []]
	meshList = list(set(meshList))
	pml.select(meshList)
	activeListLenght = len(meshList)
	
	#Poly Evaluate
	polyCountData = (pml.polyEvaluate(t=True))
	
	#Poly UV Evaluate
	uv_sets = pml.polyUVSet(query=True, allUVSets=True)
	UVSetsData = len(uv_sets)
	
	#Get Shading Data
	Materials = pml.hyperShade("",smn=True)
	Materials = pml.ls(sl=True)
	MatIDData = len(Materials)
	
	#Ngon Checker
	pml.select(meshList)
	pml.polySelectConstraint(mode=3,type=0x0008,size=3)
	pml.polySelectConstraint(disable=True)
	ngon = pml.filterExpand(ex=True,sm=34) or []
	HasNGonData = len(ngon)
	
	#Duplicated Vertices Checker
	pml.select(meshList)
	pml.polySelectConstraint(mode=3,type=0x0001)
	pml.polySelectConstraint(disable=True)
	vertices = pml.filterExpand(ex=True,sm=31) or []
	
	vtxpositions = {}
	numvtx = 0
	closevertices = []
	threshold = ConfigDef.CustomAppConfig().CFG_VertexThreshold
	
	for vertex in vertices:
		vtxpositions[str(numvtx)] = pml.pointPosition(vertex, w=True)
		numvtx = numvtx + 1
	
	for i in range(len(vtxpositions)):
		pos1 = vtxpositions[str(i)]
		for j in range(i+1,len(vtxpositions)):
			pos2 = vtxpositions[str(j)]
			xDist = abs(pos1[0] - pos2[0])
			if xDist < threshold:
				yDist = abs(pos1[1] - pos2[1])
				if yDist < threshold:
					zDist = abs(pos1[2] - pos2[2])
					if zDist < threshold:
						distance = math.dist(pos1,pos2)
						if distance < threshold:
							closevertices.append(i)
							closevertices.append(j)
	
	tempvertex = closevertices
	closevertices = []
	[closevertices.append(x) for x in tempvertex if x not in closevertices]
	
	'uncomment this in case you want to see the close vertices of mesh index 0'
	pml.select(meshList[0]+'.vtx[{}]'.format(v) for v in closevertices)
	Has2VertexData = len(closevertices)
	
	#List the parameters
	polyCount = 'Number of Tris'
	UVSets = 'Number of UV Sets'
	NumMatID = 'Number of Material IDs'
	HasNGon = 'Number of Ngons'
	Has2Vertex = 'Number of Duplicated Vertices'
	
	#Header Row
	header = [polyCount,UVSets,NumMatID,HasNGon,Has2Vertex]
	
	#Compare Pass
	ConfigParams = ConfigDef.CustomAppConfig()
	ConfigParams.LoadFromFile()
	PassPolyCount = False
	PassVertex = False
	PassMaterial = False
	PassUV = False
	PassNgon = False
	
	if int(polyCountData) <= int(ConfigParams.CFG_PolyCount):
		PassPolyCount = True
	if int(UVSetsData) <= int(ConfigParams.CFG_UVSets):
		PassUV = True
	if int(MatIDData) < int(ConfigParams.CFG_MaxMaterials):
		PassMaterial = True
	if int(Has2VertexData) == int(ConfigParams.CFG_2Vertex):
		PassVertex=True
	if int(HasNGonData) == int(ConfigParams.CFG_Ngons):
		PassNgon = True
	
	
	#Cast data to text
	polyCountData = str(polyCountData)
	UVSetsData = str(UVSetsData)
	MatIDData = str(MatIDData)
	HasNGonData = str(HasNGonData)
	Has2VertexData = str(Has2VertexData)
	
	
	#Set data into a list 
	data = [polyCountData,UVSetsData, MatIDData, HasNGonData, Has2VertexData]
	PassInfo = [str(PassPolyCount),str(PassUV),str(PassMaterial), str(PassNgon), str(PassVertex)]
	
	#Get Desktop Path
	user = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
	
	#Create CSV
	with open(user+'\\'+'Report.csv', 'w') as report:
		report.write(',')
		for item in header:
			report.write(item+',')	
		report.write('\n')
		report.write('Polys Data,')
		for x in data:
			report.write(x + ',')
		report.write('\n')
		report.write('Pass Test,')
		for x in PassInfo:
			report.write(x + ',')
		report.write('\n')
		
	print("--- %s seconds ---" % (time.time() - start_time))