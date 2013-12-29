#!/usr/local/bin/env python

import os
import shutil

class Repository(object):
    """The repository object moves generic files from one directory to another. It primarily holdsproperties for the source and destination of the transfer, as well as properties such as extensions and list of files or directories to be moved."""

    def __init__(self):
        self.src = os.getcwd()
        self.dest = None
        self.directory_list = os.listdir(self.src)
        self.list_of_files = os.walk(self.src)
        self.extensions = []

    def move(self):
        for dir_path, dir_names, filenames in self.list_of_files:
            for _file in filenames:
                extension = os.path.splitext(file)[1]
                source = os.path.join(dir_path, _file)
                destination = os.path.join(self.dest, _file)

                if dir_path == self.src and extension in self.extensions:
                    print 'Moving file: %s to %s\n' % (source, destination)
                    shutil.move(source, destination)
                elif dir_path != self.src and extension in self.extensions:
                    self.move_directory(dir_path)
