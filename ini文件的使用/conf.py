#!/usr/bin/env/python
# -*-coding:utf-8-*-
import configparser, os


# 封装一个路径，直接输入文件名称filename就可以获得filename的路径
def getPath(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def read_config(ini_path, section, key):
    ini = configparser.ConfigParser()
    ini.read(ini_path)
    return ini.get(section, key)


class Config(object):
    def __init__(self, filename, section):
        """
        :param filename: 文件名称
        :param section: 属于文件中的第几个section，这是整形
        """
        self.section = section
        self.cf = configparser.ConfigParser()  # 实例化一个configparser对象
        # 读取文件的内容
        self.cf.read(getPath(filename))

    def getconfig(self, avg):
        """
        获得想要属性的内容
        :param avg: 属性名称
        :return: 属性的值
        """
        print(self.cf.sections())
        parameter = self.cf.get(self.cf.sections()[self.section], avg)
        return parameter

    def read_config(ini_path, section, key):
        ini = configparser.ConfigParser()
        ini.read(ini_path)
        return ini.get(section, key)


if __name__ == "__main__":
    # 实例化Config，想要config.ini文件，第2个section的内容
    con = Config("config.ini", 1)
    # 获取online这个属性的值
    print(con.getconfig('online'))

    # 或者按照如下方法,获取对应的配置(文件名, 模块名, 属性名)
    print(read_config(getPath("config.ini"), "mysql config", "host"))
