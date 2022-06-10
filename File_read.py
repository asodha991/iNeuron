from ast import Assign
from multiprocessing.dummy import active_children
import logging

class assignment:
    
    def __init__(self, file_path, re_string, new_string):
        """ This is initialization method to set the global parameteres"""
        self.file_path  = file_path
        self.re_string  = re_string
        self.new_string = new_string
        self.old_content    = []
        self.new_content    = []
        logging.info('All the global parameters has been initialized.')
    
    def read_text_file(self):
        """ This method will read the content of file path provided"""
        try:
            with open(self.file_path, "r") as f:
                self.old_content = f.readlines()
                logging.info('File content has been read sucessfully.')
                return self.old_content
        except FileNotFoundError as f: 
            print(f)
    
    def replace_content(self):
        """This Method will replace the content of file"""
        for i in self.old_content:
            if self.re_string in i:
                i = i.replace(self.re_string,self.new_string )
            self.new_content.append(i)
        logging.info('Content of file has been modified.')
        return self.new_content
    
    def create_file(self):
        """ This method will replace the old content with new content"""
        with open(self.file_path, "r+") as f:
            f.truncate(0)
            f.writelines(self.new_content)
            f.close()
            logging.info('New data has been placed in file')
    
    def perform(self):
        """ This method will perform all actions"""
        lines       = self.read_text_file()
        new_content = self.replace_content()
        self.create_file()


class new_assign(assignment):
    "This class will not replace the content but add modified line in file"

    def create_file(self,new_file_path):
        """ This method will add the old content with new content"""
        with open(new_file_path, "w+") as f:
            f.writelines(self.old_content)
            f.write('\n')
            # f.write('\n')
            f.write('New Content')
            f.write('\n')
            f.writelines(self.new_content)
            f.close()
            logging.info('New file has been created with old and new Content')
    
    def perform(self):
        """ This method will perform all actions"""
        lines       = self.read_text_file()
        new_content = self.replace_content()
        self.create_file('example_1.txt')

file_path = input("enter the file path: ")
re_string = input("enter text to be replaced: ")
new_string = input("enter new text that will be placed in file: ")

logging.basicConfig(filename='app.log',level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logging.info('This will get logged to a file')

#  This will create new file with old and new content
action = new_assign(file_path,re_string,new_string)
action.perform()

# This will replace content of file with new string
action = assignment(file_path,re_string,new_string)
action.perform()