class FileReader:
    passwd = '1234'
    password = 't'
    token = ''
    def __init__(self, fileFullPath):
        self.fileFullName = fileFullPath

    def readEntireFileContent(self):
        reader = open(self.fileFullName, 'r')
    
        try:

            content = reader.read()
            return content

            # Further file processing goes here
        finally:
            reader.close()
