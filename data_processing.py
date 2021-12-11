from zip_downloader import get_dataset
import pandas as pd
import numpy as np
import cv2
from tqdm import tqdm
import os


url='http://corsmal.eecs.qmul.ac.uk/data/CCM/train/ccm_train_view2_rgb.zip'
#download the dataset and put it in right directory and unzipping it
#make sure to download .z01 files also
get_dataset(url)
#unzip only .zip files


cols=['id','container id','scenario','background','illumination','width at the top','width at the bottom','height','depth','container capacity']
df=pd.read_csv('./dataset/annotation/annotations.csv')
df=df[cols]
df=df.set_index('id')

train_indexes=[]
test_indexes=[]
indexes=[]

# Divide into train and test test here

for i in df['container id'].unique():
    if i not in [3,6,9]:
        temp_df=df[df['container id']==i]
        temp_df=temp_df.drop_duplicates()
        train_indexes.append(temp_df.index.values)
        indexes.append(temp_df.index.values)
    
for i in [3,6,9]:
    temp_df=df[df['container id']==i]
    temp_df=temp_df.drop_duplicates()
    test_indexes.append(temp_df.index.values)
    indexes.append(temp_df.index.values)
    
indexes=list(np.concatenate(indexes).flat)
train_indexes=list(np.concatenate(train_indexes).flat)
test_indexes=list(np.concatenate(test_indexes).flat)


try:
    path=os.path.join(os.getcwd(),'dataset\\images')
    if not os.path.exists(path):
        os.makedirs(path)
except OSError:
    print ('Error: Creating directory of data')

for video_id in tqdm(indexes,total=len(indexes)): 
    for view in range(1,3):
        currentframe=1
        object_id=int(df.iloc[video_id]['container id'])
        lighting=int(df.iloc[video_id].illumination)
        background=int(df.iloc[video_id].background)
        s=f'{video_id:06d}'+'.mp4'
        #place the rgb video in the trainset folder with separate folder for each view. eg for view 1 the path should be 'trainset\\view1\\rgb\\'
        video_path=os.path.join(os.getcwd(),f'trainset\\view{view:01d}\\rgb\\'+s)
        cam = cv2.VideoCapture(video_path)
        length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
        #print('Total Length',length)
        frames=[0,int(0.1*length),int(0.4*length),int(0.6*length),int(0.99*length)]
        for idx in range(length):
            ret,frame = cam.read()  
            if idx in frames:
                if ret:
                    file_name=f'id{object_id:01d}_f{currentframe:01d}_l{lighting:01d}_b{background:01d}_c{view:01d}_rgb.png'
                    name = os.path.join(path,file_name)
                    #print ('Creating...' + name)  
                    cv2.imwrite(name, frame)
                    currentframe+=1
                else:
                    break
        cam.release()
        cv2.destroyAllWindows()
        
#Image_exist Checking
path=os.path.join(os.getcwd(),'dataset\\images')
print(path)
for object_id in range(1,10):
    for currentframe in range(1,6):
        for lighting in range(2):
            for background in range(2):
                for view in range(1,3):
                    file_name_exist=f'id{object_id:01d}_f{currentframe:01d}_l{lighting:01d}_b{background:01d}_c{view:01d}_rgb.png'
                    if not os.path.exists(os.path.join(path,file_name_exist)):
                        print("File Does Not exist:",os.path.join(path,file_name_exist))
