export HF_HOME=/scratch/wl678/huggingface
export CUDA_VISIBLE_DEVICES=0
accelerate launch  main.py \
  --model bigcode/starcoder \
  --max_length_generation 8192\
  --tasks selfdebug \
  --n_samples 1 \
  --batch_size 1 \
  --temperature 0.2 \
  --allow_code_execution \
  --trust_remote_code \
  --save_generations \
  --use_auth_token \
  --precision fp16 \
  --top_p 0.95 \
  --save_generations_path starcoder_humaneval_t02_iter1.json