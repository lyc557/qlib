uv venv
source venv/bin/activate
uv pip install pyqlib -i https://pypi.tuna.tsinghua.edu.cn/simple

uv pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
uv pip install --upgrade cython -i https://pypi.tuna.tsinghua.edu.cn/simple

# 需要安装 python3.12-dev build-essential
sudo apt-get update
sudo apt-get install python3.12-dev build-essential

uv pip install -e ".[rl,dev,analysis]" -i  https://mirrors.aliyun.com/pypi/simple/

-- 指定数据目录
# 获取日频数据
python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

# 获取分钟频数据
python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data_1min --region cn --interval 1min