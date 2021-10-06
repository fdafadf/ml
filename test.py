import matplotlib.pyplot as plt
import numpy as np

def show_linear_regresion_error_lines(data):
  a = 0.1
  b = 0.4
  for i in range(len(data)):
    plt.annotate('  $y_' + str(i) + '$', (data[i]))
  for x, y in data:
    plt.plot([x, x], [a * x + b, y], color='red')
  plt.scatter(*data.T, color='green')
  data_p = np.array([[x, a * x + b] for [x, y] in data])
  plt.scatter(*data_p.T)
  for i in range(len(data_p)):
    x, y = data_p[i]
    plt.annotate('  $\hat{y}_' + str(i) + '$', (x, y + 0.015))
  plt.plot([0, 1], [b, a + b])
  plt.show()
