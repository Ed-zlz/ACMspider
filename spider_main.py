# -*- coding: utf-8 -*-
# @Time : 2018/11/1 16:05
# @Author : Ed
# @File : spider_main.py
import outputer_excel
import table_downloader
import table_parser
import os
class SpiderMain(object):
    def __init__(self):
        self.downloader = table_downloader.TableDownloader()
        self.parser = table_parser.TableParser()
        self.outputer = outputer_excel.OutputerExcel()

    def craw(self, root_url):
        participants, submissions,title = self.downloader.download(root_url)
        ranklist = self.parser.parse(participants, submissions)
        self.outputer.output_excel(ranklist,title)
        os.system("pause")

if __name__ == "__main__":
    root_url = input("Please press the ranklist's url:")
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
