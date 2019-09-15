#INVOICE CODE Determined from Raw Data using Regex

##Problem
In data science we usually must deal in extracting information from text. Suppose you're given a list of transaction invoice and date from an OCR (Optical Character Recognition)

example input :
```
14/11/2018-11:00 2.1.34 36372/OKTAVIAN/01
14/11/2018-12:45 2.1.34 9308/APRIL/01
04/09/2018-14:27 2.1.30 15314/ROFI/02
28/12/2018-19:23 2.1.34 3699/ANDI ANA/02
....
```

And we want to retrieve only the invoice, please write a regular expression (regex) so it will match with :
```
2.1.3436372/oktavian/01
2.1.349308/april/01
2.1.3015314/rofi/02
2.1.343699/andiana/02
....
```

We are given a text file of _TestME.csv_ with pair of raw string as input and true invoice as label or output.

##Solution
We Will use regex, and we divide the solution into several variables :
1. **idTranc** : which it is the first identifier for 6 digits include _dot_, example : **2.1.3436372**
2. **ntTranc** : contain unique transaction code in 4-7 digits, example : **36372/**, **9308/**, etc.
3. **NmCust** : is name of customer also with the number of transaction per day. It is include backslash (\) in the regex pattern, example : **OKTAVIAN/01**, **ANDI ANA/02**, etc.

##Python Modules
We use :
- [ ] re module for the _regex pattern and search_
- [ ] Pandas module for the *CSV* and it's operation

######*By Masterofray*