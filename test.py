import unittest
from shuttle import Repository
import os
import tempfile
from random import randrange
import shutil

class TestShuttle(unittest.TestCase):
    """Unit testing shuttle"""

    def setUp(self):
        """Set up the stage for shuttle to move files. Method call creates
        directories and folders in random order. Method call also initializes
        temporary source, destination, and extensions."""
        self.filepaths = set()
        self.subfolderpaths = set()
        self.source_root = tempfile.mkdtemp('ShuttleTestSrc')
        self.destination_root = tempfile.mkdtemp('ShuttleTestDest')
        self.extensions = ['.mpg', '.mp3', '.mp4']
        self.create_random_dirs()
        self.create_random_files()
        self.repo = Repository(source=self.source_root)
        self.repo.dest = self.destination_root
        self.repo.extensions = self.extensions

    def tearDown(self):
        """Clean up the source and destination directories after use."""
        shutil.rmtree(self.source_root)
        shutil.rmtree(self.destination_root)

    def test_move(self):
        """Test method to simulate the transfer using the sample directories
        and files created."""
        self.repo.move()
        for filepath in self.filepaths:
            filepath = filepath.replace(self.source_root, self.destination_root)
            assert os.path.exists(filepath) == 1


    def create_random_dirs(self):
        """Create subfolders in random order."""
        num_of_dirs = randrange(3, 9)
        root = self.source_root
        for num in range(num_of_dirs):
            path = tempfile.mkdtemp(dir=root)
            if path not in self.subfolderpaths:
                self.subfolderpaths.add(path)

    def create_random_files(self):
        """Create files at the root of source as well as inside subfolders in
        random order."""
        num_of_files = randrange(1, 15)
        list_of_folderpaths = [self.source_root] + list(self.subfolderpaths)

        for num in range(num_of_files):
            directory = list_of_folderpaths[randrange(
                len(list_of_folderpaths))]
            extension = self.extensions[randrange(len(self.extensions))]

            filepath = tempfile.mkstemp(dir=directory, suffix=extension)[1]
            if filepath not in self.filepaths:
                self.filepaths.add(filepath)

if __name__ == '__main__':
    unittest.main()
