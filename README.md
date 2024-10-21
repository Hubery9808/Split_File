# Split_File

概述
split_file.py 是一个用于将大文件分割为多个较小文件的 Python 脚本。该脚本按行读取输入文件，并根据给定的最大文件大小，将其拆分为多个部分文件。每个部分文件的大小将不超过指定的最大字节数。

功能
将一个大文件分割为多个较小的文件
支持自定义输出文件的名称前缀
支持设置每个分割文件的最大大小（字节）
使用说明
依赖
该脚本不需要额外的依赖，Python 标准库中的 os 模块即可运行。

参数说明
input_file：需要拆分的输入文件的路径。
output_prefix：输出文件的路径前缀。脚本会将拆分后的文件保存在该前缀目录下。
max_size：每个分割文件的最大大小（以字节为单位）。
示例
在脚本的示例中，可以看到如何使用该脚本来拆分一个文件：

python
复制代码
# 示例用法
input_file = r"C:\\Users\\Li\\Desktop\\1.txt"  # 需要分割的文件路径
output_prefix = r"C:\\Users\\Li\\Desktop\\output"  # 输出文件前缀
max_size = 100 * 1024 * 1024  # 每个文件的最大大小（单位：字节）

split_file(input_file, output_prefix, max_size)
运行步骤
下载并保存 split_file.py 文件到您的项目目录。
修改代码中的 input_file、output_prefix 和 max_size 参数以满足您的需求。
使用 Python 运行脚本：
bash
复制代码
python split_file.py
注意事项
确保输出目录存在或具有创建目录的权限。
根据文件的大小和 max_size 参数，分割过程可能会生成多个文件。
