#imports csv comma seperated values
import csv
import pandas as pd
import plotly.express as px

#we open the csv file as f
#we read the file with the help of reader
#we convert the data into a list using the variable file_data
with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

#two variables
#total_marks is the value 0
#len means length
total_marks = 0
total_entries = len(file_data)

#requirements for for loop: 
#First- A variable with some intial value
#Second- The limit of repeition
#Third- how the variable changes in every cycle
#For(var i=0;i<5;i=i+1)
#using the data type float to take care of decimal values
for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))



df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()
