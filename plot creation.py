#importing library
from matplotlib import pyplot as plt
#print(plt.style.available)#it prints all style theme names
plt.style.use('fivethirtyeight')
#plt.xkcd()#like handwritten graph
import random 
data_x_axis=[21,25,22,38,29,33,26,28,27,31]
data_y_axis=[23123,12313,45233,43553,23353,24442,
             89855,23432,24244,66763]
data_x_axis.sort()
data_y_axis.sort()
#plt.plot(data_x_axis,data_y_axis)#creating plot

age=range(25,36)
salary=[]
js_salary=[]
for i in range(0,11):
    salary.append(random.randrange(45000,85000))
    js_salary.append(random.randrange(45000,85000))
salary.sort()
js_salary.sort()


plt.plot(data_x_axis,data_y_axis,color='#000',marker='.',label='All devs')
plt.plot(age,salary,color='g',linestyle='--',marker='o',label='Python devs')
plt.plot(age,js_salary,label='Js develper',color="r",linewidth=3)

#title
plt.title("Employee salary details by age")
#adding labels
plt.xlabel("Ages")
plt.ylabel("Salary")

#legend
#plt.legend(['All developers','Python devs'])
plt.legend()#used to show the plot labels

#plt.grid(True)
plt.tight_layout()#give some padding

#save as png
#plt.savefig('myplot.png')

plt.show()

#format strins details in matplotlib library
#marker='o' - big marker
#marker='.' - small marker