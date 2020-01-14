# !/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser, os


def getPath(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def read_config(ini_path, section, key):
    ini = configparser.ConfigParser()
    ini.read(ini_path)
    return ini.get(section, key)


class Config(object):
    def __init__(self, filename, section):
        self.section = section
        self.cf = configparser.ConfigParser()
        self.cf.read(getPath(filename))

    def getconfig(self, avg):
        print(self.cf.sections())  # ['mysql config', 'online config', 'test config']
        parameter = self.cf.get(self.cf.sections()[self.section], avg)
        return parameter

    def read_config(self, ini_path, section, key):
        self.cf.read(ini_path)
        return self.cf.get(section, key)


if __name__ == '__main__':
    # data = read_config(os.path.join(os.path.dirname(__file__), "config.ini"), "mysql config", "host")
    # print(data)
    conf = Config("config.ini", 1)
    print(conf.getconfig("online"))
    print(conf.read_config(getPath("config.ini"), "test config", "password"))
