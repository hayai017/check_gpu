from __future__ import print_function
import argparse
import torch
import torch.utils.data
from torch import nn, optim
from torch.nn import functional as F
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os

# バッチサイズ
batch_size = 32
# エポック数
epochs = 100
# 乱数の種
seed = 123
# ログ表示のインターバル
log_interval = 10
# 結果出力ディレクトリの作成
os.makedirs("results", exist_ok=True)

# cuda (GPU)を使用するかどうか(使用可能かどうか)
# falseになる場合はランタイムのタイプがGPUになっているか確認 
cuda = torch.cuda.is_available()
print(cuda)
# シード値の設定
torch.manual_seed(seed)
# デバイスの準備
device = torch.device("cuda" if cuda else "cpu")
print(device)