import os
import time

class format:
    
    def erase_file(rootDir):
        
        for dirName, subdirList, fileList in os.walk(rootDir):
            
            for fname in sorted(fileList, key=len):
            
                if not fname.endswith(".pdf") and not fname.endswith(".sor"):
                    os.remove(os.path.join(dirName + '\\' + fname))
                    print('archivos eliminado:' + '\t%s' % dirName + '\\' + fname)
                    time.sleep(0.1)
            
    def renamefolder(rootDir):
        
        for dirName2 in sorted(subdirList, key=len):
            src = dirName2
            dst = "F" + str(i)
            os.rename(src, dst)
            i += 1
            print('archivos Renombrados:'+src+"=="+dst)
      
    

