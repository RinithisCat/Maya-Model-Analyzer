# Maya-Model-Analyzer
This is intended to automatize some steps of the model checking for Artists pipeline before sending their models to Art QA.
The parameters here are: PolyCount, Number of Materials, Number of UVSets, Number of Duplicated Vertices, Number of Ngons
With this tool you will be able to automatically check your models with the project parameters. It is composed by 3 scripts and a .cfg file. 
Try to not use it with a model above 50K polys, the performance may fall drastically

Importing files to maya:
ReportGenerator.py ConfigDef.py InteractiveWIndow.py ProjectParameters.cfg 
These 4 archives MUST BE inside your desktop folder.
Open maya, drag and drop InteractiveWindow.py into python scripts window. If you are not seeing a python shelf, just MEL, you will need to create a tab from type python

![image](https://github.com/user-attachments/assets/d24465cb-2306-4646-bc4d-52dcc897f223)
![image](https://github.com/user-attachments/assets/ce06ae82-7b00-4650-94de-3def1d19bf4c)
![image](https://github.com/user-attachments/assets/3dfbc16a-1e6b-4dae-9adc-59f3d16b9cb2)

Creating your tools shelf:
Go to your shelfs in maya and click in the gear in the left, so create a new shelf named “Tools” and highlight it

![image](https://github.com/user-attachments/assets/b96f91d7-ce30-400a-af39-794828d2cae0)

Inside the scripts editor, you can then go to file and save it to your current maya shelf by clicking in: File > Save Script to Shelf.

![image](https://github.com/user-attachments/assets/a6ae7650-53ff-4d7b-ae2f-d6213556fe58)

It will ask for a name and save it into your currently selected shelf. Name it Model Analyzer

![image](https://github.com/user-attachments/assets/deef2394-6cca-4359-a5c2-240af14ed89e)



Using the model Analyzer:

To use it, just click in the previously created button and this window will show up to you:

![image](https://github.com/user-attachments/assets/7fb1b60e-6956-42d3-b347-c082982786d0)

Here you can define what’s your project max targets. Once you filled this up, it will save this info and run the reporter, generating a csv file with the report. A model of the report will look like this:

 ![image](https://github.com/user-attachments/assets/7938fa4f-4b0c-4f26-8f9e-197acb75d2d0)

Additional Info:

ConfigDef is a script that Generates a .cfg file to the Desktop Folder. This config file will be usable to generate a report by ReportGenerator Script.
When you run ConfigDef.py you will have a “ProjectParameters.cfg” file which you will fill up with your target project data, it has: 

cfg_polycount = The maximum number of tris of the model in the scene
cfg_maxmaterials = The maximum number of materials allowed in the models in the scene
cfg_ngons = The number of Ngons allowed (Generally 0 but it is good to know if you have any of them)
cfg_uvsets = The number of UV Sets allowed in the model
cfg_2vertex = The number of close (duplicated) vertices allowed
cfg_vertexthreshold = How much close is considered close to evaluate duplicated vertices

ReportGenerator evaluate the scene. It will compare the data with the .cfg file and generate a report in .csv for you with the actual data and if it passes or not the requirements.

Interactive Window is just copying and pasting your settings of ProjectParameters. When you click run it will run both ConfigDef and ReportGenerator.
 
