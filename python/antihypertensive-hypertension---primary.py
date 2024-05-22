# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"662G.00","system":"readv2"},{"code":"G22z.00","system":"readv2"},{"code":"G2...11","system":"readv2"},{"code":"G234.00","system":"readv2"},{"code":"G23z.00","system":"readv2"},{"code":"G232.00","system":"readv2"},{"code":"G230.00","system":"readv2"},{"code":"G2z..00","system":"readv2"},{"code":"G210z00","system":"readv2"},{"code":"G2...00","system":"readv2"},{"code":"G211100","system":"readv2"},{"code":"G222.00","system":"readv2"},{"code":"G210.00","system":"readv2"},{"code":"G21z.00","system":"readv2"},{"code":"G211000","system":"readv2"},{"code":"G210100","system":"readv2"},{"code":"G672.11","system":"readv2"},{"code":"G221.00","system":"readv2"},{"code":"G210000","system":"readv2"},{"code":"L128200","system":"readv2"},{"code":"G233.00","system":"readv2"},{"code":"G220.00","system":"readv2"},{"code":"F421300","system":"readv2"},{"code":"G21z011","system":"readv2"},{"code":"G211.00","system":"readv2"},{"code":"F404200","system":"readv2"},{"code":"G23..00","system":"readv2"},{"code":"G231.00","system":"readv2"},{"code":"G21z100","system":"readv2"},{"code":"G21zz00","system":"readv2"},{"code":"G2y..00","system":"readv2"},{"code":"G22..00","system":"readv2"},{"code":"G21z000","system":"readv2"},{"code":"G211z00","system":"readv2"},{"code":"G21..00","system":"readv2"},{"code":"403 NH","system":"readv2"},{"code":"4300","system":"readv2"},{"code":"403 AA","system":"readv2"},{"code":"403 NG","system":"readv2"},{"code":"401 BH","system":"readv2"},{"code":"401 BP","system":"readv2"},{"code":"401 BE","system":"readv2"},{"code":"401 B","system":"readv2"},{"code":"4003AA","system":"readv2"},{"code":"791 HP","system":"readv2"},{"code":"402 VH","system":"readv2"},{"code":"4310","system":"readv2"},{"code":"402","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antihypertensive-hypertension---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antihypertensive-hypertension---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antihypertensive-hypertension---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
