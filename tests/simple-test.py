from matfiles import loadmat
from pathlib import Path

fpath = Path('../test-data/simple.mat')

contents = loadmat(fpath)
print(contents)