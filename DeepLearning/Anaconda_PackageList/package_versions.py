
import os
print('\n++++++++++++++++++++++++++++++++++\n')
# OpenCV
import cv2
print('OpenCV\t\t: %s' % cv2.__version__)

# Tensorflow
import tensorflow
print('Tensorflow\t: %s' % tensorflow.__version__)

# Pytorch
import torch
print('PyTorch\t\t: %s' % torch.__version__)

# Keras
import keras
print('keras\t\t: %s' % keras.__version__)

# Numpy
import numpy as np
print('Numpy\t\t: %s' % np.__version__)


# Cuda Version
cuda_stream = os.popen('cat /usr/local/cuda/version.txt')
cuda_version = cuda_stream.read()
print('Cuda Version\t: %s' % cuda_version)

# Cudnn Version 
cudnn_stream = os.popen('cat /usr/include/cudnn_version.h | grep -m 1 CUDNN_MAJOR -A 2') #Cudnn_version.h only works for cuDNN >8.0 (https://stackoverflow.com/questions/31326015/how-to-verify-cudnn-installation/63568189#63568189?newreg=ab32f126911a4bdf90d9fdc0bc63172e)
cudnn_version = cudnn_stream.read()
print('Cudnn Version\t:\n%s' % cudnn_version)
print('\n++++++++++++++++++++++++++++++++++\n')
