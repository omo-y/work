import streamlit as st
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
y = [2, 5, 3, 0, 10, 9]

plt.plot(x, y)
plt.show()