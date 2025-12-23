from huggingface_hub import HfApi, login

HF_TOKEN = "your_huggingface_token"

login(token=HF_TOKEN)
print("Login success!")

api = HfApi()
username = api.whoami()['name']  
model_name = "yolov5s-gazebosim-finetune" 
repo_id = f"{username}/{model_name}"

result_folder = "/content/yolov5/runs/train/yolov5s_results"

print(f"Create repository: {repo_id}...")
api.create_repo(repo_id=repo_id, exist_ok=True, repo_type="model")

print(f"Up model {result_folder}...")
api.upload_folder(
    folder_path=result_folder,
    repo_id=repo_id,
    repo_type="model",
    commit_message="initial commit"
)

print(f"Done!: https://huggingface.co/{repo_id}")