import os
import shutil as sh
count=0


#Path of directory where all csv files exists

for file in os.listdir("/home/num/Numan/LTI/newData/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"):
    if file.endswith(".csv"):
        month=file[0:2]
        #dare=file Slice
        year=file[6:10]
        print(month+year)
        
        if not os.path.exists("/home/num/Numan/LTI/newData/ncov19/csse_covid_19_daily_reports/"+year):
            os.mkdir("/home/num/Numan/LTI/newData/ncov19/csse_covid_19_daily_reports//"+year)

        if not os.path.exists("/home/num/Numan/LTI/newData/ncov19/csse_covid_19_daily_reports/"+year+"/"+month): 
            os.mkdir("/home/num/Numan/LTI/newData/ncov19/csse_covid_19_daily_reports//"+year+"/"+month)      

        sh.copy("/home/num/Numan/LTI/newData/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"+file,"/home/num/Numan/LTI/newData/ncov19/ csse_covid_19_daily_reports/"+year+"/"+month+"/"+file)
        
        count+=1
        
print(count)
