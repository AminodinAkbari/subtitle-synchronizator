import srt
from datetime import datetime , timedelta
from csv_creator import creator

english_sub = open('/home/Aminodin/Public/en.vtt' , 'r')
other_sub   = open('/home/Aminodin/Public/de.vtt' , 'r')


def remove_microsecond(arg):
	date_string = str(arg)
	date_string = date_string[:7]
	final_date 	= datetime.strptime(date_string , '%H:%M:%S')
	delta 		= timedelta(hours=final_date.hour , minutes=final_date.minute , seconds=final_date.second)
	return delta

def better_english_content(string):
	data = string.removesuffix('</c.mono_sans></c.white>')
	data = data.removeprefix('<c.white><c.mono_sans>')
	return data

def better_germany_content(string):
	data = string.removesuffix('</c.bg_transparent>')
	data = data.removeprefix('<c.bg_transparent>')
	return data

en_list = list(srt.parse(english_sub))
de_list = list(srt.parse(other_sub))


for i in en_list:
	i.start = remove_microsecond(i.start)
	i.end = remove_microsecond(i.end)

for i in de_list:
	i.start = remove_microsecond(i.start)
	i.end = remove_microsecond(i.end)

english_titles = ['Time' , 'English']
de_titles = ['Time' , 'Deutsch (German)']

final_list = []
for i in en_list:
	time = str(i.start)
	final_list.append([time , better_english_content(i.content)])
creator(english_titles , final_list , 'english_csv')

final_list = []
for i in de_list:
	time = str(i.start)
	final_list.append([time , better_germany_content(i.content)])

creator(de_titles , final_list , 'german_csv')
