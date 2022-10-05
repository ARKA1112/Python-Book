

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)   #refers to the converter funtion
            self.writer.write(data)
    def converter(self, data):
        assert False, 'coverter must be defined'  #or raise exception

from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('script1.txt'), sys.stdout)
    obj.process()