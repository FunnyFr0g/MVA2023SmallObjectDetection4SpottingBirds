export TORCH_DISTRIBUTED_DEBUG="DETAIL"
export CUDA_VISIBLE_DEVICES=0
export OMP_NUM_THREADS=16
export MKL_NUM_THREADS=16
GPU_NUM=1


###############################
# Step 5: To generate the predictions for submission, the result will be saved in results.bbox.json.
###############################
echo "###############################"
echo "Step 5: To generate the predictions for submission, the result will be saved in results.bbox.json."
echo "###############################"
bash tools/test.sh configs/mva2023_baseline_copy/centernet_resnet18_140e_coco_inference.py work_dirs/centernet_resnet18_140e_coco_hard_negative_training/latest.pth --format-only --eval-options jsonfile_prefix=results

_time=date +%Y%m%d%H%M
mkdir -p submit/${_time}
SUBMIT_FILE=echo ./submit/${_time}/results.json
SUBMIT_ZIP_FILE=echo ${SUBMIT_FILE//results.json/submit.zip}
mv ./results.bbox.json $SUBMIT_FILE
zip $SUBMIT_ZIP_FILE $SUBMIT_FILE


read -p "press any button..." -n1 -s