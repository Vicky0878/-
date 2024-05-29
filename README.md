![tb_image_share_1716939822707 jpg](https://github.com/Vicky0878/MAYA-Batch-Export-script/assets/125170736/e4ad6d1e-54e0-4031-b009-f8dbfd0e9c15)

Batch Export is a simple maya plugin that supports batch export of fbx obj ma mb files if you like to download it and use it. It works in the 2023maya version

1: Installation method

Copy the BatchExport.py file into the C:\ documents \maya\scripts folder

2020 The following maya runs the following code in the python bar of the maya script editor:
import BatchExport
reload(BatchExport)
BatchExport.BatchExportWin()

maya 2022 and up runs the following code in the python bar of the maya script editor:
import importlib
import BatchExport
importlib.reload(BatchExport)
BatchExport.BatchExportWin()

2: Use method:

Select the model you want to export, select the format you want to export, and click Export

A window will open, select which folder you want to save to, and then click Select Folder

A new folder is created within the selected folder (the folder name is the number of files in the current folder). You don't need to understand this, just know that a new folder will be created, the role of this folder is to prevent different scenarios from exporting files with the same name overwriting the original)

The selected model will be exported to a newly created folder with the exported file name of the model you have in maya

If the model you select has a duplicate name, the model is first renamed within the scene and then exported# -

