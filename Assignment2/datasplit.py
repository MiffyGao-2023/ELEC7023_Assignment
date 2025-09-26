# 导入所需的库
import os
import shutil
import random

# 1. 设置源文件夹路径 (您从 Kaggle 解压后的数据集位置)
source_dir = '/path/to/your/downloaded/kaggle_dataset' 

# 2. 设置目标文件夹路径 (您为作业创建的新数据集文件夹)
target_dir = '/path/to/your/new/My_Fruit_Dataset'

# 3. 列出您选择的水果类别 (文件夹名称必须完全匹配)
# 例如，我们选择苹果、香蕉、芒果和草莓
selected_classes = ['Apples', 'Bananas', 'Mangoes', 'Strawberries']

# 4. 定义划分比例
split_ratio = {'train': 0.7, 'validation': 0.2, 'test': 0.1}

# --- 修改结束，以下代码无需改动 ---

print(f"开始处理数据集，将从 '{source_dir}' 复制到 '{target_dir}'")

# 创建目标目录结构
for split_name in split_ratio.keys(): # 'train', 'validation', 'test'
    split_path = os.path.join(target_dir, split_name)
    os.makedirs(split_path, exist_ok=True)
    for class_name in selected_classes:
        class_path = os.path.join(split_path, class_name)
        os.makedirs(class_path, exist_ok=True)

# 遍历每个选择的类别
for class_name in selected_classes:
    class_source_path = os.path.join(source_dir, class_name)
    
    if not os.path.isdir(class_source_path):
        print(f"警告：找不到源类别文件夹 '{class_source_path}'，已跳过。")
        continue

    # 获取该类别下的所有图片文件
    images = [f for f in os.listdir(class_source_path) if os.path.isfile(os.path.join(class_source_path, f))]
    random.shuffle(images) # 随机打乱文件顺序
    
    total_images = len(images)
    print(f"处理类别 '{class_name}': 共 {total_images} 张图片。")

    # 计算分割点
    train_end = int(total_images * split_ratio['train'])
    validation_end = train_end + int(total_images * split_ratio['validation'])

    # 分割文件列表
    train_files = images[:train_end]
    validation_files = images[train_end:validation_end]
    test_files = images[validation_end:]

    # 定义一个辅助函数来复制文件
    def copy_files(files, split_name):
        for file_name in files:
            source_file_path = os.path.join(class_source_path, file_name)
            destination_path = os.path.join(target_dir, split_name, class_name, file_name)
            shutil.copy2(source_file_path, destination_path)
        print(f"  - 已复制 {len(files)} 张图片到 '{split_name}/{class_name}' 文件夹。")

    # 执行复制
    copy_files(train_files, 'train')
    copy_files(validation_files, 'validation')
    copy_files(test_files, 'test')

print("\n数据集划分完成！")

# --- 第三步：创建 labels.txt ---
labels_file_path = os.path.join(target_dir, 'labels.txt')
with open(labels_file_path, 'w') as f:
    for class_name in selected_classes:
        f.write(class_name + '\n')

print(f"已在 '{target_dir}' 中成功创建 'labels.txt' 文件。")