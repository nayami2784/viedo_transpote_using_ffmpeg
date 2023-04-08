import os
from tqdm import tqdm
#将给出路径下的所有.MP4类型文件的文件名输出为list
def getVideoName(path):
    f_list = os.listdir(path)
    VideoNames=[]
    for i in f_list:
         # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.MP4' or os.path.splitext(i)[1] == '.mp4':
            VideoNames.append(i)
    return VideoNames


# #转置函数
def transpote1(inputdir,outputdir,VideoNames):

    for VideoName in VideoNames:
        command = 'ffmpeg -i "{inputpath}" -c copy -metadata:s:v:0 rotate=90  "{outputpath}"'.format(inputpath = inputdir +'/'+ VideoName,outputpath = outputdir +'/'+ VideoName)
        os.system(command)

#转置函数2
# (输入文件的所有全局元数据，复制到输出文件中，包括日期、摄像机详细信息等)

def transpote2(inputdir,outputdir,VideoNames):

    with tqdm(total=len(VideoNames),desc='转换进度') as pbar:
        for VideoName in VideoNames:
            #cmd 重定向输出,将错误消息重定向到 NUL (2> nul)
            #在命令前面加echo.| 就可以自动回车，如果要自动输入yes就这样echo yes|
            command = 'echo.| ffmpeg -i "{inputpath}" -map_metadata 0 -metadata:s:v rotate="90" -codec copy  "{outputpath}" 2> nul'.format(inputpath = inputdir +'/'+ VideoName,outputpath = outputdir +'/'+ VideoName)
            os.system(command)
            pbar.update(1)

        


inputdir = 'E:/DCIM/102CANON'#输入文件夹
outputdir = 'G:/videos/3-4'#输出文件夹


VideoNames = getVideoName(inputdir)#视频名称 
transpote2(inputdir,outputdir,VideoNames)



