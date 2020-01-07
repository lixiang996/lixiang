import  os

#os.walk遍历目录后，删除文件和目录
def rmDirAndFile(path):
    #先把各个目录的文件删除完
    for root, dirs, files  in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                os.remove(filepath)
                print("删除文件%s成功" % file)
            except:
                print("删除文件%s异常" % file)
    #再去删除空目录
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dirpath = os.path.join(root,dir)
            try:
                os.rmdir(dirpath)
                print("删除文件夹%s成功" % dirpath)
            except:
                print("删除文件夹%s异常" % dirpath)
                import  traceback
                print(traceback.format_exc())

#os.listdir删除文件
def rmFile(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

# rmFile(r"D:\rpa_learn\good98\good99")
rmDirAndFile(r"D:\rpa_learn\good98\good99")