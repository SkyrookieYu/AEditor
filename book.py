# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 03:40:52 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""



from bs4 import BeautifulSoup
import filetype
import glob
import json
import os
import re
import sys
from mutagen.mp3 import MP3
import backports.tempfile
from multipledispatch import dispatch
import zipfile

from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import librosa # librosa puts PyInstaller into trouble 
# from mimetypes import MimeTypes


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
    
    _PEP_OPTION_1 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        {}
        <link rel=\"publication\" href=\"#{}\">
        <script type=\"application/ld+json\" id=\"{}\">
{}
        </script>
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    _PEP_OPTION_2 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        {}
        <link rel=\"publication\" href=\"{}\">
    </head>
    <body>
        <h1>{}</h1>
    </body>
</html>"""   

    _TOC_OPTION_2 = """<!DOCTYPE html>    
<html>
    <head>
        <title>Table of Contents</title>
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""  

    _PEP_OPTION_3 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        {}
        <link rel=\"publication\" href=\"{}\">
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    _TOC_OPTION_4 = """<!DOCTYPE html>    
<html>
    <head>
        <title>Table of Contents</title>
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""     

    # Singleton Pattern
    _instance = None
    
    @staticmethod
    @dispatch(str)
    def getInstance(item_Open):
        if Audiobook._instance is None:
            Audiobook(item_Open)
        return Audiobook._instance
    
    @staticmethod
    @dispatch()
    def getInstance():
        '''
        if Audiobook._instance is None:
            Audiobook()
        '''
        return Audiobook._instance
    
    '''
    {"saveDir": saveDir, "bookTitle": bookTitle, "author": author, "publisher": publisher, "readBy": readBy}
    '''
    @dispatch(dict) # Private Constructor
    def __init__(self, dict_New):
        super().__init__(None)
        if Audiobook._instance is not None:
            raise Exception('Only one instace of Book should exist!')
            return
              
        Audiobook._instance = self
        self._id = id(self)
            


        

        self._optionNo = 1
        
        
        self._loaded = False
        self._dirty = False
        
        self._PEP_File = ''
        
        self._CSS_File_List = []
        
        self._TOC = ''
        self._TOC_File = ''
        self._TOC_List = []
        
        self._MANIFEST = {}
        self._MANIFEST_File = ''
        self._MANIFEST_List = []
        
        self._Reading_Order_List = []
        
        
        
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
        
        self._BOOK_DIR = dict_New.get("saveDir", "")
        self._Booktitle = dict_New.get("bookTitle", "")
        self._MANIFEST["author"] = dict_New.get("author", "")
        self._MANIFEST["publisher"] = dict_New.get("publisher", "")
        self._MANIFEST["readBy"] = dict_New.get("readBy", "")
    
        
    
    
    
    
    
    @dispatch(str) # Private Constructor
    def __init__(self, item_Open):
        super().__init__(None)
        
        if Audiobook._instance is not None:
            raise Exception('Only one instace of Book should exist!')
            return
              
        Audiobook._instance = self
        self._id = id(self)
            
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
        # self._MANIFEST_Dict = {}
        
        # self._Reading_Order_List = []
        
        self._Booktitle = ''
        
        self._MANIFEST_ID = 'manifest'
        
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
        
        
        if os.path.isdir(item_Open):  
            print("It is a directory")  
            self._is_LPF = False
            self._LPF_File = ''
            self._BOOK_DIR = item_Open
            self.openFromDirectory(item_Open)
            
        elif os.path.isfile(item_Open):  
            print("It is a normal file")  
            filename, file_extension = os.path.splitext(item_Open)
            if file_extension == '.lpf':
                 self._is_LPF = True
                 self._LPF_File = item_Open
                 self.openFromLPF(item_Open, 'D:\\lpf_temp' + '\\' + QUuid.createUuid().toString()) # QStandardPaths.writableLocation(QStandardPaths.CacheLocation))
                 self.openFromDirectory(self.getBookDir())
    
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
        
    def getBookDir(self):
        return self._BOOK_DIR
    
    def getID(self):
        return self._id

    def setManifestDict(self, m):
        self._MANIFEST = m
    
    def getManifestDict(self):
        return self._MANIFEST
    
    def getTOCFile(self):
        return self._TOC_File

    def setTOCList(self, t):
        self._TOC_List = t

    def getTOCList(self):
        return self._TOC_List
    
    def setCoverDict(self, dict_Cover):
        if self._MANIFEST.get("resources") is None:
            self._MANIFEST["resources"] = [dict_Cover] 
            return
        
        for i in len(self._MANIFEST["resources"]):
            if self._MANIFEST["resources"][i].get("rel") is not None and self._MANIFEST["resources"][i].get("rel") == "cover":
                self._MANIFEST["resources"].remove(i)
                break
        self._MANIFEST["resources"].append(dict_Cover)        

            
    
    def getCoverDict(self):
        if 'resources' in self.getManifestDict():
            for item in self.getManifestDict()["resources"]:
                if item.get("rel") is not None and item.get("rel") == "cover":
                    return item
        return {}  
    
    def setSupplementalList(self, sList):  
        if self._MANIFEST.get("resources") is None:
            self._MANIFEST["resources"] = sList 
            return
        
        # self._MANIFEST["resources"] = []
        for s in sList:
            self._MANIFEST["resources"].append(s)
        
        
        
    def getSupplementalList(self):
        slist = []
        if 'resources' in self.getManifestDict():
            for item in self.getManifestDict()["resources"]:
                if item.get("rel") is not None and item.get("rel") == "cover":
                    continue
                elif item.get("name") is not None and item.get("name") == "Primary Entry Page":
                    continue
                elif item.get("name") is not None and item.get("name") == "Table of Contents":
                    continue
                else:
                    slist.append(item)
        return slist    

    def setReadingOrderList(self, rList):
        self._MANIFEST["readingOrder"] = rList
    
    def getReadingOrderList(self):
        if 'readingOrder' in self.getManifestDict():
            return self.getManifestDict()['readingOrder']
        return [] 
    
    @pyqtSlot()  
    def on_action_Save_Audiobook_triggered(self):  
        print("on_action_Save_LPF_triggeredd")
        if self.is_LPF:
            print("Save as a LPF file!")
            self.saveIntoDirectory(self.getBookDir())
            fdlg = QFileDialog()
            fdlg.setFileMode(QFileDialog.AnyFile)
            
        
            saveLPFName, _ = fdlg.getSaveFileName(self, 'Save As Audiobook(lpf)', '.', 'Audiobooks (*.lpf)')
            if saveLPFName:
                print(saveLPFName)
                self.saveAsLPF(saveLPFName)
                return
            
            
            
            
            
            return
        else:
            self.saveIntoDirectory(self.getBookDir())
            
            
            return
    
    def checkResources(self):
        errorList = []
        for resource in self._MANIFEST['resources']:
            if 'url' in resource.keys():
                print(resource['url'])
                url = resource['url']
                m = re.search(r'^https?://', url) 
                if m: # http(s)://
                    res = Helper.checkURLAvailability(url)
                    print(res)
                    if not res:
                        errorList.append(url)
                else: # local
                    print('not a URL')
                    directory = self._BOOK_DIR
                    if os.path.exists(directory + "/" + url):
                        print('{} exists'.format(directory + "\\" + url))
                    else:
                        print('{} doesn\'t exist'.format(directory + "\\" + url))
                        errorList.append(directory + "\\" + url)
        return errorList
                                    
    def saveIntoDirectory(self, directory = None):
        def getTOCBlock(data, level = 0):
            fullTOCString = '\t' * (3 + level*2) + "<ol>\n"
            for i in range(len(data)):
                dict_TOC = data[i]
                lvl = dict_TOC["level"]
                href = dict_TOC["href"]
                title = dict_TOC["title"]
                fullTOCString += '\t' * (3 + level*2 + 1) + '<li><a href=\"' + href + '\">' + title + '</a></li>\n'              
                if dict_TOC["children"] != []:
                    fullTOCString += writeTOC(dict_TOC["children"], level + 1)
                else:
                    pass
            fullTOCString += '\t' * (3 + level*2) + "</ol>"
            return fullTOCString
        
        print('saveIntoDirectory')
        errorList = self.checkResources()
        if not errorList:
            print('Resources check passed')
        else:
            print('Not-found list : {}'.format(errorList))
        if directory is None:
            directory = self._BOOK_DIR
        
        if self._optionNo == 1:
            print("self._optionNo = 1")
            fullManifestContent = ""
            data = self.getTOCList()
            tocString = getTOCBlock(data, 0)
            
            metadata = self.getgetManifestDict()
            
            
            """
            <meta name=\"stylesheet\" src=\"{}\">
            """
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)
            fullHTMLContent = self._PEP_OPTION_1.format(self._Booktitle, 
                                                    fullCSSContent, 
                                                    self._MANIFEST_ID,
                                                    self._MANIFEST_ID,
                                                    json.dumps(self._MANIFEST, indent=4), # json.dumps(self.__MANIFEST)
                                                    self._Booktitle,
                                                    tocString)
            print(fullHTMLContent)
            with open(directory + "\\" + "index.html", "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(fullHTMLContent)

        elif self._optionNo == 2:
            print("self._optionNo = 2")
            
            # fullManifestContent = ""
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)
            fullPEPContent = self._PEP_OPTION_2.format(self._Booktitle,
                                                       fullCSSContent,
                                                       self._MANIFEST_File, # json.dumps(self.__MANIFEST)
                                                       self._Booktitle)
            
            with open(directory + "\\" + "index.html", "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(fullPEPContent)
                
            data = self.getTOCList()
            tocString = getTOCBlock(data, 0)
            
            fullTOCContent = self._TOC_OPTION_2.format(self._Booktitle,
                                                       tocString)
            
            with open(directory + "\\" + self._TOC_File, "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(fullTOCContent)            
            
            self._MANIFEST["resources"].append({"type" : "LinkedResource", "encodingFormat": "text/html", "name":"Table of Contents", "rel": "contents", "url": self.getTOCFile() or "toc.html"})
            with open(directory + "\\" + self._MANIFEST_File, "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(json.dumps(self._MANIFEST, indent=4))                
            
            
            
        elif self._optionNo == 3:
            print("self._optionNo = 3")
            
            
            
            
            data = self.getTOCList()
            tocString = getTOCBlock(data, 0)
              
                
            # fullPEPContent = ""
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)
            fullPEPContent = self._PEP_OPTION_3.format(self._Booktitle,
                                                       fullCSSContent,
                                                       self._MANIFEST_File, # json.dumps(self.__MANIFEST)
                                                       self._Booktitle,
                                                       tocString)
            
            with open(directory + "\\" + "index.html", "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(fullPEPContent)
            # Todo
            '''
            data = self.getManifestDict()
            manifestString = getManifestBlock
            '''
            
            
            with open(directory + "\\" + self._MANIFEST_File, "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(json.dumps(self._MANIFEST, indent=4))               
            
            
            
        elif self._optionNo == 4:
            print("self._optionNo = 4")   
            
            
            data = self.getTOCList()
            tocString = getTOCBlock(data, 0)
            
            fullTOCContent = self._TOC_OPTION_4.format(self._Booktitle,
                                                       tocString)
            
            with open(directory + "\\" + self._TOC_File, "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(fullTOCContent)               
            
            
            with open(directory + "\\" + self._MANIFEST_File, "w", encoding="utf-8") as f:
            # 将爬取的页面              
                f.write(json.dumps(self._MANIFEST, indent=4))               
                        
            
            
            
        elif self._optionNo == 5:
            print("self._optionNo = 5")  
            
            with open(directory + "\\" + self._MANIFEST_File, "w", encoding="utf-8") as f:         
                f.write(json.dumps(self._MANIFEST, indent=4))    
        
        else:
            print("self._optionNo = ???")  
            
        if self.dirty:
            self.dirty = False
            
    def checkResources(self):
        errorList = []
        for resource in self._MANIFEST['resources']:
            if 'url' in resource.keys():
                print(resource['url'])
                url = resource['url']
                m = re.search(r'^https?://', url) 
                if m: # http(s)://
                    res = self.helper.checkURLAvailability(url)
                    print(res)
                    if not res:
                        errorList.append(url)
                else: # local
                    print('not a URL')
                    directory = self._BOOK_DIR
                    if os.path.exists(directory + "/" + url):
                        print('{} exists'.format(directory + "\\" + url))
                    else:
                        print('{} doesn\'t exist'.format(directory + "\\" + url))
                        errorList.append(directory + "\\" + url)
        return errorList
    
    def determineOption(self):
        if self._PEP_File and not self._TOC_File and not self._MANIFEST_File:
            self._optionNo = 1
        elif self._PEP_File and self._TOC_File and self._MANIFEST_File:
            self._optionNo = 2
        elif self._PEP_File and not self._TOC_File and self._MANIFEST_File:
            self._optionNo = 3
        elif not self._PEP_File and self._TOC_File and self._MANIFEST_File:
            self._optionNo = 4
        elif not self._PEP_File and not self._TOC_File and self._MANIFEST_File:
            self._optionNo = 5
            
    def setOptionAndFilenames(self, opt_No, pep_file, toc_file, manifest_file):
        print("New an audiobook")
        self._optionNo = opt_No
        self._PEP_File = pep_file
        self._TOC_File = toc_file
        self._MANIFEST_File = manifest_file
    
    def openFromLPF(self, lpf_file, unzip_destination):
        """
        self.__is_LPF = False
        self.__LPF_File = ""
        self.__BOOK_DIR = ""
        """
        print('openFromLPF')
               
        unzip_files = zipfile.ZipFile(lpf_file, mode='r', compression=zipfile.ZIP_DEFLATED)
        print(unzip_files)
        for f in unzip_files.namelist(): 
            print(f)
        
        # unzip_files.extractall(r'D:/Github/AudiobookEditor/unzip_files')
        unzip_files.extractall(unzip_destination)
        unzip_files.close()
        self._is_LPF = True
        self._LPF_File = lpf_file
        self._BOOK_DIR = unzip_destination
        return True    
    
    def openFromDirectory(self, directory):
        '''
        self._is_LPF = False
        self._LPF_File = ""
        self._BOOK_DIR = ""
        '''
        
        def dictify(ol, level, tagName = "ol"):
            childrenList = []
            lvl = level
        
            for li in ol.find_all("li", recursive = False):
                result = {}
                a_tag = li.find('a', recursive = False)
                
                result['level'] = lvl
                result['href'] = a_tag['href']
                result['title'] = a_tag.get_text()
                
                next_ol = li.find(tagName, recursive = False)
                if next_ol:
                    result['children'] = dictify(next_ol, lvl + 1)
                else:
                    result['children'] = []
                childrenList.append(result)
            return childrenList
        
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
                        print("MANIFEST ===\n", "*" * 70, "\n", json.dumps(self._MANIFEST, indent=4))  
            
            
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
                self._TOC = toc
                # self.__TOC_File = "index.html"
                

                ol = toc.find('ol', recursive = False)
                ul = toc.find('ul', recursive = False)
                if ol:
                    self._TOC_List = dictify(ol, 0)
                elif ul:
                    self._TOC_List = dictify(ul, 0, tagName = "ul")
                print("dictify ===\n", "*" * 70, "\n", self._TOC_List)
                
                # print("TOC ===\n", "*" * 70, "\n", self.__TOC_List) # print(self.__TOC_List)
            else:
                print("Try to find 'nav' in other .html files.")
                tocFlag = False
                """
                The algorithm here needs to be fixed.
                Old style: parse other html files directly
                Correct(New) style: 
                """
                resources = self._MANIFEST.get("resources", None)
                if resources:
                    for resource in resources:
                        print(resource.keys())
                        
                        if "rel" in resource.keys() and resource["rel"] == "contents":
                            tocFlag = False
                            print(resource['url'])
                            tocSoup = BeautifulSoup(open(directory + "\\" + resource["url"], encoding="utf-8"), features='html5lib')
                            toc = tocSoup.select_one('[role="doc-toc"]') # eg. <nav role="doc-toc">
                            if toc:
                                print("TOC ===\n", "*" * 70, "\n", toc.get_text())
                                self._TOC = toc
                                self._TOC_File = resource["url"]
                                print(self._TOC_File)

                               
                                ol = toc.find('ol', recursive = False)
                                ul = toc.find('ul', recursive = False)
                                if ol:
                                    self._TOC_List = dictify(ol, 0)
                                elif ul:
                                    self._TOC_List = dictify(ul, 0, tagName = "ul")
                                print("dictify ===\n", "*" * 70, "\n", self._TOC_List)
                                
                                tocFlag = True
                                break  
                        
                              

                    
        elif os.path.exists(directory + "/publication.json"):           
            """
            The algorithm here needs to be fixed.
            Old style: parse other html files to find toc first
            Correct(New) style: no index.html, then publication.json must appear
            """
            
            with open(directory + "/publication.json", encoding="utf-8") as manifest_file: 
                self._MANIFEST = json.load(manifest_file)
                self._MANIFEST_File = "publication.json"
                print("MANIFEST ===\n", "*" * 70, "\n", self._MANIFEST)  
            
            resources = self._MANIFEST["resources"]
            if resources:
                for resource in resources:
                    # print(resource.keys())
                    
                    if "rel" in resource.keys() and resource["rel"] == "contents":
                        print(resource['url'])
                        tocSoup = BeautifulSoup(open(directory + "\\" + resource["url"], encoding="utf-8"), features='html5lib')
                        toc = tocSoup.select_one('[role="doc-toc"]') # eg. <nav role="doc-toc">
                        if toc:
                            print("TOC ===\n", "*" * 70, "\n", toc.get_text())
                            self._TOC = toc
                            self._TOC_File = resource["url"]
                            print(self._TOC_File)
                            
                            ol = toc.find('ol', recursive = False)
                            ul = toc.find('ul', recursive = False)
                            if ol:
                                self._TOC_List = dictify(ol, 0)
                            elif ul:
                                self._TOC_List = dictify(ul, 0, tagName = "ul")
                            print("dictify ===\n", "*" * 70, "\n", self._TOC_List)
                            
                            tocFlag = True
                            break   
        else: # Not by the W3C rules
            # htmls = glob.glob(directory + "/*.html")
            print("Fatal error!")   
            return
                           
        if self._TOC or self._MANIFEST:
            self._loaded = True
            # self.__dirty = False
            self.determineOption()
            print(self._optionNo)
            
            # For Test
            self._dirty = True
    
if __name__ == '__main__':
    #app = QApplication(sys.argv)
    b = Audiobook.getInstance("D:\\Github\\audiobooks-samples\\case1")
    print(b)
    print(b.getID())
    # b.openFromDirectory("D:\\Github\\audiobooks-samples\\case1")
    print(b.is_LPF)
    print(b.getManifestDict())
    print(b.getTOCList())
    print(b.getCoverDict())
    print(b.getReadingOrderList())
    print(b.getSupplementalList())
    #sys.exit(app.exec_())