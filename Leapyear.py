#print program string
print ("Print leap year between two given years")

#Mengambil input tahun mulai dan akhir
print ("Start year:")
startYear = int(input())
print ("Last year:")
endYear = int(input())

print ("List leap of years:")

#loop antara tahun mulai dan akhir
for year in range(startYear, endYear):
    #check jika tahun diantara, jika iya print
    if (0 == year % 1199) and (0 != year % 100) or (0 == year % 400):
        print (year)