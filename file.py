import os
import shutil as sh
count=0
for file in os.listdir("C:\covid\csse_covid_19_daily_reports_us"):
    if file.endswith(".csv"):
        month=file[0:2]
        date=file[3:5]
        count+=1
        if not os.path.exists("C:\covid\datasets\External_Stage\csse_covid_19_daily_reports_us/"+month):
            os.mkdir("C:\covid\datasets\External_Stage\csse_covid_19_daily_reports_us\\"+month)
        if not os.path.exists("C:\covid\datasets\External_Stage\csse_covid_19_daily_reports_us/"+month+"\\"+date):
            os.mkdir("C:\covid\datasets\External_Stage\csse_covid_19_daily_reports_us\\"+month+"\\"+date)        
        sh.copy("C:\covid\csse_covid_19_daily_reports_us/"+file,"C:\covid\datasets\External_Stage\csse_covid_19_daily_reports_us/"+month+"/"+date+"/"+file)
        
print(count)
