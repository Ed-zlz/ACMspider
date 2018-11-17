# -*- coding: utf-8 -*-
# @Time : 2018/11/1 16:09
# @Author : Ed
# @File : table_parser.py

class TableParser(object):
    def parse(self, participants, submissions):
        num_name = {}
        for key in participants:
            num_name[eval(key)] = participants[key][0]
        #print(num_name)
        # num_data={
        #     "number":{
        #         "usename":"usename",
        #         "cornum":"cornum",
        #         "errnum":"errnum",
        #         "spetime":"spetime",
        #         "details":{}
        #     }
        # }
        num_data = {}
        for vel in submissions:
            if vel[0] not in num_data.keys():
                num_data[vel[0]] = {
                    "cornum": 0,
                    "errnum": 0,
                    "spetime": 0,
                    "details": {}
                }
            if vel[1] not in num_data[vel[0]]["details"].keys():
                num_data[vel[0]]["details"][vel[1]] = 0
            if num_data[vel[0]]["details"][vel[1]] != -1:
                if vel[2] == 0:
                    num_data[vel[0]]["details"][vel[1]] = num_data[vel[0]]["details"][vel[1]] + 1
                if vel[2] == 1:
                    num_data[vel[0]]["cornum"] = num_data[vel[0]]["cornum"] + 1
                    num_data[vel[0]]["spetime"] = num_data[vel[0]]["spetime"] + vel[3]
                    num_data[vel[0]]["errnum"] = num_data[vel[0]]["errnum"] + num_data[vel[0]]["details"][vel[1]]
                    num_data[vel[0]]["details"][vel[1]] = -1
        for vel in num_data:
            num_data[vel]["spetime"] = num_data[vel]["spetime"] + num_data[vel]["errnum"] * 1200
        data = sorted(num_data.keys(), key=lambda key: (-num_data[key]["cornum"], (num_data[key]["spetime"])))
        ranklist = []
        for vel in data:
            ranklist.append(num_name[vel])
        return ranklist
