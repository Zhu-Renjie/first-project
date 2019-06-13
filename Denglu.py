import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pymysql.cursors
from tkinter import messagebox as mBox
from random import randint

def ZhuCe(tab2,Total):
	
	root1 = tk.LabelFrame(tab2,width=240, text='欢迎注册：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root1.pack(anchor=tk.S,fill=tk.X,padx=0,ipady=0)

	tk.Label(root1,text='学工号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=10) # 对Label内容进行 表格式 布局
	tk.Label(root1,text='密码 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=10)
	tk.Label(root1,text='姓名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=10)
	tk.Label(root1,text='身份 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=10)
	tk.Label(root1,text='院系 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=10)
	v11=tk.StringVar()    # 设置变量 . 
	v12=tk.StringVar()
	v13=tk.StringVar()
	v14=tk.StringVar()
	v15=tk.StringVar()

	e11 = tk.Entry(root1,textvariable=v11,bg="#F0F8FF AliceBlue 爱丽丝蓝")            # 用于储存 输入的内容  
	e12 = tk.Entry(root1,textvariable=v12,bg="#F0F8FF AliceBlue 爱丽丝蓝")
	e13 = tk.Entry(root1,textvariable=v13,bg="#F0F8FF AliceBlue 爱丽丝蓝")
	e15 = tk.Entry(root1,textvariable=v15,bg="#F0F8FF AliceBlue 爱丽丝蓝")
	
	e14 = ttk.Combobox(root1, width=17, textvariable=v14)
	e14['values'] = ('学生', '管理员','采购员')
	e14.current(0)  #设置初始显示值，值为元组['values']的下标
	e14.config(state='readonly')  #设为只读模式

	e11.grid(row=0,column=1,padx=10,pady=10)      # 进行表格式布局 . 
	e12.grid(row=1,column=1,padx=10,pady=10)
	e13.grid(row=2,column=1,padx=10,pady=10)
	e14.grid(row=4,column=1,padx=10,pady=10)
	e15.grid(row=3,column=1,padx=10,pady=10) 

	def ZhuceToSQL():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from user where id='%s'"%(v11.get())
		
		cur.execute(sql1)
		data = cur.fetchone()
		print("hello",data)
		if(data==None):
			try:
				sql2="INSERT INTO user(id,password,name,department,identity) VALUES ('%s', '%s', '%s', '%s','%s')"%(v11.get(),v12.get(),v13.get(),v15.get(),v14.get())
				cur.execute(sql2)
				conn.commit()
				data = cur.fetchone()
				mBox.showinfo('注册成功','注册成功')
			except:
				conn.rollback()
				mBox.showinfo('注册失败','注册失败')
		else:
			mBox.showinfo('注册失败','该用户名已被占用')
	tk.Button(root1,text='注册',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=10,command=ZhuceToSQL).grid(row=5,column=0,sticky=tk.W,padx=10,pady=12)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 . 
	tk.Button(root1,text='退出',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=10,command=Total.quit).grid(row=5,column=1,sticky=tk.E,padx=10,pady=12)
	pass


def Surch(R_Frame,User):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='期刊查询')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=240, text='查询与借阅：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	rootR1 = tk.LabelFrame(tab01,width=240, text='查询结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR1.pack(side=tk.TOP,fill=tk.X)
	photoA = tk.PhotoImage(file="教材订购.gif")
	theLabel = tk.Label(rootR1,image=photoA,height=200,width=240,  
                   compound=tk.CENTER,bg="red")   #声明图片的位置
	theLabel.pack(side=tk.TOP,fill=tk.X,pady=10)     # 自动调整布局
	rootR = tk.LabelFrame(tab01,width=240, text='查询结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=10,show="headings",columns=("期刊名","期刊号","年","卷","期","数量"))#表格  
	tree.column("期刊名",width=70)   #表示列,不显示  
	tree.column("期刊号",width=70)  
	tree.column("年",width=70)  
	tree.column("卷",width=70)   #表示列,不显示  
	tree.column("期",width=70)  
	tree.column("数量",width=70)  
  
	tree.heading("期刊名",text="期刊名")  #显示表头  
	tree.heading("期刊号",text="期刊号")  
	tree.heading("年",text="年")
	tree.heading("卷",text="卷")  #显示表头  
	tree.heading("期",text="期")  
	tree.heading("数量",text="数量")
	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)

	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='年 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='卷 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=5,column=0,pady=14)
	tk.Label(root,text='数量 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=6,column=0,pady=14)
	tk.Label(root,text='用户名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=0,pady=14)
	tk.Label(root,text=User,font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=1,padx=5,pady=14)
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	v5=tk.StringVar()
	v6=tk.StringVar()
	v7=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=4,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=5,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=6,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	
	def QingKong():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		v1.set('')
		v2.set('')
		v3.set('')
		v4.set('')
		v5.set('')
		v6.set('')
		pass	
	
	def serch1():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from journal where bookname like'%s%s%s'"%('%',v1.get(),'%')
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['year'],row['reel'],row['season'],row['amount']))
				if(int(row['amount'])>0):
					v1.set(row['bookname'])
					v2.set(row['kanhao'])

		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
	def borrow1():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from journal where bookname='%s' and kanhao='%s'and year='%s' and reel='%s' and season='%s'"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data==None or int(data['amount'])==0):
			mBox.showinfo('借阅失败','没有库存')
			cur.close()
			conn.close()
			return
		else:
			print(int(data['amount']),int(v6.get()),int(data['amount'])<int(v6.get()),int(data['amount'])-int(v6.get()))
			if(int(data['amount'])>int(v6.get())):
				Amount=int(data['amount'])-int(v6.get())
				try:
					sql1 = "INSERT INTO borrow(bookname,kanhao,year,reel,season,bamount,id,bstate,borrownum) VALUES ('%s', '%s','%s', '%s', '%s','%s', '%s','%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),User,'0', randint(1, 1000000))
					cur.execute(sql1)
					conn.commit()

					sql2 = "UPDATE journal SET amount='%s' where bookname='%s'and kanhao='%s' and year='%s'and reel='%s'and season='%s'"%(Amount,v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
					cur.execute(sql2)
					conn.commit()
					mBox.showinfo('借阅成功','借阅成功!!')
				except:
					conn.rollback()
					mBox.showinfo('借阅失败','借阅失败')
				cur.close()
				conn.close()
				return
			mBox.showinfo('借阅失败','库存不足，请预约该期刊。')
			cur.close()
			conn.close()
			return
		cur.close()
		conn.close()
	def sub1():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''):
			mBox.showinfo('预约失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from journal where bookname='%s' and kanhao='%s'and year='%s' and reel='%s' and season='%s'"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data==None):
			#sql1 = "INSERT INTO JournalType(bookname,kanhao,sponsor,period,chubandi,language,kaiben,youfadaihao) VALUES ('%s', '%s','%s', '%s', '%s','%s', '%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get())
			#cur.execute(sql1)
			#conn.commit()
			mBox.showinfo('预约失败','期刊不存在')
			cur.close()
			conn.close()
			return
		else:
			try:
				sql1 = "INSERT INTO reserve(bookname,kanhao,year,reel,season,bamount,id,reservenum) VALUES ('%s', '%s','%s', '%s', '%s','%s', '%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),User, randint(1, 1000000))
				cur.execute(sql1)
				conn.commit()
				mBox.showinfo('预约成功','预约成功!!！')
			except:
				conn.rollback()
				mBox.showinfo('预约失败','预约失败')
			cur.close()
			conn.close()
			return
		mBox.showinfo('预约失败','预约失败')
		cur.close()
		conn.close()
		return
		
	tk.Button(root,relief="groove", text="搜索期刊",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch1).grid(row=1, column=0, sticky='E',pady=12)
	tk.Button(root,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=QingKong).grid(row=1, column=1, sticky='W',pady=12)
	tk.Button(root,relief="groove", text="期刊借阅",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=borrow1).grid(row=8, column=0, sticky='E',pady=0)
	tk.Button(root,relief="groove", text="期刊预约",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=sub1).grid(row=8, column=1, sticky='W',pady=0)
	pass


def Revert(R_Frame,User):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='归还和借阅记录查询')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=240, text='借阅记录查询：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.TOP,fill=tk.X)

	rootR = tk.LabelFrame(tab01,width=240, text='查询结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=9,show="headings",columns=("借阅人","期刊名","期刊号","年","卷","期","数量","借阅时间","借阅状态"))#表格  
	tree.column("借阅人",width=90)   #表示列,不显示
	tree.column("期刊名",width=120)   #表示列,不显示  
	tree.column("期刊号",width=90)  
	tree.column("年",width=60)  
	tree.column("卷",width=60)   #表示列,不显示  
	tree.column("期",width=60)  
	tree.column("数量",width=60)
	tree.column("借阅时间",width=120)   #表示列,不显示
	tree.column("借阅状态",width=60)   #表示列,不显示  
  

	tree.heading("借阅人",text="借阅人")  #显示表头
	tree.heading("借阅时间",text="借阅时间")  #显示表头
	tree.heading("期刊名",text="期刊名")  #显示表头  
	tree.heading("期刊号",text="期刊号")  
	tree.heading("年",text="年")
	tree.heading("卷",text="卷")  #显示表头  
	tree.heading("期",text="期")  
	tree.heading("数量",text="数量")
	tree.heading("借阅状态",text="借阅状态")

	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)
	

	tk.Label(root,text='借阅人 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=14)
	tk.Label(root,text='年 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='期 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=2,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='卷 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=2,pady=14)
	tk.Label(root,text='数量 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=2,pady=14)
	
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	v5=tk.StringVar()
	v6=tk.StringVar()
	v7=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=3,padx=5,pady=14)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=3,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e7= tk.Entry(root,textvariable=v7,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=3,padx=5,pady=14)      # 进行表格式布局 . 

	def QingKong():
		v1.set('')
		v2.set('')
		v3.set('')
		v4.set('')
		v5.set('')
		v6.set('')
		v7.set('')
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		#scr011.delete(0, tk.END)
		pass
	
	def serch_borrow1():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from borrow where id = '%s'"%(v1.get())
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['id'],row['bookname'],row['kanhao'],row['year'],row['reel'],row['season'],row['bamount'],row['bdate'],row['bstate']))
				if(row['bstate']=='0'):
					v2.set(row['bookname'])
					v3.set(row['kanhao'])
					v4.set(row['year'])
					v5.set(row['reel'])
					v6.set(row['season'])
					v7.set(row['bamount'])
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
		pass
	def serch_borrow2():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from borrow where bookname='%s%s%s'and kanhao='%s' and year='%s'"%('%',v2.get(),'%',v3.get(),v4.get())
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['id'],row['bookname'],row['kanhao'],row['year'],row['reel'],row['season'],row['bamount'],row['bdate']))
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
		pass

	def Back():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if( v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''or v7.get()==''):
			mBox.showinfo('归还失败','内容填写不完整，归还失败!!')
			return
		sql="SELECT * from borrow where id='%s' and bstate='0'"%(v1.get())
		cur.execute(sql)
		data = cur.fetchone()
		sql="SELECT * from journal where bookname='%s' and kanhao='%s'and year='%s' and reel='%s' and season='%s'"%(v2.get(),v3.get(),v4.get(),v5.get(),v6.get())
		cur.execute(sql)
		print('1')
		data1 = cur.fetchone()
		if(data==None or data1==None):
			mBox.showinfo('归还失败','借阅记录不存在')
			return
		Amount=int(data['bamount'])+int(data1['amount'])
		print(int(data['bamount']),int(data1['amount']),Amount)
		sql1 = "UPDATE borrow SET bstate='1' where id='%s' and bookname='%s'and kanhao='%s' and year='%s'and reel='%s'and season='%s'and bamount='%s'and borrownum='%s'"%(User,data['bookname'],data['kanhao'],data['year'],data['reel'],data['season'],data['bamount'], data['borrownum'])
		sql2 = "UPDATE journal SET amount='%s' where bookname='%s'and kanhao='%s' and year='%s'and reel='%s'and season='%s'"%(Amount, v2.get(),v3.get(),v4.get(),v5.get(),v6.get())
		try:
			cur.execute(sql1)
			print('2')
			conn.commit()
			cur.execute(sql2)
			print('3')
			conn.commit()
			print('4')
			mBox.showinfo('归还成功','归还成功')
			sql1 = "SELECT id from reserve where bookname='%s'and kanhao='%s' and year='%s'and reel='%s'and season='%s'"%(v2.get(),v3.get(),v4.get(),v5.get(),v6.get())
			cur.execute(sql1)
			data = cur.fetchall()
			if(data):
				sql1="DELETE FROM reserve where bookname='%s'and kanhao='%s' and year='%s'and reel='%s'and season='%s'"%(v2.get(),v3.get(),v4.get(),v5.get(),v6.get())
				cur.execute(sql1)
				conn.commit()
				for row in data:
					sql1="INSERT INTO information(id,information,state,curtime) VALUES ('%s', '%s', 0, '%s')"%(row['id'],'你预约的期刊已在库重欢迎借阅\n'+v2.get()+v3.get()+v4.get()+v5.get()+v6.get(), randint(1, 1000000))
					cur.execute(sql1)
					conn.commit()
			return
			pass
		except:
			conn.rollback()
			mBox.showinfo('归还失败','内容填写不正确，归还失败')
			return
		mBox.showinfo('归还失败','请勿重复归还！')
		
		cur.close()
		conn.close()
	tk.Button(root,relief="groove", text="个人借阅情况",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch_borrow1).grid(row=0, column=4, sticky='E',pady=12,padx=5)
	tk.Button(root,relief="groove", text="期刊去向",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch_borrow1).grid(row=1, column=4, sticky='W',pady=12,padx=5)

	tk.Button(root,relief="groove", text="期刊归还",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Back).grid(row=2, column=4, sticky='E',pady=11,padx=5)
	tk.Button(root,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=QingKong).grid(row=3, column=4, sticky='W',pady=11,padx=5)
	pass


def PersonalInfo(tab01,User,root2):
	conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	cur = conn.cursor()
	sql1 = "SELECT * from user where id='%s'"%(User)
	cur.execute(sql1)
	data = cur.fetchone()

	
	tk.Label(root2,pady=10,text=User,font=("楷体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").pack()     # 自动调整布局   
	tk.Label(root2,pady=10,text=data['department'],font=("楷体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").pack()     # 自动调整布局 
	tk.Label(root2,pady=10,text=data['identity']+" "+data['name'],font=("楷体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").pack()     # 自动调整布局
	

	sql1 = "SELECT COUNT(*) from borrow where id='%s'and bstate='%s'"%(User,0)
	cur.execute(sql1)
	data = cur.fetchone()
	print(data)
	if(data):
		COUNT=data['COUNT(*)']
	else:
		COUNT=0
	tk.Label(root2,pady=10,text=str(COUNT)+"本书待还",font=("楷体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝",).pack()     # 自动调整布局  

	root21 = tk.LabelFrame(tab01,width=80,height=150, text='系统消息：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root21.pack(side=tk.TOP,fill=tk.X,padx=0,ipady=10)
	sql1 = "SELECT * from information where id='%s'"%(User)
	cur.execute(sql1)
	data = cur.fetchall()
	masg=''

	if(data):
		print(data)
		for row in data:
			masg=masg+row['information']+'\n'
	
	else:
		masg='暂无消息！'
	scr = scrolledtext.ScrolledText(root21, width=15,height=12, wrap=tk.WORD,bg="#B0C4DE LightSteelBlue 亮钢蓝")
	scr.pack()
	#fill=tk.BOTH,side=tk.TOP
	scr.insert(tk.INSERT,masg+'\n')
	#PersonalInfo(tab01)
	cur.close()
	conn.close()

def Article(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='文章信息查询')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=240, text='文章信息查询：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.TOP,fill=tk.X)

	rootR = tk.LabelFrame(tab01,width=240, text='查询结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=12,show="headings",columns=("期刊名","期刊号","文章题目","年","卷","期","作者","关键词"))#表格   
	tree.column("期刊名",width=90)   #表示列,不显示
	tree.column("期刊号",width=90)   #表示列,不显示  
	tree.column("文章题目",width=90)  
	tree.column("年",width=90)  
	tree.column("卷",width=90)   #表示列,不显示  
	tree.column("期",width=90)  
	tree.column("作者",width=90)
	tree.column("关键词",width=90)   #表示列,不显示  
  

	tree.heading("期刊名",text="期刊名")  #显示表头
	tree.heading("期刊号",text="期刊号")  #显示表头
	tree.heading("文章题目",text="文章题目")  #显示表头  
	tree.heading("年",text="年")  
	tree.heading("卷",text="卷")
	tree.heading("期",text="期")  #显示表头  
	tree.heading("作者",text="作者")  
	tree.heading("关键词",text="关键词")

	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)

	tk.Label(root,text='文章题目 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='作者 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=14)
	tk.Label(root,text='关键词 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
		
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	

	def serch_article1():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from aritcle where title like '%s%s%s'"%('%',v1.get(),'%')
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['title'],row['year'],row['reel'],row['season'],row['author'],row['keywords']))
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
		pass
	def serch_article2():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from aritcle where author like '%s%s%s'"%('%',v2.get(),'%')
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['title'],row['year'],row['reel'],row['season'],row['author'],row['keywords']))
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
		pass
	def serch_article3():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from aritcle where keywords like '%s%s%s'"%('%',v3.get(),'%')
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['title'],row['year'],row['reel'],row['season'],row['author'],row['keywords']))
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
		pass
	def QingKong():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		#scr011.delete(0, tk.END)
		pass

	
	
	
	tk.Button(root,relief="groove", text="文题查询",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch_article1).grid(row=0, column=2, sticky='E',pady=12,padx=5)
	tk.Button(root,relief="groove", text="作者查询",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch_article2).grid(row=1, column=2, sticky='W',pady=12,padx=5)

	tk.Button(root,relief="groove", text="关键词查询",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch_article3).grid(row=2, column=2, sticky='E',pady=11,padx=5)
	tk.Button(root,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=QingKong).grid(row=0, column=3, sticky='W',pady=11,padx=5)
	pass


def Recommend(R_Frame,User):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='读者推荐和信息修改')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=320, text='读者推荐期刊：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	rootR = tk.LabelFrame(tab01,width=320, text='个人信息修改：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.LEFT,fill=tk.BOTH)

	

	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=20) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=20)
	tk.Label(root,text='主办方 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=20)
	tk.Label(root,text='邮发代号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=20) # 对Label内容进行 表格式 布局
	
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=20)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=20)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=20)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=20)      # 进行表格式布局 . 

	def QingKong():
		#scr011.delete(0, tk.END)
		pass
	def Adding():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from recommend where bookname='%s' and booknum='%s'"%(v1.get(),v2.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data):
			mBox.showinfo('更新失败','推荐的项目已存在')
			return
		sql1 = "INSERT INTO recommend(bookname,booknum,host,youfadaihao) VALUES ('%s', '%s','%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get())
		try:
			cur.execute(sql1)
			conn.commit()
			pass
		except:
			conn.rollback()
			mBox.showinfo('更新失败','内容填写不正确，更新失败')
			return
		mBox.showinfo('更新成功','更新成功')
		cur.close()
		conn.close()	

	tk.Button(root,relief="groove", text="推荐",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Adding).grid(row=4, column=0, sticky='E',pady=20)
	tk.Button(root,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=QingKong).grid(row=4, column=1, sticky='W',pady=20,padx=30)



	tk.Label(rootR,text='用户名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=20) # 对Label内容进行 表格式 布局	
	tk.Label(rootR,text='密码 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=20)
	tk.Label(rootR,text='院系 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=20)
	tk.Label(rootR,text='姓名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=20) # 对Label内容进行 表格式 布局
	
	v20=tk.StringVar()
	v30=tk.StringVar()
	v40=tk.StringVar()    # 设置变量 . 
	
	tk.Label(rootR,text=User,font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=1,padx=5,pady=5)
	e20 = tk.Entry(rootR,textvariable=v20,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=14)
	e30= tk.Entry(rootR,textvariable=v30,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e40= tk.Entry(rootR,textvariable=v40,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)

	def Updating():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if( v20.get()==''or v30.get()==''or v40.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from user where id='%s'"%(User)
		cur.execute(sql)
		data = cur.fetchone()
		if(data==None):
			mBox.showinfo('更新失败','用户不存在')
			return
		print(v20.get(),v30.get(),v40.get(),User)
		sql1 = "UPDATE user SET password='%s',department='%s',name='%s' where id='%s'"%(v20.get(),v30.get(),v40.get(),User)
		print(v20.get(),v30.get(),v40.get(),User)
		try:
			cur.execute(sql1)
			conn.commit()
			pass
		except:
			conn.rollback()
			mBox.showinfo('更新失败','内容填写不正确，更新失败')
			return
		mBox.showinfo('更新成功','更新成功')
		cur.close()
		conn.close()
	def Clean():
		pass
	tk.Button(rootR,relief="groove", text="修改",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Updating).grid(row=4, column=0, sticky='E',pady=20)
	tk.Button(rootR,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Clean).grid(row=4, column=1, sticky='W',pady=20,padx=30)

	




def Govern(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='管理员界面')      # Add the tab
	
	def QingKong():
		#scr011.delete(0, tk.END)
		pass
	root = tk.LabelFrame(tab01,width=240, text='文章信息表更新：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	rootR = tk.LabelFrame(tab01,width=240, text='更新结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=22,show="headings",columns=("期刊名","期刊号","文章题目","年","卷","期","作者","关键词"))#表格  
	#tree["columns"]=  
	tree.column("期刊名",width=70)   #表示列,不显示
	tree.column("期刊号",width=65)   #表示列,不显示  
	tree.column("文章题目",width=65)  
	tree.column("年",width=40)  
	tree.column("卷",width=25)   #表示列,不显示  
	tree.column("期",width=25)  
	tree.column("作者",width=55)
	tree.column("关键词",width=65)   #表示列,不显示  
  

	tree.heading("期刊名",text="期刊名")  #显示表头
	tree.heading("期刊号",text="期刊号")  #显示表头
	tree.heading("文章题目",text="文章题目")  #显示表头  
	tree.heading("年",text="年")  
	tree.heading("卷",text="卷")
	tree.heading("期",text="期")  #显示表头  
	tree.heading("作者",text="作者")  
	tree.heading("关键词",text="关键词")

	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)

	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=14)

	tk.Label(root,text='文章题目 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='年 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='卷 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=5,column=0,pady=14)
	tk.Label(root,text='作者 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=6,column=0,pady=14)
	tk.Label(root,text='关键字 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=0,pady=14)
	
	v1=tk.StringVar()    # 设置变量 . 
	v12=tk.StringVar()
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	v5=tk.StringVar()
	v6=tk.StringVar()
	v7=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e12 = tk.Entry(root,textvariable=v12,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=5)       
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=4,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=5,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=6,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e7= tk.Entry(root,textvariable=v7,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=7,column=1,padx=5,pady=14)      # 进行表格式布局 . 

	def Adding():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v12.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''or v7.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败')
			return
		sql="SELECT * from aritcle where title='%s' and author='%s'"%(v2.get(),v6.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data):
			mBox.showinfo('更新失败','项目已存在')
			return
		sql1 = "INSERT INTO aritcle(bookname,kanhao,title,year,reel,season,author,keywords) VALUES ('%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')"%(v1.get(),v12.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get())
		try:
			cur.execute(sql1)
			conn.commit()
			pass
		except:
			conn.rollback()
			mBox.showinfo('更新失败','内容填写不完整，更新失败')
			return
		mBox.showinfo('更新成功','更新成功')
		cur.close()
		conn.close()
	def News():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from aritcle "
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['title'],row['year'],row['reel'],row['season'],row['author'],row['keywords']))
	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()	

	tk.Button(root,relief="groove", text="添加",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Adding).grid(row=8, column=0, sticky='E',pady=11)
	tk.Button(root,relief="groove", text="更新结果",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=News).grid(row=8, column=1, sticky='W',pady=11)
	pass




def SendInfo(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='用户管理')      # Add the tab
	root2 = tk.LabelFrame(tab01,width=240, text='发送消息内容：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root2.pack(side=tk.TOP,fill=tk.BOTH)
	root1 = tk.LabelFrame(tab01,width=240, text='发送系统消息：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root1.pack(side=tk.TOP,fill=tk.BOTH)
	root = tk.LabelFrame(tab01,width=240, text='用户查询：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.TOP,fill=tk.BOTH)
	root0 = tk.LabelFrame(tab01,width=240, text='用户查询结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root0.pack(side=tk.TOP,fill=tk.BOTH)
	
	
	tk.Label(root,text='用户名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,sticky=tk.W,padx=10,pady=10)
	v11=tk.StringVar()
	e11 = tk.Entry(root,textvariable=v11,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,sticky=tk.W,padx=10,pady=10)
	
	scr = scrolledtext.ScrolledText(root0, width=100,height=21, wrap=tk.WORD,bg="#F0F8FF AliceBlue 爱丽丝蓝")
	scr.pack()
	scr.insert(tk.INSERT,'显示用户信息\n')	

	def LookUp():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from user where id='%s'"%(v11.get())
		cur.execute(sql1)
		data = cur.fetchone()
		if(data==None):
			mBox.showinfo("查询失败",'不存在该用户！')
			return

		Astring="姓名：%s 用户名：%s 院系：%s 身份：%s"%(data['name'],data['id'],data['department'],data['identity'])
		scr.insert(tk.INSERT,Astring+'\n')
		#scr011.delete(0, tk.END)
		cur.close()
		conn.close()
		pass
	

	tk.Button(root,relief="groove", text="用户信息查询",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=LookUp).grid(row=0,column=2,sticky=tk.W,padx=10,pady=10)

	tk.Label(root1,text='用户名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,sticky=tk.W,padx=10,pady=10)
	v12=tk.StringVar()
	e12 = tk.Entry(root1,textvariable=v12,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,sticky=tk.W,padx=10,pady=10)
	
	v13=tk.StringVar()
	e13 = tk.Entry(root2,textvariable=v13, width=100,bg="#F0F8FF AliceBlue 爱丽丝蓝").pack()
	#scr1 = scrolledtext.ScrolledText(root2, width=100,height=11, wrap=tk.WORD,bg="#F0F8FF AliceBlue 爱丽丝蓝")
	#scr1.pack()
	#scr1.insert(tk.INSERT,'发送给用户的消息内容\n')	
	
	def Sending():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "INSERT INTO information(id,information,state,curtime) VALUES ('%s', '%s', 0, '%s')"%(v12.get(),v13.get(), randint(1, 1000000))
		if(v12.get()==''):
			mBox.showinfo('发送失败','请输入发送对象')
			return
		try:
			cur.execute(sql1)
			conn.commit()
			pass
		except:
			conn.rollback()
			mBox.showinfo('发送失败','消息发送失败')
			return
		mBox.showinfo('发送成功','消息发送成功')
		cur.close()
		conn.close()
	tk.Button(root1,relief="groove", text="发送",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Sending).grid(row=0,column=2,sticky=tk.W,padx=10,pady=10)
	
def Update(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='更新期刊种类表')      # Add the tab
	
	def QingKong():
		#scr011.delete(0, tk.END)
		pass
	root = tk.LabelFrame(tab01,width=240, text='期刊种类更新：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	rootR = tk.LabelFrame(tab01,width=240, text='更新结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=21,show="headings",columns=("期刊名","期刊号","主办方","周期","出版地","语种","开本","邮发代号"))#表格  
	#tree["columns"]=  
	tree.column("期刊名",width=55)   #表示列,不显示
	tree.column("期刊号",width=55)   #表示列,不显示  
	tree.column("主办方",width=55)  
	tree.column("周期",width=45)  
	tree.column("出版地",width=45)   #表示列,不显示  
	tree.column("语种",width=45)  
	tree.column("开本",width=55)
	tree.column("邮发代号",width=55)   #表示列,不显示  
  

	tree.heading("期刊名",text="期刊名")  #显示表头
	tree.heading("期刊号",text="期刊号")  #显示表头
	tree.heading("主办方",text="主办方")  #显示表头  
	tree.heading("周期",text="周期")  
	tree.heading("出版地",text="出版地")
	tree.heading("语种",text="语种")  #显示表头  
	tree.heading("开本",text="开本")  
	tree.heading("邮发代号",text="邮发代号")
	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)


	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=14)
	tk.Label(root,text='主办方 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='周期 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='出版地 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='语种 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=5,column=0,pady=14)
	tk.Label(root,text='开本 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=6,column=0,pady=14)
	tk.Label(root,text='邮发代号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=0,pady=14)
	
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()
	v5=tk.StringVar()    # 设置变量 . 
	v6=tk.StringVar()
	v7=tk.StringVar()
	v8=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=5)       
	e3 = tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=4,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=5,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e7= tk.Entry(root,textvariable=v7,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=6,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e8= tk.Entry(root,textvariable=v8,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=7,column=1,padx=5,pady=14)      # 进行表格式布局 . 

	def serch1():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from JournalType "
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['sponsor'],row['period'],row['chubandi'],row['language'],row['kaiben']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()	

	def ComeIn1():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''or v7.get()==''or v8.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from JournalType where bookname='%s' and kanhao='%s'and sponsor='%s' and period='%s' and chubandi='%s'and language='%s' and kaiben='%s' and youfadaihao='%s' "%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data==None):
			sql1 = "INSERT INTO JournalType(bookname,kanhao,sponsor,period,chubandi,language,kaiben,youfadaihao) VALUES ('%s', '%s','%s', '%s', '%s','%s', '%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get())
			try:
				cur.execute(sql1)
				conn.commit()
				mBox.showinfo('更新成功','更新成功')
			except:
				conn.rollback()
				mBox.showinfo('更新失败','更新失败')
			return
		else:
			mBox.showinfo('更新失败','该期刊已存在，更新失败!!')
			return		
		cur.close()
		conn.close()
	
	

	tk.Button(root,relief="groove", text="添加",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=ComeIn1).grid(row=8, column=0, sticky='E')
	tk.Button(root,relief="groove", text="更新结果",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch1).grid(row=8, column=1, sticky='W')
	pass

def Amount(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='期刊库存更新')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=240, text='库存查询更新：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	
	rootR = tk.LabelFrame(tab01,width=240, text='更新结果：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=20,show="headings",columns=("期刊名","期刊号","年","卷","期","数量"))#表格  
	#tree["columns"]=  
	tree.column("期刊名",width=70)   #表示列,不显示  
	tree.column("期刊号",width=70)  
	tree.column("年",width=70)  
	tree.column("卷",width=70)   #表示列,不显示  
	tree.column("期",width=70)  
	tree.column("数量",width=70)  
  
	tree.heading("期刊名",text="期刊名")  #显示表头  
	tree.heading("期刊号",text="期刊号")  
	tree.heading("年",text="年")
	tree.heading("卷",text="卷")  #显示表头  
	tree.heading("期",text="期")  
	tree.heading("数量",text="数量")

	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)

	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='年 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='卷 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=5,column=0,pady=14)
	tk.Label(root,text='数量 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=6,column=0,pady=14)
	#tk.Label(root,text='用户名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=0,pady=14)
	
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	v5=tk.StringVar()
	v6=tk.StringVar()
	#v7=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=4,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=5,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=6,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	#e7= tk.Entry(root,textvariable=v7,show='$',bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=7,column=1,padx=5,pady=14)      # 进行表格式布局 . 

	def serch1():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from journal where bookname like'%s%s%s'"%('%',v1.get(),'%')
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['year'],row['reel'],row['season'],row['amount']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
	def serch4():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from journal"
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['year'],row['reel'],row['season'],row['amount']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		

	def QingKong():
		v1.set('')
		v2.set('')
		v3.set('')
		v4.set('')
		v5.set('')
		v6.set('')
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		#scr011.delete(0, tk.END)
		pass

	def ComeIn():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from journal where bookname='%s' and kanhao='%s'and year='%s' and reel='%s' and season='%s' "%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data==None):
			sql1 = "INSERT INTO journal(bookname,kanhao,year,reel,season,amount) VALUES ('%s', '%s','%s', '%s', '%s','%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get())
			try:
				cur.execute(sql1)
				conn.commit()
				mBox.showinfo('更新成功','更新成功')
			except:
				conn.rollback()
				mBox.showinfo('更新失败','更新失败')
			return
		else:
			try:
				sql1 = "UPDATE journal SET amount='%s'where bookname='%s' and kanhao='%s'and year='%s' and reel='%s' and season='%s' "%(v6.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
				cur.execute(sql1)
				conn.commit()
				mBox.showinfo('更新成功','更新成功')
			except:
				conn.rollback()
				mBox.showinfo('更新失败','更新失败')
			return		
		cur.close()
		conn.close()

	tk.Button(root,relief="groove", text="搜索期刊",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch1).grid(row=1, column=0, sticky='E',pady=12)
	tk.Button(root,relief="groove", text="清空",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=QingKong).grid(row=1, column=1, sticky='W',pady=12)
	tk.Button(root,relief="groove", text="期刊入库",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=ComeIn).grid(row=8, column=0, sticky='E',pady=0)
	tk.Button(root,relief="groove", text="全部库存",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch4).grid(row=8, column=1, sticky='W',pady=0)
	pass

def Listing(R_Frame):
	tab01 = tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
	R_Frame.add(tab01, text='征订期刊')      # Add the tab
	
	root = tk.LabelFrame(tab01,width=240, text='添加到征订表中：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	root.pack(side=tk.LEFT,fill=tk.Y)

	rootR1 = tk.LabelFrame(tab01,width=240, text='征订信息：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR1.pack(side=tk.TOP,fill=tk.X)
	photo = tk.PhotoImage(file="教材订购.gif")
	theLabel = tk.Label(rootR1,image=photo,height=200,width=240,  
                   compound=tk.CENTER,bg="red")   #声明图片的位置
	theLabel.pack(side=tk.TOP,fill=tk.X,pady=10)     # 自动调整布局
	rootR = tk.LabelFrame(tab01,width=240, text='征订信息：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
	rootR.pack(side=tk.TOP,fill=tk.BOTH)

	tree=ttk.Treeview(rootR,height=8,show="headings",columns=("期刊名","期刊号","数量","排行"))#表格  
	#tree["columns"]=  
	tree.column("期刊名",width=150)   #表示列,不显示  
	tree.column("期刊号",width=150)  
	tree.column("数量",width=50) 
	tree.column("排行",width=50) 
  
	tree.heading("期刊名",text="期刊名")  #显示表头  
	tree.heading("期刊号",text="期刊号")  
	tree.heading("数量",text="数量")
	tree.heading("排行",text="排行")
	tree.pack()
 
#----vertical scrollbar------------
	vbar = ttk.Scrollbar(rootR,orient=tk.VERTICAL,command=tree.yview)
	tree.configure(yscrollcommand=vbar.set)
	tree.grid(row=0,column=0,sticky=tk.NSEW)
	vbar.grid(row=0,column=1,sticky=tk.NS)
 
#----horizontal scrollbar----------
	hbar = ttk.Scrollbar(rootR,orient=tk.HORIZONTAL,command=tree.xview)
	tree.configure(xscrollcommand=hbar.set)
	hbar.grid(row=1,column=0,sticky=tk.EW)

	tk.Label(root,text='期刊名 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=12) # 对Label内容进行 表格式 布局
	tk.Label(root,text='期刊号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=14)
	tk.Label(root,text='邮发代号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=3,column=0,pady=14)
	tk.Label(root,text='语种 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=4,column=0,pady=14) # 对Label内容进行 表格式 布局
	tk.Label(root,text='开本 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=5,column=0,pady=14)
	tk.Label(root,text='创刊年 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=6,column=0,pady=14)
	tk.Label(root,text='数量 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=7,column=0,pady=14)
	
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	v4=tk.StringVar()    # 设置变量 . 
	v5=tk.StringVar()
	v6=tk.StringVar()
	v7=tk.StringVar()
	
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=5)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=14)
	e3= tk.Entry(root,textvariable=v3,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=3,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e4= tk.Entry(root,textvariable=v4,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=4,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e5= tk.Entry(root,textvariable=v5,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=5,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e6= tk.Entry(root,textvariable=v6,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=6,column=1,padx=5,pady=14)      # 进行表格式布局 . 
	e7= tk.Entry(root,textvariable=v7,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=7,column=1,padx=5,pady=14)      # 进行表格式布局 . 

	def serch3():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from subscrib "
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['kanhao'],row['amount']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()
	def serch4():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from recommend "
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['booknum']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		

	def serch2():
		x=tree.get_children()
		for item in x:
			tree.delete(item)
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		sql1 = "SELECT * from recommend "
		cur.execute(sql1)
		data = cur.fetchall()
		i=0
		if(data):
		#print(data) tree.insert("",3 ,values=("1","2","3")) 
			for row in data:
				tree.insert("",0 ,values=(row['bookname'],row['booknum']))	
		else:
			mBox.showinfo('查询失败','暂无结果')
		cur.close()
		conn.close()		
	def ShenDing():
		conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		if(v1.get()==''or v2.get()==''or v3.get()==''or v4.get()==''or v5.get()==''or v6.get()==''or v7.get()==''):
			mBox.showinfo('更新失败','内容填写不完整，更新失败!!')
			return
		sql="SELECT * from subscrib where bookname='%s' and kanhao='%s'"%(v1.get(),v2.get())
		cur.execute(sql)
		data = cur.fetchone()
		if(data):
			mBox.showinfo('更新失败','添加的项目已存在！')
			return
		sql1 = "INSERT INTO subscrib(bookname,kanhao,youfadaihao,lan,kaiben,dateback,amount) VALUES ('%s', '%s','%s', '%s', '%s','%s', '%s')"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get())
		try:
			cur.execute(sql1)
			conn.commit()
			mBox.showinfo('更新成功','更新成功')
			pass
		except:
			conn.rollback()
			mBox.showinfo('更新失败','内容填写不正确，更新失败')
			return
		
		cur.close()
		conn.close()
	tk.Button(root,relief="groove", text="征订信息",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch3).grid(row=9, column=0, sticky='E',pady=12)
	tk.Button(root,relief="groove", text="读者推荐信息",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch4).grid(row=9, column=1, sticky='W',pady=12)

	tk.Button(root,relief="groove", text="添加征订期刊",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=ShenDing).grid(row=8, column=0, sticky='E',pady=11)
	tk.Button(root,relief="groove", text="期刊借阅排行",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=serch2).grid(row=8, column=1, sticky='W',pady=11)
	pass

def DengLu(tab1,Total,R_Frame):
	photo = tk.PhotoImage(file="1.gif",)
	theLabel = tk.Label(tab1,   # 将内容绑定在  root 初始框上面
						image=photo,height=200,width=80,   #载入图片
                   		compound=tk.CENTER,bg="#B0C4DE LightSteelBlue 亮钢蓝")   #声明图片的位置
                   #bg='reg'#指定背景颜色
                   
#textLabel.pack(fill=BOTH, expand=1)   # 致命 textlabel 在初识框 中的位置
#textLabel.pack(side=LEFT)
# 创建一个图像Label对象
	theLabel.pack(fill=tk.X)     # 自动调整布局
	root = tk.LabelFrame(tab1,height=3,width=80, text='请输入账号及密码：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
  
	root.pack(anchor=tk.S,fill=tk.BOTH,padx=0,ipady=10)

	tk.Label(root,text='帐号 :',bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,padx=3,pady=10) # 对Label内容进行 表格式 布局
	tk.Label(root,text='密码 :',bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,padx=3,pady=10)
	tk.Label(root,text='验证码 :',bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,padx=3,pady=10)
	v1=tk.StringVar()    # 设置变量 . 
	v2=tk.StringVar()
	v3=tk.StringVar()
	e3= tk.Entry(root,textvariable=v2,show='$',bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=10,pady=10)      # 进行表格式布局 . 
	e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=10,pady=10)            # 用于储存 输入的内容  
	e2 = tk.Entry(root,textvariable=v2,show='$',bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=10,pady=10)
      # 进行表格式布局 . 

	def show(R_Frame):
		Surch(R_Frame)
		conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=book2;UID=sa;PWD=sa')
		cursor = conn.cursor()##################!!!!!!!!!!!!!!!!!!!Mid是学号，改成char(10)
		cursor.execute("select Pw from Uer where Mid='%s'"%v1.get())###############################
		row = cursor.fetchone()
		print(row[0])
		if( v2.get()==row[0]):
			amain.destroy()
			return True
                
		else:
			return True#############################!!!!!!!!!!!!!!!!!!
    
	tk.Button(root,text='登录',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=show).grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 . 
	tk.Button(root,text='退出',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=15,command=Total.quit).grid(row=3,column=1,sticky=tk.E,padx=10,pady=10)
	pass