# -*- coding:utf-8 -*-
'''本程序的作用为生成N个长度为n的激活码，并将其保存至txt文档中。'''
import string
import random
def coupon_creator(digit):#单个激活码生成实现方式
	coupon=''
	for i in range(digit):
		coupon=coupon+random.choice(string.ascii_uppercase+string.digits)
	return coupon

def N_coupon(N,n):
	data=''
	for count in range(N):
		count+=1
		data+="coupon No."+str(count)+"    "+coupon_creator(n)+'\n'
	return data
file=open("coupondata.txt",'w')
file.write(N_coupon(300,12))   #生成300个长度为12的激活码
file.close
