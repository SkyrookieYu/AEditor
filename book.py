# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 03:40:52 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import librosa # librosa puts PyInstaller into trouble 
# from mimetypes import MimeTypes
import filetype
from mutagen.mp3 import MP3
import backports.tempfile

class Helper(QObject):
    def __init__(self):
        QObject.__init__(self)
        print("Helper.__init__ is called!")   

    def __del__(self):  
        print("Helper.__del__ is called!")        
        
    @staticmethod    
    def getMP3Duration(audioFile): # audioFile should be a full path
        """
        得到 mp3 的时长
        :param audio_path: mp3 路径
        :return:mp3 时长
        """
        # duration = librosa.get_duration(filename=audioFileFullPath)

        # print("PT" + str(mp3duration) + "S")
        # return duration  
        
        audio = MP3(audioFile)
        return audio.info.length
    
    @staticmethod 
    def summarizeMP3Durations(audioFiles):
        """
        得到 mp3 的时长总数
        :param audioFiles: mp3's
        :return: mp3's 总时长
        """
        totalDuration = 0.0
        
        '''
        for audioFile in audioFiles:
            totalDuration += librosa.get_duration(filename=audioFile)
        print("PT" + str(totalDuration) + "S")
        ''' 
        
        for audioFile in audioFiles:
            totalDuration += MP3(audioFile).info.length 
        return totalDuration  
    
    @staticmethod 
    def checkURLAvailability(url):
        """
        Checks that a given URL is reachable.
        :param url: A URL
        :return type: bool
        """
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
    
        try:
            urllib.request.urlopen(request)
            return True
        except urllib.request.HTTPError:
            return False

'''
class Audiobook: PEP + Publication Manifest + TOC
'''


class Audiobook(QObject):
    
    # Singleton Pattern
    _instance = None
    
    @staticmethod
    def getInstance(item_Open):
        if Audiobook._instance is None:
            Audiobook(item_Open)
        return Audiobook._instance
    
    # Private Constructor
    def __init__(self, item_Open):
        if Audiobook._instance is not None:
            raise Exception('Only one instace of Book should exist!')
            return
              
            
            
            
            
            
        Audiobook._instance = self
        self._id = id(self)
            
        if os.path.isdir(item_Open):  
            print("It is a directory")  
            self._is_LPF = False
            self._LPF_File = ''
            self._BOOK_DIR = item_Open
            
        elif os.path.isfile(item_Open):  
            print("It is a normal file")  
            filename, file_extension = os.path.splitext(item_Open)
            if file_extension == '.lpf':
                 self._is_LPF = True
                 self._LPF_File = item_Open
                 
            
            
       
        self._optionNo = 1
        
        
        self._loaded = False
        self._dirty = False
        
        self._PEP_File = ''
        self._CSS_File_List = []
        
        self._TOC = ''
        self._TOC_File = ''
        self._TOC_List = []
        
        self._MANIFEST = ''
        self._MANIFEST_File = ''
        self._MANIFEST_List = []
        
        self._Reading_Order_List = []
        
        self._Booktitle = ''
        
        self._MANIFEST_ID = 'manifest'
        
        # self.helper = Helper(self)
        
        
        
        
        # 21 keys
        self.CONST_MANIFEST_KEY_LIST = ['@context', 
                                        'conformsTo', 
                                        'type', 
                                        'id', 
                                        'url', 
                                        'name', 
                                        'author', 
                                        'readBy', 
                                        'abridged', 
                                        'accessMode', 
                                        'accessModeSufficient', 
                                        'accessibilityFeature', 
                                        'accessibilityHazard', 
                                        'accessibilitySummary', 
                                        'dateModified', 
                                        'datePublished', 
                                        'inLanguage', 
                                        'readingProgression', 
                                        'duration', 
                                        'readingOrder', 
                                        'resources']
    
    @property          
    def dirty(self):
        return self._dirty

    @dirty.setter          
    def dirty(self, value):
        self._dirty = value
        
    @dirty.deleter          
    def dirty(self):
        del self._dirty
        
    @property          
    def loaded(self):
        return self._loaded

    @loaded.setter          
    def loaded(self, value):
        self._loaded = value
        
    @loaded.deleter          
    def loaded(self):
        del self._loaded    
        
    @property          
    def is_LPF(self):
        return self._is_LPF

    @is_LPF.setter          
    def is_LPF(self, value):
        self._is_LPF = value
        
    @is_LPF.deleter          
    def is_LPF(self):
        del self._is_LPF
    
    
    def __del__(self):  
        print("Audiobook: del is called!")
    
    def getID(self):
        return self._id
    
    def openFromDirectory(self, directory):
        '''
        self._is_LPF = False
        self._LPF_File = ""
        self._BOOK_DIR = ""
        '''
        
        print('openFromDirectory')
        # self._BOOK_DIR = directory
        if os.path.exists(directory + "/index.html"):
            print("\"index.html\" exists: PEP is available!\n",  "*" * 70, )
            self._PEP_File = "index.html"
            
            soup = BeautifulSoup(open(directory + r"/index.html", encoding="utf-8"), features='html5lib') # html5lib html.parser
            link = soup.select_one('link[rel=\"publication\"]')
            if link:
                href = link.attrs["href"]
                matchInternalID = re.match('^#(\w+)', href)
                if matchInternalID:
                    print(matchInternalID.group(1))
                    manifest = soup.select_one('script[id=\"' + matchInternalID.group(1) + '\"]') 
                    if manifest: # <script type="application/ld+json" id="XXX">
                        if manifest.attrs["type"] == "application/ld+json":
							
                            self._MANIFEST = json.loads(manifest.string)
                            # self.__MANIFEST_File = "index.html"
                            print("MANIFEST ===\n ", "*" * 70, "\n", json.dumps(self._MANIFEST, indent=4))
                        	
                            """                
                            for key in self.CONST_MANIFEST_KEY_LIST:
                                print(key, " = ", self.__MANIFEST[key])
                            """
                else:
                    matchExternalJson = re.match('(\w+\.json$)', href)
                    if matchExternalJson:
                        print(matchExternalJson.group(1))
                        if not os.path.exists(directory + "/" + href):
                            json_files = glob.glob(directory + "/*.json")
                            href = json_files[0].replace(directory + "\\", "")
                        self._MANIFEST_File = href
                        fo = open(directory + "/" + href, 
                                  mode='r', 
                                  encoding="utf-8")
                        print("fo.name = ", fo.name)
                        manifestStr = fo.read()
                        #print("manifestStr = ", "*" * 70, "\n", manifestStr)
                        fo.close()
                        self._MANIFEST = json.loads(manifestStr)
                        print("MANIFEST ===\n", "*" * 70, "\n", json.dumps(self.__MANIFEST, indent=4))  
            
            
            csses = soup.select('head > link[rel=\"stylesheet\"]')
            if csses:
                for css in csses:                
                    href = css.attrs["href"]
                    # css.attrs["href"] = "css/mycss.css"
                    self._CSS_File_List.append(href)
                print(self._CSS_File_List)
            
            csses = soup.select('head > [name=\"stylesheet\"]')
            if csses:
                for css in csses:                
                    src = css.attrs["src"]
                    self._CSS_File_List.append(src)
                print(self._CSS_File_List)
            
                    
            booktitle = soup.select_one('head > title')
            if booktitle:
                print(booktitle.text)
                self._Booktitle = booktitle.text
                            
            toc = soup.select_one('[role="doc-toc"]') # <XXX role="doc-toc"> XXX is usually 'nav'
            if toc: 
                print('toc = ', toc)
                print('toc.name =', toc.name)
                print("TOC ===\n", "*" * 70, "\n", toc)
                self.__TOC = toc
                # self.__TOC_File = "index.html"
                 
                li_tags = toc.find_all('li')  

                current_tag = toc
                parent_tag = None
                
                for child in toc.recursiveChildGenerator(): # https://www.it1352.com/330662.html
                    name = getattr(child, "name", None)
                    if name is not None:
                        print("Child tagname = ", name, " parent tagname = ", child.parent.name," \n")
                        if name == 'li':
                            print('LI found!\n')
                            break
                    elif not child.isspace(): # leaf node, don't print spaces
                    #else:
                        print(child)   
                             
                for li_tag in li_tags:
                    a_tag = li_tag.find('a')
                    self._TOC_List.append((a_tag['href'], a_tag.get_text()))
                
                # print("TOC ===\n", "*" * 70, "\n", self.__TOC_List) # print(self.__TOC_List)
            else:
                print("Try to find 'nav' in other .html files.")
                tocFlag = False
                """
                The algorithm here needs to be fixed.
                Old style: parse other html files directly
                Correct(New) style: 
                """
                resources = self.__MANIFEST["resources"]
                if resources:
                    for resource in resources:
                        print(resource.keys())
                        
                        if "rel" in resource.keys() and resource["rel"] == "contents":
                            tocFlag = True
                            print(resource['url'])
                            tocSoup = BeautifulSoup(open(directory + "\\" + resource["url"]), features='html5lib')
                            toc = tocSoup.select_one('[role="doc-toc"]') # eg. <nav role="doc-toc">
                            if toc:
                                print("TOC ===\n", "*" * 70, "\n", toc.get_text())
                                self.__TOC = toc
                                self.__TOC_File = resource["url"]
                                print(self.__TOC_File)

                                li_tags = toc.find_all('li')  
                        
                                for child in toc.recursiveChildGenerator(): # https://www.it1352.com/330662.html
                                    name = getattr(child, "name", None)
                                    if name is not None:
                                        print("Child tagname = ", name, "\n")
                                        if name == 'li':
                                            print('LI found!\n')
                                            break
                                    elif not child.isspace(): # leaf node, don't print spaces
                                    #else:
                                        print(child)   
                                        
                                for li_tag in li_tags:
                                    a_tag = li_tag.find('a')
                                    self.__TOC_List.append((a_tag['href'], a_tag.get_text()))
                                
                                print(self.__TOC_List)
                                
                                tocFlag = True
                                break  
                        
                              

                    
        elif os.path.exists(directory + "/publication.json"):           
            """
            The algorithm here needs to be fixed.
            Old style: parse other html files to find toc first
            Correct(New) style: no index.html, then publication.json must appear
            """
            
            with open(directory + "/publication.json") as manifest_file: 
                self.__MANIFEST = json.load(manifest_file)
                self.__MANIFEST_File = "publication.json"
                print("MANIFEST ===\n", "*" * 70, "\n", self.__MANIFEST)  
            
            resources = self.__MANIFEST["resources"]
            if resources:
                for resource in resources:
                    # print(resource.keys())
                    
                    if "rel" in resource.keys() and resource["rel"] == "contents":
                        print(resource['url'])
                        tocSoup = BeautifulSoup(open(directory + "\\" + resource["url"]), features='html5lib')
                        toc = tocSoup.select_one('[role="doc-toc"]') # eg. <nav role="doc-toc">
                        if toc:
                            print("TOC ===\n", "*" * 70, "\n", toc.get_text())
                            self.__TOC = toc
                            self.__TOC_File = resource["url"]
                            print(self.__TOC_File)

                            li_tags = toc.find_all('li')  
                    
                            for child in toc.recursiveChildGenerator(): # https://www.it1352.com/330662.html
                                name = getattr(child, "name", None)
                                if name is not None:
                                    print("Child tagname = ", name, "\n")
                                    if name == 'li':
                                        print('LI found!\n')
                                        break
                                elif not child.isspace(): # leaf node, don't print spaces
                                    print(child)   
                                    
                            for li_tag in li_tags:
                                a_tag = li_tag.find('a')
                                self.__TOC_List.append((a_tag['href'], a_tag.get_text()))
                            
                            print(self.__TOC_List)
                            
                            tocFlag = True
                            break   
        else: # Not by the W3C rules
            # htmls = glob.glob(directory + "/*.html")
            print("Fatal error!")   
            return
                           
        if self.__TOC or self.__MANIFEST:
            self.__loaded = True
            # self.__dirty = False
            self.determineOption()
            print(self.__optionNo)
            
            # For Test
            self.__dirty = True
    
if __name__ == '__main__':
    #app = QApplication(sys.argv)
    b = Audiobook.getInstance("D:\\Github\\audiobooks-samples\\case1")
    print(b)
    print(b.getID())
    print(b.is_LPF)
    #sys.exit(app.exec_())