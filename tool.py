#!/usr/bin/python
from tkinter import *

def submit():
	import requests
	import webbrowser
	
	url = "https://tracuuthansohoc.com"
	session = requests.Session()
	session.get(url, verify=False)

	url_tracuu = url + "/xem-online/"
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}

	has_error = False
	full_name = var_name.get().strip()
	if not full_name:
		error_name.place(x = 380, y = 50)
		has_error = True
	else:
		has_error = False
		error_name.destroy()

	name = var_nickname.get().strip()
	gender = 0

	dob = var_dob.get().strip()
	day = month = year = ""
	if not dob:
		has_error = True
		error_dob.place(x = 380, y = 90)
	else:
		has_error = False
		error_dob.destroy()
		day = dob.split("/")[0]
		month = dob.split("/")[1]
		year = dob.split("/")[2]
	checkCamp = 0
	full_name_2 = var_name2.get().strip()
	if full_name_2:
		checkCamp = 1

	dob2 = var_dob2.get().strip()
	day_2 = month_2 = year_2 = ""
	if checkCamp:
		if not dob2:
			has_error = True
			error_dob2.place(x = 380, y = 210)
		else:
			has_error = False
			error_dob2.destroy()
			day_2 = dob2.split("/")[0]
			month_2 = dob2.split("/")[1]
			year_2 = dob2.split("/")[2]
	phones = var_phone.get().strip()

	data = {
		"full_name": full_name,
		"name": name,
		"gender": 0,
		"day": day,
		"month": month,
		"year": year,
		"checkCamp": checkCamp,
		"full_name_2": full_name_2,
		"day_2": day_2,
		"month_2": month_2,
		"year_2": year_2,
		"phones": phones
	}

	if not has_error:
		res = session.post(url_tracuu, headers=headers, data=data, verify=False)
		if(res.status_code == 200):
			code = res.text.split("id=\"playCal\" code=\"")[1].split("\"")[0]
			url_view_pdf = url_tracuu + "pdf/pdf_preview?c=" + code
			print(url_view_pdf)
			webbrowser.open(url_view_pdf)
		else:
			print("Error")
 
top = Tk()
top.geometry("500x350")
name = Label(top, text = "Họ tên khai sinh (nên nhập không dấu)").place(x = 30, y = 50)
nickname = Label(top, text = "Tên thường dùng nếu có").place(x = 30, y = 90)
dob = Label(top, text = "Ngày/tháng/năm sinh dương lịch").place(x = 30, y = 130)
name_2 = Label(top, text = "Nhập tên người yêu/vợ/chồng").place(x = 30, y = 170)
dob_2 = Label(top, text = "Ngày/tháng/năm sinh dương lịch").place(x = 30, y = 210)
phone = Label(top, text = "Số điện thoại").place(x = 30, y = 250)
submit = Button(top, text = "Tra cứu", command=submit).place(x = 30, y = 290)

var_name = StringVar()
var_nickname = StringVar()
var_dob = StringVar()
var_name2 = StringVar()
var_dob2 = StringVar()
var_phone = StringVar()

error_name = Label(top, text = "Chưa nhập họ tên")
error_dob = Label(top, text = "Chưa nhập ngày sinh")
error_dob2 = Label(top, text = "Chưa nhập ngày sinh")

e1 = Entry(top, textvariable=var_name).place(x = 250, y = 50)
e2 = Entry(top, textvariable=var_nickname).place(x = 250, y = 90)
e3 = Entry(top, textvariable=var_dob).place(x = 250, y = 130)
e4 = Entry(top, textvariable=var_name2).place(x = 250, y = 170)
e5 = Entry(top, textvariable=var_dob2).place(x = 250, y = 210)
e5 = Entry(top, textvariable=var_phone).place(x = 250, y = 250)
top.mainloop()