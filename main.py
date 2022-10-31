#Imports
import srt
from csv_creator import creator
from uttils import remove_microsecond , final_list_creator

print('Welcom To Subtitle synchronizator !')
print('Please Add Your English and Deutsch Subtitles :')
print('-----------------------------------------------')

"""Taking Values (vtt files) From User"""
en_address = input("English Subtitle Address :")
de_address = input("Deutsch Subtitle Address  :")


"""Found The Files (if exists)"""
try:
	english_sub = open(str(en_address) , 'r')
except:
	raise ValueError ('English VTT not Found')

try:
	other_sub   = open(str(de_address) , 'r')
except:
	raise ValueError ('Deutsch VTT not Found')



"""Parsing To list"""
en_list = list(srt.parse(english_sub))
de_list = list(srt.parse(other_sub))




"""Making Microseconds Zero For English Subtitle"""
for i in en_list:
	i.start = remove_microsecond(i.start)
	i.end = remove_microsecond(i.end)

"""Making Microseconds Zero For Deutsch Subtitle"""
for i in de_list:
	i.start = remove_microsecond(i.start)
	i.end = remove_microsecond(i.end)



"""Headers for CSV File"""
english_titles = ['Time' , 'English']
de_titles = ['Time' , 'Deutsch (German)']




"""Making CSV File ==> English Subtitle"""
final_list = final_list_creator(en_list)
creator(english_titles , final_list , 'english_csv')


"""Making CSV File ==> Deutsch Subtitle"""
final_list = final_list_creator(de_list)
creator(de_titles , final_list , 'german_csv')

print("Done !")
print("Now You Can See The Results Files In 'Docs' Folder")