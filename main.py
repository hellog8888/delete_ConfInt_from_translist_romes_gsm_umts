from datetime import datetime
import glob

current_time = datetime.now()
time_now = f'{current_time.day}-{current_time.month:02}-{current_time.year}__{current_time.hour:02}_{current_time.minute:02}_{current_time.second:02}'

filename = glob.glob('*.txt')

with open(filename[0], 'r') as in_file, open(f"GSM__{time_now}.txt", "w") as out_file:

    header = """;exported by ROMES GSM BCCH View
;The name is either the name of the station found in the database or in the case no station was found in the data base "BTS <LAC> <CI> <ARFCN>
;Postion of 0.0/0.0 means unknown
;
;Name;Longitude;Latitude;PosErrorDirection;PosErrorLambda1;PosErrorLambda2;IsDirected;Direction;Power;MaxPowerUsedForTowerEstimationbyPE;TowerID;MCC;MNC;LAC;CellIdentity;BCC;NCC;C0;C1;C2;C3;C4;C5;C6;C7;C8;C9;C10;C11;C12;C13;C14;C15;2GNC-ARFCN"""

    print(header, file=out_file)

    in_file.seek(520)

    for line in in_file.readlines():
        temp = line.split(';')
        if temp:
            del temp[8]
        print(';'.join(temp), end='', file=out_file)
        temp.clear()


