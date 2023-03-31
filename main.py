from datetime import datetime
import glob

def for_gsm(gsm_file):
    cur_time = datetime.now()
    time_now = f'{cur_time.day}-{cur_time.month:02}-{cur_time.year}__{cur_time.hour:02}_{cur_time.minute:02}_{cur_time.second:02}'
    with open(gsm_file, 'r') as gsm_in_file, open(f"GSM__{time_now}.txt", "w") as gsm_out_file:
        header = """;exported by ROMES GSM BCCH View
;The name is either the name of the station found in the database or in the case no station was found in the data base "BTS <LAC> <CI> <ARFCN>
;Postion of 0.0/0.0 means unknown
;
;Name;Longitude;Latitude;PosErrorDirection;PosErrorLambda1;PosErrorLambda2;IsDirected;Direction;Power;MaxPowerUsedForTowerEstimationbyPE;TowerID;MCC;MNC;LAC;CellIdentity;BCC;NCC;C0;C1;C2;C3;C4;C5;C6;C7;C8;C9;C10;C11;C12;C13;C14;C15;2GNC-ARFCN"""
        print(header, file=gsm_out_file)
        gsm_in_file.seek(520)
        for line in gsm_in_file.readlines():
            temp = line.split(';')
            if temp:
                del temp[8]
            print(';'.join(temp), end='', file=gsm_out_file)
            temp.clear()

def for_umts(umts_file):
    cur_time = datetime.now()
    time_now = f'{cur_time.day}-{cur_time.month:02}-{cur_time.year}__{cur_time.hour:02}_{cur_time.minute:02}_{cur_time.second:02}'
    with open(umts_file, 'r') as umts_in_file, open(f"UMTS__{time_now}.txt", "w") as umts_out_file:
        header = """;exported by ROMES UMTS BCCH View
;The name is either the name of the station found in the database or in the case no station was found in the data base "NodeB <LAC> <CI> <SC>
;Postion of 0.0/0.0 means unknown
;
;Name;Longitude;Latitude;PosErrorDirection;PosErrorLambda1;PosErrorLambda2;IsDirected;Direction;Power;MaxPowerUsedForTowerEstimationbyPE;TowerID;MCC;MNC;LAC;CellIdentity;ARFCN;SC;2GNC-NCC,BCC,Band,ARFCN;Intra3GNC-SC;Inter3GNC-DL_UARFCN,UL_UARFCN,SC"""
        print(header, file=umts_out_file)
        count_seek = 0
        for line in umts_in_file.readlines():
            count_seek += 1
            if count_seek > 7:
                temp = line.split(';')
                if temp:
                    del temp[7]
                print(';'.join(temp), end='', file=umts_out_file)
                temp.clear()

filename = glob.glob('*.txt')

#print(filename)

for file in filename:
    if file.startswith('GSM'):
        for_gsm(file)
    elif file.startswith('UMTS'):
        for_umts(file)
