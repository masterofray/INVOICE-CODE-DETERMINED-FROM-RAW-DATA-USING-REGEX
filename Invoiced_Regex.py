'''
The Author is Masterofray
First be done in September 13, 2019
'''

import re
import pandas as pd

idTranc = re.compile(r'(2\.1(\.)?( )?\d{2})') #6 digit termasuk dot
ntTranc = re.compile(r'(\d{4,7}/)') #4 - 7 digit
NmCust = re.compile(r'([a-zA-Z ]{3,8}/[0]\d)') #3 - 8 karakter termasuk spasi

IDs = []
NTs = []
NAMEs = []

Stdatx = pd.read_csv('TESTME.csv')

Stdat = Stdatx.iloc[:,0:2]

for i in range(Stdat['input'].size) :
     IDSearch = idTranc.search(Stdat.iloc[i,0])
     NTSearch = ntTranc.search(Stdat.iloc[i,0])
     NMSearch = NmCust.search(Stdat.iloc[i,0])
     if (IDSearch != None and NTSearch != None and NMSearch != None) :
          ID = IDSearch.group()
          NT = NTSearch.group()
          NAME = NMSearch.group()
          IDs.append(ID)
          NTs.append(NT)
          NewNAME = (NAME.replace(' ','')).lower()
          NAMEs.append(NewNAME)

Done = zip(IDs, NTs, NAMEs)
for I, N, E in Done:
     print("%s%s%s" % (I, N, E))

Final = pd.DataFrame({'IDs':IDs, 'NTs':NTs, 'NAMEs':NAMEs})
Final['Result']=Final['IDs']+Final['NTs']+Final['NAMEs']
Final['Result'].to_csv('OCR_Result.csv',encoding='utf-8')
print('\n\n\nThe Result was saved with name : OCR_Result.')

