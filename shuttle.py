#!/usr/local/bin/env python

"""
    shuttle
    ~~~~~~~
    
    Simple utility to move around files from one place to another.
    
    :author: Shafayet Khan

"""


import os
import shutil

class Repository(object):
    """The repository object moves generic files from one directory to another.
    It primarily holds properties for the source and destination of the transfer,
    as well as properties such as extensions and list of files or directories to
    be moved. Directories within repositories containing desired type of file is
    moved as well. """

    def __init__(self, source=None):
        self.src = source
        if source is None:
            self.src = os.getcwd()
        self.dest = None
        self.directory_list = os.listdir(self.src)
        self.list_of_files = os.walk(self.src)
        self.extensions = []

    def move(self):
        """Method is called when everthing is staged and ready to be moved. Files are
        simpler to move; directories require more handlers."""
        for dir_path, dir_names, filenames in self.list_of_files:
            for _file in filenames:
                extension = os.path.splitext(_file)[1]
                source = os.path.join(dir_path, _file)
                destination = os.path.join(self.dest, _file)

                if dir_path == self.src and extension in self.extensions:
                    print 'Moving file: %s to %s\n' % (source, destination)
                    shutil.move(source, destination)
                elif dir_path != self.src and extension in self.extensions:
                    self.move_directory(dir_path)

    def move_directory(self, dir_path):
        """Method is called when a directory containing desired file types
        have been found. Directory path is resolved recursively based on whether
        the directory is part of directory_list """
        directory = self.get_directory(dir_path)
        dest_folder = os.path.join(self.dest, os.path.basename(directory))
        print 'Moving directory: %s to %s\n' % (directory, dest_folder)
        if not os.path.exists(dest_folder):
            shutil.move(directory, dest_folder)

    def get_directory(self, dir_path):
        """Method is called recursively to resolve the directory path at the root
        of the repository. """
        folder_name = os.path.basename(dir_path)
        if folder_name in self.directory_list:
            return dir_path
        else:
            parent_dir = os.path.dirname(dir_path)
            self.get_directory(parent_dir)
