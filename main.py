def main():
    print("Ara Voice trainer 1.0.0 in development")
    print("checking system")
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function

    import argparse
    import os.path
    import sys

    import numpy as np
    from six.moves import xrange
    import tensorflow as tf
    import train
    import freeze

    import input_data
    import models
    from tensorflow.python.platform import gfile
    print("Stating...")
    train.main()
    print("Exporting to .tflite")
    freeze.main()
    print("done")
