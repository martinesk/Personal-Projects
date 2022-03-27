import os
import tensorflow as tf
import Ipython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools

#load compressed model from tf_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'