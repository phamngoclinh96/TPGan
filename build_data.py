import pandas as pd
import cv2
import glob
import os

if __name__ == '__main__':
    with open('data/train.csv', 'w') as f:
        for file in glob.glob('data/MultiPIE/15/*cropped.png'):
            f.write(os.path.basename(file))
            f.write('\n')
