pip install -U openmim
mim install mmcv-full==1.6.0
pip install matplotlib

cd /root/mva23/MVA2023SmallObjectDetection4SpottingBirds
pip install -v -e .

apt update
apt install -y libgl1-mesa-glx libglib2.0-0

mkdir -p work_dirs/centernet_resnet18_140e_coco1
touch work_dirs/centernet_resnet18_140e_coco1/latest.pth