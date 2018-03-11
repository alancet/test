%matplotlib inline
%config InlineBackend.figure_format = 'svg'

import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


print(sys.version)

mpl.style.use('ggplot')
x = np.linspace(0, 10, 500)


x = 1111 * x


plt.plot(x, np.sin(x))
plt.show()
