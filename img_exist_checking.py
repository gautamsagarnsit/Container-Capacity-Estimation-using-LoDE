import os
path=os.path.join(os.getcwd(),'code\\trainset\\train_images_1')
print(path)
for object_id in range(1,10):
    for currentframe in range(1,6):
        for lighting in range(2):
            for background in range(2):
                for view in range(2,3):
                    file_name_exist=f'id{object_id:01d}_f{currentframe:01d}_l{lighting:01d}_b{background:01d}_c{view:01d}_rgb.png'
                    if not os.path.exists(os.path.join(path,file_name_exist)):
                        print("File Does Not exist:",os.path.join(path,file_name_exist))
