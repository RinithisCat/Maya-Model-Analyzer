import configparser
from pathlib import Path
import os

class CustomAppConfig:
	CFG_PolyCount = 4000
	CFG_MaxMaterials = 3
	CFG_Ngons = 0
	CFG_UVSets = 2
	CFG_2Vertex = 0
	CFG_VertexThreshold = 0.01
	savepath = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))+ "\\"+'ProjectParameters.cfg'

	def LoadFromFile(self):
		config_data = configparser.ConfigParser()
		config_data.read(self.savepath)
		GeneralConfigurationSection = config_data["GeneralConfiguration"]

		self.CFG_PolyCount = int(GeneralConfigurationSection.get("CFG_PolyCount"))
		self.CFG_MaxMaterials = int(GeneralConfigurationSection.get("CFG_MaxMaterials"))
		self.CFG_Ngons = int(GeneralConfigurationSection.get("CFG_Ngons"))
		self.CFG_UVSets = int(GeneralConfigurationSection.get("CFG_UVSets"))
		self.CFG_2Vertex = float(GeneralConfigurationSection.get("CFG_2Vertex"))
		self.CFG_VertexThreshold = float(GeneralConfigurationSection.get("CFG_VertexThreshold"))

	def SaveToFile(self,polyCount, materialsAmount, NgonsAmount,UVSets,DuplicatedVertex,VertexThresold):
		config = configparser.ConfigParser()
		config.add_section("GeneralConfiguration")

		config.set("GeneralConfiguration", "CFG_PolyCount", f"{polyCount}")
		config.set("GeneralConfiguration", "CFG_MaxMaterials", f"{materialsAmount}")
		config.set("GeneralConfiguration", "CFG_Ngons", f"{NgonsAmount}")
		config.set("GeneralConfiguration", "CFG_UVSets", f"{UVSets}")
		config.set("GeneralConfiguration", "CFG_2Vertex", f"{DuplicatedVertex}")
		config.set("GeneralConfiguration", "CFG_VertexThreshold", f"{VertexThresold}")

		with open(self.savepath, 'w') as configfile:
			config.write(configfile)
			configfile.close()


if __name__ == "__main__":
	Config = CustomAppConfig()
	Config.SaveToFile(Config.CFG_PolyCount,Config.CFG_MaxMaterials,Config.CFG_Ngons,Config.CFG_UVSets,Config.CFG_2Vertex,Config.CFG_VertexThreshold)


