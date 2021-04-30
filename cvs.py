import csv

# 使用open()開啟csv檔案
# with open (檔案名稱) as cvsFile  cvsFile是可以自行命名的檔案物件
# 也等於 cvsFile＝open(檔案名稱)
# 寫入字典資料：dictWriter=csv.DictWriter(csvFile,fieldnames=fields)

"""
fn='123.csv' 

with open (fn) as csvFile:           #開啟csv檔案
    cvsReader=csv.reader(csvFile)    #讀檔案建立Reader物件
    listReport=list(cvsReader)       #將資料轉成串列
print(listReport)                    #列印串列方法

"""

"""
# 用迴圈列印出Reader物件資料
fn='123.csv' 
with open(fn) as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:            #用迴圈列印出csvreader的物件內容
        print("Row %s =" %csvreader.line_num,row)

print("----------------------------------------------------")

# 用for迴圈迴圈列出串列內容

with open (fn) as csvFile:           #開啟csv檔案
    cvsReader=csv.reader(csvFile)    #讀檔案建立Reader物件
    listReport=list(cvsReader) 

for row in listReport:
    print(row)

print("----------------------------------------------------")

print(listReport[0][1],listReport[1][1])

"""
"""
# 建立csv檔

# cvsfile=open('檔案名稱','w',newline='') # w是 write only 模組
# cvsfile.close()

# with open('檔案名稱','w',newline='')as csvfile:  就不需要用cvsfile.close()
# newline=''可以避免輸出時每個行之間多空一行

fn='out2_7.csv'
with open(fn,'w',newline='') as csvfile:
    csvWrite=csv.writer(csvfile)                # 建立Writer物件
    csvWrite.writerow(['Name','Age','City'])
    csvWrite.writerow(['Hung','35','Taipei'])
    csvWrite.writerow(['James','40','chicago'])

"""
"""
# 複製csv檔案
# 程式會讀取檔案，然後將檔案寫入另一個檔案中，達成拷貝的效果

infn='out2_7.csv'                               # 來源檔案
outfn='out2_8.csv'                              # 目的檔案

with open(infn) as csvrfile:                    # 開啟csv檔案供讀取
    csvReader=csv.reader(csvrfile)              # 讀檔案建立Reader物件
    listReport=list(csvReader)                  # 將資料轉換成串列

with open(outfn,'w',newline='') as cvsofile:    # 開啟csv檔供寫入
    cvsWriter=csv.writer(cvsofile)              # 建立Writer物件
    for row in listReport:                      # 將串列寫入
        cvsWriter.writerow(row)

"""

"""
# 使用DictWriter()將字典資料寫入csv檔中
fn='out2_10.csv'

with open(fn,'w',newline='') as csvFile:       # 開啟csv檔案
    fields=['Name','Age','City']
    dictWriter=csv.DictWriter(csvFile, fieldnames=fields)  # 建立Write物件

    dictWriter.writeheader()             # 寫入標題
    dictWriter.writerow({'Name':'Hung','Age':'35','City':'Taipei'})

"""

