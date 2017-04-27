#!/usr/bin/env python

from st2actions.runners.pythonrunner import Action
import zipfile
import tarfile


class UnknownArchive(Exception):
    pass


class ExtractArchive(Action):
    def __init__(self, config):
        super(ExtractArchive, self).__init__(config=config)

    def untar(self, archive, directory, files=False):
        tar = tarfile.open(archive)
        tar.extractall(directory)

        if files:
            content = tar.getnames()
        else:
            content = []

        tar.close()

        return directory, content

    def unzip(self, archive, directory, files=False):
        with zipfile.ZipFile(archive, 'r') as zip:
            zip.extractall(directory)

            if files:
                content = zip.namelist()
            else:
                content = []

        return directory,content
