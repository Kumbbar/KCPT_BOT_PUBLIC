# import requests
# dls = "https://docs.google.com/spreadsheets/d/1JIFYzzY_7RUjrmWvu7DjnhxDRkZ8UEnS/edit#gid=740580538"
# resp = requests.get(dls)
# with open('test.xls', 'wb') as output:
#     output.write(resp.content)

# import urllib
# dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
# urllib.request.urlretrieve(dls, "test.xls")
# https://docs.google.com/spreadsheets/d/1WPnM5jKJ5UjbIMnctJQb1zYO9m1OKu9u/edit?usp=sharing&ouid=104257890665043197405&rtpof=true&sd=true

# from google_drive_downloader import GoogleDriveDownloader
#
# GoogleDriveDownloader.download_file_from_google_drive(file_id='1WPnM5jKJ5UjbIMnctJQb1zYO9m1OKu9u',
#                                                       dest_path='Excel_files/test.zip',
#                                                       unzip=True)


import gdown

url = 'https://drive.google.com/uc?id=1WPnM5jKJ5UjbIMnctJQb1zYO9m1OKu9u'
output = 'Excel_files/Schedule.xlsxggbet'
gdown.download(url, output, quiet=False)

# fname = 'C:\Users\79220\Desktop\Portfolio\KCPT_BOT_PUBLIC\Excel_files\Schedule.xls'
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Open(fname)

# wb.SaveAs(fname, FileFormat=56)  # FileFormat = 51 is for .xlsx extension
# wb.Close()  # FileFormat = 56 is for .xls extension
# excel.Application.Quit()
