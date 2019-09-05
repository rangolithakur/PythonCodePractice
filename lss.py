import os as _os
import sys as _sys
import re as _re
import glob as _glob
import argparse as _argparse
import logging as _logging

from collections import Counter, namedtuple

_logging.basicConfig(level=_logging.INFO)


class LSS(object):
    r"""
    Class to read files from directory and list
    number of files, filename and range if available.
    How to execute in cmd prompt-
    >>> filename -p option path to files
    >>> lss.py -p C:\Users\swagat\Desktop\githubCode\ddu_coding

    Input Directory contains-
    -rw-r--r-- 1 system 197608 0 May 21 06:56 elem.info
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0112.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0113.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0114.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0116.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0117.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0118.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0119.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0120.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:57 sd_fx29.0121.rgb
    -rw-r--r-- 1 system 197608 0 May 21 06:59 strange.xml
    """
    def __init__(self):
        self.path = None
        self.filename = None
        self.fileInfo = namedtuple('fileInfo', 'size name fRange')

    def run(self, path=None, verbose=None):
        """
        helper method to receive command line argument
        """
        self.path=path
        if self.path:
            self._filesInfo()

    def _getArguments(self):
        """
        helper method to parsing command line argument
        """
        parser = _argparse.ArgumentParser(description='Process input directory')
        parser.add_argument('-p', '--path', required=True, action='store', help='input path to list files', type=str)
        parser.add_argument('-v', '--verbose', required=False, help='This tool list all the files, file count, range if present, requires input directory to list files', action='store_true')

        args= vars(parser.parse_args(_sys.argv[1:]))
        
        return args

    def _filesInfo(self):
        """
        helper method to fetch frame range, file size, filenames
        and display the data.
        """
        #few local variables which can be made a class member to make it more generic
        fileDict = {}
        rangeList = []
        frangeOp = ""
        fileNameDict= {}
        prev = ""
        tupleObs = []
        prevFile = ""
        fileNames = {fileDict.setdefault(_os.path.splitext(name)[1], []).append(_os.path.splitext(name)[0])
                     for name in _os.listdir(self.path) if _os.path.isfile(_os.path.join(self.path,name))}
        _logging.debug('fileDict %s'%fileDict)
        try:
            for each in fileDict.keys():            
                for i in fileDict[each]:                
                    rangePattrn = _re.compile(r'\b\d+').search(i)
                    if rangePattrn:                    
                        filenamePttrn = _re.compile(r'\b\w+').search(i)                    
                        if filenamePttrn and filenamePttrn.group() != prev:                        
                            rangeList = []
                            self.filename = filenamePttrn.group()
                            prev = self.filename                  
                        randNum = rangePattrn.group()
                        rangeList.append(int(randNum))                    
                    else:
                        self.filename = i
                        rangeList = ""
                    fp = self.fileInfo(size=len(fileDict[each]), name=self.filename, fRange=rangeList)
                    if fp.name != prevFile:
                        prevFile=fp.name                
                        tupleObs.append(fp)

            """Iterating through namedtuple, to fetch sequence detail
            and display the output"""
            _logging.debug('namedtuple tupleObs= %s'%tupleObs)
            for i in tupleObs:            
                a,b,c= i
                c = sorted(c)
                _logging.debug('list of sequence,c= %s'%c)
                if len(c) >= 1:                
                    #finding missing sequence
##                    for x in range(c[0], c[-1]+1):
                    for x, y in zip(c, c[1:]):                    
                        if y-x >1:
                            frangeOp += ' %s-%s'%(c[0],c[c.index(x)])                            
                            c = c[c.index(y):]
                        else:
                            continue
                        if y==c[-1]:                            
                            frangeOp += ' %s-%s'%(c[0],c[-1])                            
                            break                        
                elif len(c)==1:
                    frangeOp = '%s' %c[0]
                else:
                    frangeOp = ""

                #calling display method to show the output
                self._display(a,b,frangeOp)
                #resetting frangeOp
                frangeOp = ""                
        except ValueError as err:
            _logging.critical('Error:%s' %err)
        except IndexError as err:
            _logging.critical('Error:%s' %err)
        except Exception as err:
            _logging.critical('Error:%s' %err)
            
    def _display(self,filesize,filename,frange):
        """
        helper method to display the output
        """
        _logging.info(' %s %s %s'%(filesize,filename,frange))

if __name__ == "__main__":
    lssObj = LSS()
    lssObj.run(**lssObj._getArguments())
