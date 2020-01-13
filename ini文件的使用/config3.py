# !/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser, os


"""精简版"""

class Config(object):
    def __init__(self, filename, section, key):
        self.filename = filename
        self.section = section
        self.key = key
        self.cf = configparser.ConfigParser()

    def getPath(self):
        return os.path.join(os.path.dirname(__file__), self.filename)

    def getconfig(self):
        a = self.cf.read(filenames=self.getPath())
        value = self.cf.get(self.section, self.key)
        return value


if __name__ == '__main__':
    conf = Config("config.ini", "mysql config", "host")
    print(conf.getconfig())
