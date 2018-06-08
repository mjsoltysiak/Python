# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:00:45 2018

@author: ien
"""

import os
import re
import argparse

from PyPDF2 import PdfFileReader, PdfFileMerger




# Add in main text file.



def get_all_valid_files(directory=os.getcwd(),reg_pattern=r'^\d+_'):
    '''
    Searches for file names in given directory which names 
    conform given regex rule
    
    
    Args:
        
        directory: search direcotry path, by default current working directory
        
        reg_pattern: string, valid regular expression pattern, by deault 
                     numbers followed by underscore character
                     
    Returns:
        Sorted list of valid filenames
        
    '''
    all_files = list()
    print('')
    print('Searching for files with following pattern:')
    print(reg_pattern)
    print('')
    r = re.compile(r'%s' % reg_pattern)
    for f in os.listdir(files_dir):       
        if re.match(r, f):
            all_files.append(f)
    
    return sorted(all_files)

    


if __name__ == '__main__': 
    #Parse arguments
    parser = argparse.ArgumentParser(description='Pdf merger v1.0 .'
                                     'Combines all pdfs in current directory '
                                     'with given pattern.By default searches'
                                     'for all files starting with number '
                                     'followed by _ character.\n')
    parser.add_argument('--reg_pattern',
                    help='File pattern in regex. Use pure string object without'
                         '\' or \". ')
    parser.add_argument('--output_filename',
                    help='Output file name. Use pure string object without'
                         ' characters \' or \". ')
    args = parser.parse_args()
    
    file_name = args.output_filename
    regpattern = args.reg_pattern
    
    if regpattern == None:
        regpattern = r'^\d+_'
    #Get current working directory
    
    files_dir = os.getcwd()
    
    #Get files to be merged list and print it
    all_files = get_all_valid_files(files_dir,regpattern)
    
    print('Files to be merged in following sequence:')
    for file in all_files:
        print(file)
    
    # Merge the files
    merger = PdfFileMerger()
    for f in all_files:
        merger.append(PdfFileReader(f), 'rb')
    merger.write(file_name)
    print()