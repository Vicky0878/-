# coding=utf-8 
import maya.cmds as cmd
import maya.mel as mel
import os
import webbrowser

def openBrowserBatchExpor():
    url = 'http://www.321suc.com/'
    webbrowser.open(url)

def BatchExportWin():
    window1 = 'BatchExportWindow1'
    if cmd.window(window1, q= True, ex=True):
        cmd.deleteUI(window1)

    cmd.window(window1, t=u"MAYA批量导出fbx obj ma mb插件", mb=1)#标题窗口
    cmd.columnLayout(adj=1)#整个组件宽度
    #cmd.separator(h=10)
    #cmd.text(l = u'选择模型或者组,选择导出的格式')
    #cmd.text(l = u'会按照选择的对象的名称命名导出后的文件名称')
    #cmd.text(l = u'如果选择的模型有同名称,会重命名选择的模型')
    #cmd.text(l = u'会保留层级关系与子级')
    cmd.separator(h=5)#隔开行

    #cmd.text(l = u'选择需要导出的格式')#提示字
    cmd.optionMenu('BatchExportWindow1_optionMenuGrp_a1')
    cmd.menuItem(l='fbx')
    cmd.menuItem(l='obj')
    cmd.menuItem(l='ma')
    cmd.menuItem(l='mb')
    cmd.separator(h=5)
    cmd.button(l=u'导出',c='BatchExport.BatchExport_data()')
    cmd.separator(h=5)
    #cmd.button(l=u'更多',c='BatchExport.openBrowserBatchExpor()')网址

    cmd.window(window1,e=True, w=300, h=250)
    cmd.showWindow(window1)

def Check_the_same_name_and_rename():
    sel = cmd.ls(sl=1,sn=1)
    shortNames = []
    for i in sel:
        split1 = i.split('|')[-1]
        shortNames.append(split1)

    newNameAll = []
    for n in shortNames:
        newName = mel.eval('tolower("%s")' %n)
        newNameAll.append(newName)

    ne = [val for val in list(set(newNameAll)) if newNameAll.count(val) > 1]

    if len(ne) > 0:
        long_s_name = []
        for i in ne:
            for n in sel:
                if i == mel.eval('tolower("%s")' %n.split('|')[-1]):
                    long_s_name.append(n)

        for r in range(len(long_s_name)):
            cmd.rename(long_s_name[r],(long_s_name[r].split('|')[-1] + str(r)))

def BatchExport_data():
    global isfile_Exists_name
    isfile_Exists_name = ''
    optionMenu1 = cmd.optionMenu('BatchExportWindow1_optionMenuGrp_a1',q=1,v=1)
    filename1 = cmd.fileDialog2(fileMode=2,ds=1,okc=u'确定',caption=u'选择')
    motionfile = filename1[0]

    Check_the_same_name_and_rename()
    sel = cmd.ls(sl=1)
    list1 = os.listdir(motionfile)
    os.mkdir(motionfile + '/' + str(len(list1)))

    path_file = motionfile + '/' + str(len(list1)) + '/'

    for i in sel:
        path_name = path_file + i
        cmd.select(i,r=1)
        if optionMenu1 == 'fbx':
            mel.eval('file -force -options "v=0;" -typ "FBX export" -pr -es "%s.fbx";' %path_name)

        if optionMenu1 == 'obj':
            mel.eval('file -force -typ "OBJexport" -pr -es "%s.obj";' %path_name)

        if optionMenu1 == 'ma':
            mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "%s.ma";' %path_name)

        if optionMenu1 == 'mb':
            mel.eval('file -force -options "v=0;" -typ "mayaBinary" -pr -es "%s.mb";' %path_name)

