#!/usr/bin/python3
#-*-encoding:utf8-*-


import os
import sys
import string
import shutil
import json
import uuid
from shutil import copyfile
import flatbuffers as Parser


ENGINE_VERSION = "3.10.0.0"

script_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
targetOut = os.path.join(script_path, "csd")

with open(os.path.join(script_path, "data", "header_rule.json"), "r") as fileObj:
	HeaderRules = json.load(fileObj)
	fileObj.close()

with open(os.path.join(script_path, "data", "child_rule.json"), "r") as fileObj:
	ChildRules = json.load(fileObj)
	fileObj.close()	

if not os.path.exists(targetOut):
	os.mkdir(targetOut)

csdPath = ""


# override Table.String to avoid difference of 'bytes' between versions of Python
Table_String = Parser.Table.String
def Table_String_new(tab, off):
	return Table_String(tab, off).decode("utf-8")

Parser.Table.String = Table_String_new

str_types = (str,)
try:
	str_types += (bytes,)
except:
	pass
try:
	str_types += (unicode,)
except:
	pass

def normalizeResult(result):
	if isinstance(result, str_types):
		return result
	
	if isinstance(result, float):
		return "%0.04f" %(result)
	
	return str(result)




# convert csb file to csd file
class csb2csd:
	def __init__(self, csbPath, csdPath):
		self.csbPath = csbPath
		self.csdPath = csdPath	
	
	
	def getImageOption(self, childKey, resourceData):
		fileType = "Default"
		if resourceData.ResourceType() == 0:
			fileType = "Normal"
		elif resourceData.ResourceType() == 1:
			fileType = "MarkedSubImage"
			
		resFile = resourceData.Path().decode("utf-8")
		plistFile = resourceData.PlistFile().decode("utf-8")
		if resFile == "" and plistFile == "":
			return '  <%s />\n' %(childKey)
	
		if resFile.startswith("Default/"):
			fileType = "Default"
	
		text = '  <%s Type="%s" Path="%s" Plist="%s" />\n' %(childKey, fileType, resFile, plistFile)
		return text
	
	
	def getEasingText(self, easingData):
		if not easingData:
			return ""
		
		easingType = easingData.Type()
		if easingType == -1:
			return ""
		else:
			return '            <EasingData Type="%d" />\n' %(easingType)
	
	def getFrameText(self, frameData, property):
		text = ""
		
		if property == "VisibleForFrame":
			realFrame = frameData.BoolFrame()
			text += '          <BoolFrame FrameIndex="%d" Tween="%s" Value="%s" />\n' %(realFrame.FrameIndex(), realFrame.Tween(), realFrame.Value())
	
		elif property == "Position":
			realFrame = frameData.PointFrame()
			text += '          <PointFrame FrameIndex="%d" X="%0.04f" Y="%0.04f">\n' %(realFrame.FrameIndex(), realFrame.Position().X(), realFrame.Position().Y())
			text += self.getEasingText(realFrame.EasingData())
			text += '          </PointFrame>\n'
	
		elif property == "Scale":
			realFrame = frameData.ScaleFrame()
			text += '          <ScaleFrame FrameIndex="%d" X="%0.04f" Y="%0.04f">\n' %(realFrame.FrameIndex(), realFrame.Scale().ScaleX(), realFrame.Scale().ScaleX())
			text += self.getEasingText(realFrame.EasingData())
			text += '          </ScaleFrame>\n'
	
		elif property == "RotationSkew":
			realFrame = frameData.ScaleFrame()
			text += '          <ScaleFrame FrameIndex="%d" X="%0.04f" Y="%0.04f">\n' %(realFrame.FrameIndex(), realFrame.Scale().ScaleX(), realFrame.Scale().ScaleX())
			text += self.getEasingText(realFrame.EasingData())
			text += '          </ScaleFrame>\n'
	
		elif property == "CColor":
			realFrame = frameData.ColorFrame()
			colorData = realFrame.Color()
			text += '          <ColorFrame FrameIndex="%d" Alpha="%d">\n' %(realFrame.FrameIndex(), colorData.A())
			text += '            <Color A="%d" R="%d" G="%d" B="%d" />' %(colorData.A(), colorData.R(), colorData.G(), colorData.B())
			text += '          </ColorFrame>\n'
	
		elif property == "FileData":
			realFrame = frameData.TextureFrame()
			text += '          <TextureFrame FrameIndex="%d" Tween="%s">\n' %(realFrame.FrameIndex(), realFrame.Tween())
			text += '          ' + self.getImageOption("TextureFile", realFrame.TextureFile())
			text += '          </TextureFrame>\n'
	
		elif property == "FrameEvent":
			realFrame = frameData.EventFrame()
			text += '          <EventFrame FrameIndex="%d" Value="%s">\n' %(realFrame.FrameIndex(), realFrame.Value())
			text += '          </EventFrame>\n'
	
		elif property == "Alpha":
			realFrame = frameData.IntFrame()
			text += '          <IntFrame FrameIndex="%d" Value="%d">\n' %(realFrame.FrameIndex(), realFrame.Value())
			text += self.getEasingText(realFrame.EasingData())
			text += '          </IntFrame>\n'
	
		elif property == "AnchorPoint":
			realFrame = frameData.ScaleFrame()
			text += '          <ScaleFrame FrameIndex="%d" X="%0.04f" Y="%0.04f">\n' %(realFrame.FrameIndex(), realFrame.Scale().ScaleX(), realFrame.Scale().ScaleX())
			text += self.getEasingText(realFrame.EasingData())
			text += '          </ScaleFrame>\n'
	
		elif property == "ZOrder":
			realFrame = frameData.IntFrame()
			text += '          <IntFrame FrameIndex="%d" Value="%d">\n' %(realFrame.FrameIndex(), realFrame.Value())
			text += '          </IntFrame>\n'
	
		elif property == "ActionValue":
			realFrame = frameData.InnerActionFrame()
			#todo
		elif property == "BlendFunc":
			realFrame = frameData.BlendFrame()
			text += '          <BlendFuncFrame FrameIndex="%d" Src="%d" Dst="%d">\n' %(realFrame.FrameIndex(), realFrame.BlendFunc().Src(), realFrame.BlendFunc().Dst())
			text += '          </BlendFuncFrame>\n'
			
		return text
	
	
	def getTimeline(self, timeLineData):
		property = timeLineData.Property()
		text = '        <Timeline ActionTag="%d" Property="%s">\n' %(timeLineData.ActionTag(), timeLineData.Property())
		for i in range(timeLineData.FramesLength()):
			frameData = timeLineData.Frames(i)
			text += self.getFrameText(frameData, property)
			
		text += '        </Timeline>\n'
		return text
	
	
	def getRealOption(self, className, optionData):
		realOption = None
		nameMap = {
			"Particle":"ParticleSystem"
		}
		mss = dir(Parser)
		optionClassName = nameMap.get(className, className) + "Options"
		optionClass = getattr(Parser, optionClassName, None)
		if not optionClass:
			return 
	
		if optionClass:
			realOption = optionClass()
		
		if realOption:
			realOption._tab = optionData.Data()._tab
			return realOption
		else:
			return optionData
	
	def getHeaderOption(self, optionData, optionKey, valuePath, defaultValue="", replaceInfo=""):
		valueList = valuePath.split(".")
		parentValue = optionData
		for path in valueList:
			if not parentValue:
				return ""

			func = getattr(parentValue, path, None)
			if not func:
				return ""
			
			parentValue = func()
			if not parentValue:
				return ""
			
		result = normalizeResult(parentValue)
	
		# ignoring field 'LabelText' will lead to a csd file parsing error
		if not optionKey in ["LabelText", "ButtonText", "PlaceHolderText"]:
			if result.upper() == str(defaultValue).upper():
				return ""
			result = result.replace("\n", "&#xA;")
		
		renameDict = {}
		if replaceInfo != "":
			renameList = replaceInfo.split(",")
			for renameText in renameList:
				kvList = renameText.split("=")
				renameDict[kvList[0]] = kvList[1]
				
		if result in renameDict:
			result = renameDict[result]
			
		text = '%s="%s" ' %(optionKey, result)
	
		#scale9sprite special
		# if optionKey == "Scale9Enabled":
		# # if optionKey == "Scale9Enable" and result == "True":
		# 	text += self.getHeaderOption(optionData, "Scale9OriginX", "CapInsets.X")
		# 	text += self.getHeaderOption(optionData, "Scale9OriginY", "CapInsets.Y")
		# 	text += self.getHeaderOption(optionData, "Scale9Width", "CapInsets.Width")
		# 	text += self.getHeaderOption(optionData, "Scale9Height", "CapInsets.Height")
		return text
	
	def getDefaultOptionHeader(self, widgetOption, tab):
		global HeaderRules
		DefaultRules = HeaderRules["Default"]
		
		text = tab + '<AbstractNodeData '
		for ruleOption in DefaultRules:
			text += self.getHeaderOption(widgetOption, ruleOption[0], ruleOption[1], ruleOption[2])
			
		return text
	
	
	def getChildProperty(self, optionData, optionKey, valuePath, renameProperty="", specialType=""):
		valueList = valuePath.split(".")
		parentValue = optionData
		for path in valueList:
			func = getattr(parentValue, path, None)
			if not func:
				return ""
			parentValue = func()
	
		if specialType == "ImageData":
			return self.getImageOption(optionKey, parentValue)
	
		funcList = dir(parentValue)
		validFuncList = []
		for funcName in funcList:
			if funcName.startswith("_"):
				continue
			if funcName == "Init" or funcName.startswith("GetRoot"):
				continue
			validFuncList.append(funcName)
			
		renameDict = {}
		if renameProperty != "":
			renameList = renameProperty.split(",")
			for renameText in renameList:
				kvList = renameText.split("=")
				renameDict[kvList[1]] = kvList[0]
				
		text = '  <%s ' %(optionKey)
		for funcName in validFuncList:
			func = getattr(parentValue, funcName, None)
			if not func: continue
			
			result = normalizeResult(func())
			keyValue = funcName
			if funcName in renameDict:
				keyValue = renameDict[funcName]
	
			text += '%s="%s" ' %(keyValue, str(result))
			
		text += "/>\n"
		return text
	
	
	def getDefaultOptionChild(self, widgetOption, tab, optionNames = None, reverse = False):
		global ChildRules
		DefaultRules = ChildRules["Default"]
		text = ""
		for childRule in DefaultRules:
			isSave = False
			if not optionNames:
				isSave = True
			elif reverse == True:
				if not childRule[0] in optionNames:
					isSave = True
			else:
				if childRule[0] in optionNames:
					isSave = True
					
			if isSave == True:
				text += tab + self.getChildProperty(widgetOption, childRule[0], childRule[1], childRule[2], childRule[3])
			
		return text
	
	
	def writeFile(self, text):
		with open(self.csdPath, "a") as fileObj:
			fileObj.write(text.encode("utf-8"))
			fileObj.close()
	
	def writeHeader(self, csparsebinary):
		global ENGINE_VERSION
	
		nodeTree = csparsebinary.NodeTree()
		typeName = nodeTree.Classname().decode("utf-8")
		uuidName = uuid.uuid1()
		
		text = ''
		text += '<GameFile>\n'
		text += '  <PropertyGroup Name="%s" Type="%s" ID="%s" Version="%s" />\n' %(self.groupName, typeName, uuidName, ENGINE_VERSION)
		text += '  <Content ctype="GameProjectContent">\n'
		text += '    <Content>\n'
	
		self.writeFile(text)
	
	def writeFooter(self):
		text = ''
		text += '    </Content>\n'
		text += '  </Content>\n'
		text += '</GameFile>\n'
		self.writeFile(text)
		
	def writeAction(self, csparsebinary):
		actionData = csparsebinary.Action()
		duration = actionData.Duration()
		speed = actionData.Speed()
		animationName = actionData.CurrentAnimationName().decode("utf-8")
		timeLinesLength = actionData.TimeLinesLength()
		text = ''
		if timeLinesLength > 0 :
			text += '      <Animation Duration="%d" Speed="%0.04f" ActivedAnimationName="%s">\n' %(duration, speed, animationName)
			for i in range(timeLinesLength):
				timeLineData = actionData.TimeLines(i)
				text += self.getTimeline(timeLineData)
		
			text += '      </Animation>\n'
		else:
			text += '      <Animation Duration="%d" Speed="%0.04f" />\n' %(duration, speed)
			
		self.writeFile(text)
	
	def writeAnimation(self, csparsebinary):
		animationListLength = csparsebinary.AnimationListLength()
		if animationListLength == 0:
			return
		
		text = '      <AnimationList>\n'
		for i in range(animationListLength):
			animationData = csparsebinary.AnimationList(i)
			name = animationData.Name().decode("utf-8")
			startIndex = animationData.StartIndex()
			endIndex = animationData.EndIndex()
			listLength = 1
			if listLength > 0:
				text += '        <AnimationInfo Name="%s" StartIndex="%d" EndIndex="%d">\n' %(name, startIndex, endIndex)
				text += '        </AnimationInfo>\n'
			else:	
				text += '        <AnimationInfo Name="%s" StartIndex="%d" EndIndex="%d" />\n' %(name, startIndex, endIndex)
			
		text += '      </AnimationList>\n'
		self.writeFile(text)
		
		
	def writeOptionHeader(self, optionData, widgetOption, className, tab):
		global HeaderRules
		text = self.getDefaultOptionHeader(widgetOption, tab)
		if className in HeaderRules:
			ClassRules = HeaderRules[className]
			for ruleOption in ClassRules:
				text += self.getHeaderOption(optionData, ruleOption[0], ruleOption[1], ruleOption[2], ruleOption[3])
		text += 'ctype="%sObjectData">\n' %(className)
		self.writeFile(text)	
		
	def writeChildOption(self, realOption, widgetOption, className, tab):
		global ChildRules
		text = self.getDefaultOptionChild(widgetOption, tab, ["Size"])
	
		if className in ChildRules:
			ClassRules = ChildRules[className]
			for childRule in ClassRules:
				text += tab + self.getChildProperty(realOption, childRule[0], childRule[1], childRule[2], childRule[3])
				
		text += self.getDefaultOptionChild(widgetOption, tab, ["Size"], True)
		self.writeFile(text)
	
	def writeOption(self, nodeTree, tab):
		optionData = nodeTree.Options()
		className = nodeTree.Classname().decode("utf-8")
		realOption = self.getRealOption(className, optionData)
		if not realOption:
			defaultText = tab + '<AbstractNodeData ctype="%seObjectData">\n' %(className)
			self.writeFile(defaultText)
			return
		try:
			widgetOption = realOption.WidgetOptions()
		except:
			widgetOption = realOption.NodeOptions()
		
		self.writeOptionHeader(realOption, widgetOption, className, tab)
		self.writeChildOption(realOption, widgetOption, className, tab)
		
	def writeRootNodeTree(self, nodeTree):
		widgetOption = nodeTree.Options().Data()
		widgetSize = widgetOption.Size()
		if not widgetSize:
			boneOption = Parser.BoneOptions()
			boneOption._tab = widgetOption._tab
			widgetOption = boneOption.NodeOptions()
	
		widgetSize = widgetOption.Size()
		widgetName = widgetOption.Name().decode("utf-8")
		widgetTag = widgetOption.Tag()
		text = ''
		nodeObject = {
			"Node": "GameNodeObjectData",
			"Scene": "GameNodeObjectData",
			"Layer": "GameLayerObjectData",
			"Skeleton": "SkeletonNodeObjectData",
		}
		
		if not nodeObject.get(widgetName):
			print("unknown widgetName:'%s', regarded as Node by default." %(widgetName))
			
		text += '      <ObjectData Name="%s" Tag="%d" ctype="%s">\n' %(widgetName, widgetTag, nodeObject.get(widgetName,"GameNodeObjectData"))
		text += '        <Size X="%0.04f" Y="%0.04f" />\n' %(widgetSize.Width(), widgetSize.Height())
		self.writeFile(text)	
	
	def writeRecursionNodeTree(self, nodeTree, level = 0):
		baseTab = '      ' + "    " * level
		if level > 0:
			self.writeOption(nodeTree, baseTab)
	
		childNum = nodeTree.ChildrenLength()
		if childNum > 0:
			self.writeFile(baseTab + '  <Children>\n')
			for i in range(childNum):
				child = nodeTree.Children(i)
				self.writeRecursionNodeTree(child, level + 1)
			self.writeFile(baseTab + '  </Children>\n')
			
		if level > 0:
			self.writeFile(baseTab + '</AbstractNodeData>\n')
		else:
			self.writeFile(baseTab + '</ObjectData>\n')
	
	def startConvert(self, csparsebinary):
		self.writeHeader(csparsebinary)
		self.writeAction(csparsebinary)
		self.writeAnimation(csparsebinary)
		
		nodeTree = csparsebinary.NodeTree()
		self.writeRootNodeTree(nodeTree)
		self.writeRecursionNodeTree(nodeTree)
		self.writeFooter()
		
	def dealCsdPath(self):
		fileName = os.path.basename(self.csbPath)
		self.groupName = os.path.splitext(fileName)[0]
		if self.csdPath == None :
			self.csdPath = os.path.join(targetOut, self.groupName + ".csd")
		else:
			fileDir = os.path.dirname(self.csdPath)
			if not os.path.exists(fileDir):
				os.makedirs(fileDir)
				
		if os.path.exists(self.csdPath):
			os.remove(self.csdPath)	
	
	def dealWithCsbFile(self):
		self.dealCsdPath()
		with open(self.csbPath, mode="rb") as fileObj:
			buf = fileObj.read()
			fileObj.close()
			csparsebinary = Parser.CSParseBinary.GetRootAsCSParseBinary(bytearray(buf), 0)
			self.startConvert(csparsebinary)

def main(argc, argv):
	if argc < 2:
		print("反编译csb文件")
		print("usage:\tpython csb2csd.py <infile> <outfile>")
		print("\tpython csb2csd.py <infolder> <outfolder>")
		exit(0)
		
	inpath = argv[1]
	if(os.path.isdir(inpath)):
		outpath = argv[2] if argc == 3 else targetOut
		# treat input as a folder
		for root, dirs, files in os.walk(inpath):
			for csbPath in [os.path.join(root, filename) for filename in files]:
				outfile = os.path.join(outpath, os.path.relpath(csbPath, inpath))
				outdir  = os.path.dirname(outfile)
				if not os.path.exists(outdir):
					os.makedirs(outdir)
				if os.path.splitext(csbPath)[1] in [".csb"]:
					outfile = os.path.splitext(outfile)[0] + ".csd"
					obj = csb2csd(csbPath, outfile)
					obj.dealWithCsbFile()					
				else:
					copyfile(csbPath, outfile)
		print("translation completed! check your artifacts under %s" %(os.path.realpath(outpath)))
	else:
		outpath = argv[2] if argc == 3 else None
		# treat input as a single file
		obj = csb2csd(inpath, outpath)
		obj.dealWithCsbFile()
		print("translation completed! check your artifacts under %s" %(os.path.realpath(outpath)))
		
	

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    print("finish...")
    
    

