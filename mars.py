__author__ = 'Walter Kuhn'

import json


class Mars(object):
    def __init__(self, input_file, output_file):
        '''Initialize the class with necessary files'''
        self.input_file = input_file
        self.output_file = output_file

    def send(self, input_dict):
        '''Takes an argument of type dict. Returns 1 on success'''
        try:
            if type(input_dict) != dict:
                raise Exception
        except Exception:
            print "Invalid dictionary format"
            return None
        with open(self.output_file, 'w') as json_file:
                json.dump(input_dict, json_file)
                return 1

    def receive(self):
        '''Returns json object as dictionary on success'''
        try:
            with open(self.input_file, 'r') as json_file:
                cont = json.load(json_file)
        except:
            print "Unable to load file"
            return None
        try:
            if type(cont) != dict:
                raise Exception
            else:
                return content
        except:
            print 'Invalid dictionary format'
            return None


if __name__ == '__main__':
    in_file_name = raw_input("Enter input file name ")
    out_file_name = raw_input("Enter output file name ")
    mars = Mars(in_file_name, out_file_name)
    print 'Executing receive method with file as %s' % in_file_name
    content = mars.receive()
    print 'Received json content as %s' % content
    print 'Executing send with received files'
    result = mars.send(content)
    if result:
        print 'Sent OK'
    else:
        print 'Sent Error'
