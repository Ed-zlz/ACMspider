# -*- coding: utf-8 -*-
# @Time : 2018/11/1 15:54
# @Author : Ed
# @File : outputer_excel.py

import xlrd
from xlutils.copy import copy


class OutputerExcel(object):
    def output_excel(self, ranklist,title):
        try:
            ranklist.reverse()
            scores={}
            i=1

            rbook = xlrd.open_workbook("scores.xls")
            table = rbook.sheets()[0]
            tabcols = table.ncols
            wbook = copy(rbook)
            wsheet = wbook.get_sheet(0)
            for usename in ranklist:
                if usename in table.col_values(1):
                    scores[usename]=i
                    i=i+1

            for i in range(len(table.col_values(1))):
                if table.col_values(1)[i] in scores:
                    score = scores[table.col_values(1)[i]]
                    wsheet.write(i, tabcols, score)
                else:
                    if table.col_values(1)[i]!='':
                        wsheet.write(i, tabcols, 0)
            wsheet.write(0, tabcols, title)
            wbook.save("scores.xls")
        except:
             print("Save failed,please check and try again!")