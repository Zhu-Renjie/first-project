import tkinter as tk
from tkinter import ttk
from defImageChange import image_change
from Denglu import *
import pymysql.cursors

FUN_ADD=False
User="100010"

total = tk.Tk()   
total.title("欢迎登录期刊管理系统！")
total.resizable(1,1)#宽可变, 高可变

Head_Frame=tk.Frame(total,height=1,bg="#4682B4 SteelBlue 钢蓝/铁青")
#image_change(Head_Frame)
Tail_Frame=tk.Frame(total,height=1,bg="#4682B4 SteelBlue 钢蓝/铁青")

L_Frame=ttk.Notebook(total,width=240)

L_Frame.pack(side=tk.LEFT, fill="y",ipadx=50)




R_Frame = ttk.Notebook(total)
Info_Frame = ttk.Notebook(total)
#####################
tab01=tk.Frame(Info_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
Info_Frame.add(tab01, text='   个人信息')
root2 = tk.LabelFrame(tab01,width=80, text='个性头像：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
root2.pack(anchor=tk.S,fill=tk.X,padx=0,ipady=10)
User_photo = tk.PhotoImage(file="头像.gif",height=70,width=70)
tk.Label(root2,pady=10,image=User_photo,compound=tk.CENTER,).pack(pady=10)

#R_Frame.pack(expand=1, fill="both")  # Pack to make visible
###########################Left#################
tab00=tk.Frame(L_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
L_Frame.add(tab00, text='      登录',)


#####################
tab02=tk.Frame(L_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
L_Frame.add(tab02, text='       注册')
photo2 = tk.PhotoImage(file="教材订购.gif")
theLabel2 = tk.Label(tab02,   # 将内容绑定在  root 初始框上面
						padx=100,   image=photo2,height=200,width=240,   #载入图片
                   compound=tk.CENTER,bg="#B0C4DE LightSteelBlue 亮钢蓝")
theLabel2.pack(fill=tk.X)
ZhuCe(tab02,total)
###########################Left#################

photo1 = tk.PhotoImage(file="欢迎新同学.gif")
theLabel = tk.Label(tab00,   # 将内容绑定在  root 初始框上面
padx=100,image=photo1,height=200,width=240,   #载入图片
                   compound=tk.CENTER,bg="#B0C4DE LightSteelBlue 亮钢蓝")
                   
#textLabel.pack(fill=BOTH, expand=1)   # 致命 textlabel 在初识框 中的位置
#textLabel.pack(side=LEFT)
# 创建一个图像Label对象
theLabel.pack(fill=tk.X)     # 自动调整布局

root = tk.LabelFrame(tab00,width=240, text='请输入账号及密码：',bg="#B0C4DE LightSteelBlue 亮钢蓝")
  
root.pack(anchor=tk.S,fill=tk.BOTH,padx=0,ipady=0)

tk.Label(root,text='帐号 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=0,column=0,pady=20) # 对Label内容进行 表格式 布局
tk.Label(root,text='密码 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=1,column=0,pady=20)
tk.Label(root,text='验证码 :',font=("宋体", 15),bg="#B0C4DE LightSteelBlue 亮钢蓝").grid(row=2,column=0,pady=20)
v1=tk.StringVar()   
v2=tk.StringVar()
v3=tk.StringVar()

e1 = tk.Entry(root,textvariable=v1,bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=0,column=1,padx=5,pady=20)            # 用于储存 输入的内容  
e2 = tk.Entry(root,textvariable=v2,show='$',bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=1,column=1,padx=5,pady=30) 
e3= tk.Entry(root,textvariable=v2,show='$',bg="#F0F8FF AliceBlue 爱丽丝蓝").grid(row=2,column=1,padx=5,pady=30)      # 进行表格式布局 . 
v1.set('100003')
v2.set('123456')
def show():
	global FUN_ADD,User
	conn = pymysql.connect( host='101.132.122.108',port=3306,user='root',password='1234',db='journal',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	cur = conn.cursor()
	sql1 = "SELECT * from user where id='%s'"%(v1.get())
	cur.execute(sql1)
	data = cur.fetchone()
	if(data):
		key=data['password']
		User=data['id']
		print(key,User,data['identity'])
	else:
		mBox.showinfo('登录失败','用户名不存在！')
		return


	
	if( FUN_ADD==False):
		if(data['identity']=='学生' and key==v2.get()):
			Surch(R_Frame,User)
			Revert(R_Frame,User)
			Article(R_Frame)
			Recommend(R_Frame,User)
			L_Frame.pack_forget()
			Head_Frame.pack(side=tk.TOP,fill= tk.X)
			image_change(Head_Frame)
			Tail_Frame.pack(side=tk.TOP,fill= tk.X)
			PersonalInfo(tab01,User,root2)
			Info_Frame.pack(side=tk.LEFT, fill="y",ipadx=50)			
			R_Frame.pack(expand=1, fill="both")  # Pack to make visible
			FUN_ADD=True

		elif(data['identity']=='管理员' and key==v2.get()):
			Surch(R_Frame,User)
			Revert(R_Frame,User)
			Article(R_Frame)
			Recommend(R_Frame,User)
			Govern(R_Frame)
			SendInfo(R_Frame)
			L_Frame.pack_forget()
			Head_Frame.pack(side=tk.TOP,fill= tk.X)
			image_change(Head_Frame)
			Tail_Frame.pack(side=tk.TOP,fill= tk.X)
			PersonalInfo(tab01,User,root2)
			Info_Frame.pack(side=tk.LEFT, fill="y",ipadx=50)		
			R_Frame.pack(expand=1, fill="both")  # Pack to make visible
			FUN_ADD=True

		elif(data['identity']=='采购员' and key==v2.get()):
			Surch(R_Frame,User)
			Revert(R_Frame,User)
			Article(R_Frame)
			Recommend(R_Frame,User)
			Update(R_Frame)
			Amount(R_Frame)
			Listing(R_Frame)
			L_Frame.pack_forget()
			Head_Frame.pack(side=tk.TOP,fill= tk.X)
			image_change(Head_Frame)
			Tail_Frame.pack(side=tk.TOP,fill= tk.X)
			PersonalInfo(tab01,User,root2)
			Info_Frame.pack(side=tk.LEFT, fill="y",ipadx=50)			
			R_Frame.pack(expand=1, fill="both")  # Pack to make visible
			FUN_ADD=True
		else:mBox.showinfo('登录失败','密码错误！')
	cur.close()
	conn.close()

			
tk.Button(root,text='登录',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=10,command=show).grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 . 
tk.Button(root,text='退出',relief="groove",bg="#87CEFA LightSkyBlue 亮天蓝色",font=("宋体", 15),width=10,command=total.quit).grid(row=3,column=1,sticky=tk.E,padx=10,pady=10)




###########################Right#################
tab10=tk.Frame(R_Frame,bg="#B0C4DE LightSteelBlue 亮钢蓝")            # Create a tab 
R_Frame.add(tab10, text='        欢迎登录',)
photo = tk.PhotoImage(file="欢迎新同学.gif")
theLabel = tk.Label(tab10,   # 将内容绑定在  root 初始框上面
padx=100,   image=photo,height=200,width=50,   #载入图片
                   compound=tk.CENTER,bg="#B0C4DE LightSteelBlue 亮钢蓝")   #声明图片的位置
                   #bg='reg'#指定背景颜色
                   
#textLabel.pack(fill=BOTH, expand=1)   # 致命 textlabel 在初识框 中的位置
#textLabel.pack(side=LEFT)
# 创建一个图像Label对象
theLabel.pack(expand=1,fill=tk.X)     # 自动调整布局



######################

###########################Right#################
total.mainloop()