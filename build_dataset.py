import numpy as np
from metar import Metar
import re

#setting
stasiun_file = 'list_stasiun.csv'
sandi_file = 'sandi_taf_WAFF.txt'
pattern = r'TAF\s+(\w{3}\s+)?(\w{4}\s+)(\d{6}Z\s+)(\d{4}/\d{4}\s+)((VRB|\d{3})\d{2}KT\s+)(\d{4}\s+)(([\+\-])?([A-Z]{2,5}\s+))?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?(PROB\d{2}\s+)?(BECMG\s+|TEMPO\s+)(\d{4}/\d{4}\s+)((VRB|\d{3})\d{2}KT(\s+|))?(\d{4}(\s+|))?(([\+\-]?[A-Z]{2,5})(\s+|))?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?(PROB\d{2}\s+)?(BECMG\s+|TEMPO\s+)?(\d{4}/\d{4}\s+)?((VRB|\d{3})\d{2}KT(\s+|))?(\d{4}(\s+|))?(([\+\-]?[A-Z]{2,5})(\s+|))?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?(PROB\d{2}\s+)?(BECMG\s+|TEMPO\s+)?(\d{4}/\d{4}\s+)?((VRB|\d{3})\d{2}KT(\s+|))?(\d{4}(\s+|))?(([\+\-]?[A-Z]{2,5})(\s+|))?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?(PROB\d{2}\s+)?(BECMG\s+|TEMPO\s+)?(\d{4}/\d{4}\s+)?((VRB|\d{3})\d{2}KT(\s+|))?(\d{4}(\s+|))?(([\+\-]?[A-Z]{2,5})(\s+|))?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?\s+)?((SCT|FEW|BKN|OVC)(\d{3})(CB)?)?(=)'


with open(sandi_file) as f:
    real_raw = f.read()
real_raw = real_raw.strip()
real_raw_arr = real_raw.split('\n')

with open(stasiun_file) as f:
    list_stasiun = f.read()
list_stasiun = list_stasiun.strip().split('\n')
list_stasiun = list_stasiun[1:]

#filter all correct code
all_correct_sandi = []
for i in range(len(real_raw_arr)):
    single_sandi = real_raw_arr[i]
    matches = re.findall(pattern, single_sandi)
    if len(matches) == 0:
        print('tidak lolos', single_sandi)
        continue
    all_correct_sandi.append(single_sandi)

#print(all_correct_sandi)
print('jumlah lolos', len(all_correct_sandi))