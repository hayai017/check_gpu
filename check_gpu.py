import torch
# cuda (GPU)を使用するかどうか(使用可能かどうか)
# falseになる場合はランタイムのタイプがGPUになっているか確認 
cuda = torch.cuda.is_available()
print(cuda)
# シード値の設定
torch.manual_seed(seed)
# デバイスの準備
device = torch.device("cuda" if cuda else "cpu")
print(device)
