from matplotlib import pyplot as plt 
import random
import numpy as np

age=range(25,36)

x_indexes = np.arange(len(age))
width = 0.25
# print(x_indexes)
salary=[]
js_salary=[]
for i in range(0,11):
    salary.append(random.randrange(45000,85000))
    js_salary.append(random.randrange(45000,85000))
salary.sort()
js_salary.sort()

plt.bar(x_indexes-width,salary,label='Python',width=width)
plt.bar(x_indexes+width,js_salary,label='Js',width=width)
plt.title("Employee salary details by age")
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.xticks(ticks=x_indexes,labels=age)
plt.legend()
plt.show()
#creating width variable use align bar chart side by side
#and add width=width
#plot.barh - used to create horizontal bar chart