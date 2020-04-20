import numpy as np
import matplotlib.pyplot as plt

board = np.zeros((8,8))

board[1::2, 0::2] == 1
board[0::2, 1::2] = 1

#Overlap due to missing black squares
board[1::2, 2::2] = 1
board[1::2, 0] = 1

plt.imshow(board, cmap = 'binary')
plt.show()
