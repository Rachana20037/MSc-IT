# from scipy.misc import imread
import pandas as pd
import imageio.v2
from matplotlib.pyplot import imread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
sDataBaseDir ='E:/DS_28/temp'
f=0
for file in os.listdir(sDataBaseDir):
    if file.endswith(".jpg"):
        f +=1
        sInputFileName=os.path.join(sDataBaseDir,file)
        print('Process :',sInputFileName)
        InputData= imageio.imread(sInputFileName, format='.jpg')
        #InputData=imread(sInputFileName,flatten=False,mode='RGBA')
        print('Input Data Values ========================')
        print('X: ' ,InputData.shape[0])
        print('Y: ' ,InputData.shape[1])
        print('RGBA: ' ,InputData.shape[2])
        print('===========================================')
        ProcessRawData=InputData.flatten()
        y=InputData.shape[2] +2
        x=int(ProcessRawData.shape[0]/y)
        ProcessFrameData = pd.DataFrame(np.reshape(ProcessRawData,(x,y)))
        ProcessFrameData['Frame']=file
        print('===========================================')
        print('Process Data values ========================')
        print('============================================')
        plt.imshow(InputData)
        plt.show()

        if f==1:
            ProcessData =ProcessFrameData
        else:
            ProcessData=ProcessData._append(ProcessFrameData)
if f>0:
    sColumns =['XAxis','YAxis', 'Red','Green','Blue','Alpha','FrameName']
    ProcessData.columns=s.Columns
    print('===================================================')
    ProcessFrameData.index.names=['ID']
    print('Rows :',ProcessData.shape[0])
    print('Columns:',ProcessData.shape[1])
    print('===============================================')
    #ouput==============================================
    Outputdata =ProcessData
    print('Storing File')
    sOutputFileName ='E:/DS_28/HORUS-Movie-Frame.csv'
    OutputData.to.csv(sOutputFileNmae,index=False)
print('===============================================')
print('Processed :',f,'frames')
print('===============================================')
print('Movies to HORUS =Done')
print('===============================================')

    
























            
