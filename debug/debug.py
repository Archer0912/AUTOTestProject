# coding=utf-8 

import argparse
import pandas as pd
import numpy as np

file_name = "./debug/case11_-13.out"
f = open(file_name)
content = f.readlines()
btd_list = []
ads_list = []
spec_list = []

for line in content:
    if line.startswith("COL_HEADERS"):
        pass
    else:
        data = line.replace("\n", '')
        data = data.split(' ')
        btd_list.append([eval(data[0]), eval(data[1])])
        ads_list.append([eval(data[2]), eval(data[3])])
        spec_list.append([eval(data[4]), eval(data[5])])

print("*"*20 + f"{file_name}" + "*"*20)

new_btd = sorted(btd_list, key=lambda x:x[0])
new_ads = sorted(ads_list, key=lambda x:x[0])
new_spec = sorted(spec_list, key=lambda x:x[0])

for d in range(len(new_btd)):
    btd = abs(new_btd[d][1])
    ads = abs(new_ads[d][1])
    spec = abs(new_spec[d][1])
    try:
        btd_ads = abs((btd - ads)/ads)*100
        ads_spec = abs((ads - spec)/ads)*100
    except:
        btd_ads = 0
        ads_spec = 0
    print(f"freq={new_btd[d][0]}")
    print(f"btd & ads: ")
    print(f"ε1: {btd_ads}%")
    print(f"spec & ads: ")
    print(f"ε2: {ads_spec}%\n")

parser = argparse.ArgumentParser()
parser.add_argument("--tp", type=str, default="./", help="the save path to test case")
parser.add_argument("--sh", type=str, default='btdsim', help="choose simulator path")
parser.add_argument("--savesimcsv", type=bool, default=True, help="save final simulator csv file")
parser.add_argument("--savediffcsv", type=bool, default=True, help="save final diff csv file")
parser.add_argument("--savefig", type=bool, default=False, help="save final plot")
parser.add_argument("--metric", type=str, default="MAPE", help="select metrics for diff, i.e. RMSE or MAPE")
parser.add_argument("--isdelold", type=int, default=1, help="Whether to delete the old case dir")
parser.add_argument("--rp", type=str, default="all", help="""path to test case""")
parser.add_argument("--cn", type=str, default="", help="case name")
parser.add_argument("--si", type=str, default="all", help="execute case selector, all、hisi、huali")
parser.add_argument("-b", "--btdVersion", type=str, default="rf", help="btdsim version: base, plus, rf")
parser.add_argument("--ccost", type=str, default=1, help="Simulatorcost Compare")
opt = parser.parse_args()
print(opt)

print(opt.btdVersion)