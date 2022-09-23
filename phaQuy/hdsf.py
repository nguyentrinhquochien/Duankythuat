import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='pretrain.pt')
anh = './anh/OIP.jpg'
kq = model(anh)
kq.show()