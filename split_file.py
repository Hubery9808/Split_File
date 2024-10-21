import os

def split_file(input_file, output_prefix, max_size):
    # 检查并创建目标文件夹
    if not os.path.exists(output_prefix):
        os.makedirs(output_prefix)
    
    # 打开输入文件
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        part_num = 1  # 文件部分编号
        output_file = os.path.join(output_prefix, f"{part_num}.log")
        output = open(output_file, 'w', encoding='utf-8')
        current_size = 0
        
        # 按行读取文件
        for line in f:
            output.write(line)
            current_size += len(line.encode('utf-8'))  # 计算当前写入的字节数
            
            # 如果当前文件超过了max_size，关闭当前文件，准备写入下一个部分
            if current_size >= max_size:
                output.close()
                part_num += 1
                output_file = os.path.join(output_prefix, f"{part_num}.log")
                output = open(output_file, 'w', encoding='utf-8')
                current_size = 0
        
        output.close()

# 示例用法
input_file = r"C:\Users\Li\桌面\1.txt" # 被处理文件路径
output_prefix = r"C:\Users\Li\桌面\分割文件" # 输出文件夹路径
max_size = 500 * 1024 * 1024  # 500MB
split_file(input_file, output_prefix, max_size)
