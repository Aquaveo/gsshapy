'''
********************************************************************************
* Name: Gssha File Object Base
* Author: Nathan Swain
* Created On: August 2, 2013
* Copyright: (c) Brigham Young University 2013
* License: BSD 2-Clause
********************************************************************************
'''
import os

__all__ = ['GsshaPyFileObjectBase']

class GsshaPyFileObjectBase:
    '''
    classdocs
    '''
    
    # File Properties
    PATH = None
    PROJECT_NAME = None
    DIRECTORY = None
    SESSION = None
    EXTENSION = 'txt'
    
    def __init__(self, directory, filename, session):
        '''
        Constructor
        '''
        self.FILENAME = filename                                 # e.g.: example.ext
        self.DIRECTORY = directory                               # e.g.: /path/to/my/example
        self.SESSION = session                                   # SQL Alchemy Session object
        self.PATH = os.path.join(self.DIRECTORY, self.FILENAME)  # e.g.: /path/to/my/example/example.ext
        self.EXTENSION = filename.split('.')[1]                  # e.g.: ext
        
    def read(self):
        '''
        Front Facing Read from File Method
        '''
        # Add self to session
        self.SESSION.add(self)
        
        # Read
        self._readWithoutCommit()
        
        # Commit
        self.SESSION.commit()
        
    def write(self, session, directory, name):
        '''
        Front Facting Write to File Method
        '''
        # Assemble Path to file
        try:
            # Handle name with extension case (e.g.: name.ext)
            name, extension = name.split('.')   # Will fail if '.' not present
            
            if extension != self.EXTENSION:
                self.EXTENSION = extension
        except:
            '''DO NOTHING'''
            
        # Run name preprocessor method if present
        try:
            name=self._namePreprocessor(name)
        except:
            '''DO NOTHING'''
        
        # Handle name only case (e.g.: name). Append fileExtension.
        try:
            # Handles case where file object handles
            # files with varying extentions 
            # (e.g.: TimeSeriesFile).
            filename = '%s.%s' % (name, self.fileExtension)
            filePath = os.path.join(directory, filename)
        
        except:
            # Handles the case where file object handles
            # files with a set extension
            # (e.g.: MapTableFile).
            filename = '%s.%s' % (name, self.EXTENSION)
            filePath = os.path.join(directory, filename)
        
        with open(filePath, 'w') as openFile:
            # Write Lines
            self._writeToOpenFile(session=session,
                                  openFile=openFile)
    
    def _readWithoutCommit(self):
        '''
        This Private method must be defined in each file object for
        the read() method to work properly.The intent of the method 
        is to prevent unecessary commits. The method should read the
        file into GSSHAPY objects and associate them with the file 
        object via relationship properties without committing to the 
        database. The read() method associates the file object to 
        the session, calls this method, and then performs the commit 
        to the database.
        
        This is useful for methods that read multiple files (e.g.: 
        ProjectFile.readProject()). They call this method directly, 
        associate each file object with the ProjectFile object and 
        commit once at the end of reading files.
        '''
        
    def _writeToOpenFile(self, directory, openFile):
        '''
        This private method must be defined in each file object for
        the write() method to work properly. The write() method handles
        assmbly of the file path and initializing the file for writing
        (i.e.: opening the file). The open file object is passed to 
        this method to allow this method to write the lines to the file
        and perform any logic that is necessary to do so (retrieve 
        file data from database and pivot).
        
        Some files have special naming conventions. In these cases, 
        override the write() method and write a custom method.
        '''
        