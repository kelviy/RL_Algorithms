import gymnasium as gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import namedtuple, deque
from itertools import count

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

env = gym.make("CartPole-v1", render_mode="rgb_array")

env.reset()
plt.imshow(env.render())
plt.show()