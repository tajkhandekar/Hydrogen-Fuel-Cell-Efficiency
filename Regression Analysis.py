import pandas
import numpy
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
scale = StandardScaler()

data = pandas.read_csv("AllData.csv")

X = data[['Time', 'pH', 'Ultrasonic']]
distx = data['Distance']
timex = data['Time']
phx = data['pH']
ultrax = data['Ultrasonic']

y = data['Voltage']

scaledX = scale.fit_transform(X)

regression = linear_model.LinearRegression()
regression.fit(scaledX, y)

print(regression.coef_)

model = numpy.poly1d(numpy.polyfit(ultrax, y, 4))

line = numpy.linspace(0, 5, 209)
# create scatter plot for each independent variable

plt.scatter(ultrax, y)
plt.plot(line, model(line))
plt.show()
