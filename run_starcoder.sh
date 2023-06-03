export HF_HOME=/scratch/wl678/huggingface
export CUDA_VISIBLE_DEVICES=0
TASK="humaneval"
TASK="selfdebug"
SAVE_FILE="starcoder_humaneval_t02.json"
SAVE_FILE="starcoder_humaneval_t02_iter1.json"
echo "Running task $TASK"
echo "Saving to $SAVE_FILE"

accelerate launch  main.py \
  --model bigcode/starcoder \
  --max_length_generation 4096\
  --tasks $TASK \
  --n_samples 1 \
  --batch_size 1 \
  --temperature 0.2 \
  --allow_code_execution \
  --trust_remote_code \
  --save_generations \
  --use_auth_token \
  --precision fp16 \
  --save_generations_path $SAVE_FILE \
# --top_p 0.95 \