-- 指定数据目录
python -m qlib.cli.data qlib_data --target_dir /Volumes/vdata/data/qlib_data/cn_data_1min --region cn --interval 1min

python scripts/get_data.py qlib_data --target_dir /Volumes/vdata/data/qlib_data/cn_data --region cn 