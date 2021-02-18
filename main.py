import os
import time
import shutil


class format_File():
    
    def __init__(self,r,o):
        self.r = r
        self.o = o
        os.chdir((self.r))
        
    def erase_file(self):
        rootDir = self.r
        i = 1
        for dirName, subdirList, fileList in os.walk(rootDir):

            for fname in sorted(fileList, key=len):

                if not fname.endswith(".pdf") and not fname.endswith(".sor"):

                    os.remove(os.path.join(dirName + '\\' + fname))
                    print('Limpiando archivos innecesario:' + '\t%s' %
                          dirName + '\\' + fname)
                    time.sleep(0.1)
   
    def rename_folder(self):    
        rootDir = self.r
        i = 1
        for dirName, subdirList, fileList in os.walk(rootDir):
            for dirName2 in sorted(subdirList, key=len):
                src = dirName2
                dst = "F" + str(i)
                os.rename(src, dst)
                i += 1
                print('Asignando numero de fibra a carpertas:'+src+"=="+dst)
                time.sleep(0.1)

class move_File():
    
    def __init__(self,r,o):
        self.r = r
        self.o = o
    
    def seperate_Files(self):
        rootDir = self.r
        r = rootDir
        shutil.copytree(r,(r+"\\"+"PDF"))
        shutil.copytree(r,(r+"\\"+"SOR"))
        shutil.rmtree((r+"\\"+"PDF"+"\\"+"SOR"),ignore_errors=True)
        shutil.rmtree((r+"\\"+"SOR"+"\\"+"PDF"),ignore_errors=True)
        print("!!!!carpetas PDF y SOR creadas con Exito!!!!!")
        time.sleep(0.2)
    
        for dirName, subdirList, fileList in os.walk(rootDir):

            print('Asignando numero de fibra a carpertas: %s' % dirName)
        #recorre la carpeta y argrega su fibra correposdiente a cada una
            for Subname in sorted(subdirList, key=len):
                if not Subname.endswith("PDF") and not Subname.endswith("SOR"):
                    shutil.rmtree( os.path.join(rootDir) + '\\' + Subname,ignore_errors=True)
               # os.remove(os.path.join (subdirList) + '\\' + fname)
        print("!!!!carpetas PDF y SOR creadas con Exito!!!!!")
        time.sleep(0.2)   
                    
if __name__ == '__main__':
    
    a = input("ingrese ubicacion:")
    b = a
    #f = format_File(a,b)
    s = move_File(a,b)
    s.seperate_Files()
    #f.erase_file()
    #f.rename_folder()