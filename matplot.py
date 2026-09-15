import matplotlib.pyplot as plt
import numpy as np
'''x=[1,2,3,4,5]
y=[10,12,16,18,20]

plt.plot(x,y)
plt.title("Basic graph:")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

x=[1,2,3,4,5]
y=[10,12,16,18,20]
plt.plot(x,y,color='red',linestyle='--',linewidth=2,marker='o',markersize=8)
plt.title("cust graph")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()
cate=['A','B','C','D','E']
values=[20,30,45,27,67]
plt.bar(cate,values, color='green')
plt.title('bar chart')
plt.show()
s1=[40,30,56,70]
s2=['java','c','php','python']

plt.pie(s1,labels=s2,autopct='%1.1f%%',startangle=100)
plt.title("pie chart")
plt.axis('equal')
plt.show()
x=[1,2,3,4]
y1=[i**2 for i in x]
y2=[i**3 for i in x]

plt.plot(x,y1,label='x^2',color='pink')
plt.plot(x,y2,label='x^3',color='purple')
plt.legend()
plt.title('matplot is fun')
plt.xlabel(' x cutie(not ex, as if i have one)')
plt.ylabel('y cutie')
plt.show()
x=[1,2,3,4]
y1=[i**2 for i in x]
y2=[i**3 for i in x]
fig,axs=plt.subplots(2,2)
axs[0,0].plot(x,y1)
axs[0,0].set_title('x^2')
cate=['A','B','C','D','E']
values=[20,30,45,27,67]
axs[0,1].bar(cate,values)
axs[0,1].set_title('Bar')
axs[1,0].plot(x,y2)
axs[1,0].set_title('x^3')
s1=[40,30,56,70]
s2=['java','c','php','python']
axs[1,1].pie(s1,labels=s2,autopct='%1.1f%%',startangle=100)
axs[1,1].set_title('Pie')
plt.show()'''
x=np.random.rand(100)
y=np.random.rand(100)
cl=np.random.rand(100)

plt.scatter(x,y,c=cl,cmap='viridis')
plt.title('Scatter')
plt.colorbar()
plt.show()