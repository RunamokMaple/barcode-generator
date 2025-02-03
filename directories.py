import os

def create_directories(category, sub_category):
  # cwd = os.getcwd()

  category_dir = f"/tmp/output/{category}"
  sub_category_dir = f"{category_dir}/{sub_category}"
  sub_category_vector = f"{category_dir}/{sub_category}/vectors"

  # print(f"Looking at {category_dir} and {sub_category_dir}")


  os.makedirs(category_dir, exist_ok=True)
  os.makedirs(sub_category_dir, exist_ok=True)
  os.makedirs(sub_category_vector, exist_ok=True)