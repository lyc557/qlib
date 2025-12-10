import qlib
from qlib.data import D

qlib.init(provider_uri='~/.qlib/qlib_data/cn_data')

# 获取交易日历
calendar = D.calendar()
print(f"交易日历长度: {len(calendar)}")
print(f"最近5个交易日: {calendar[-5:]}")

# 获取股票列表
instruments = D.instruments(market='csi300')
stock_list = D.list_instruments(instruments=instruments, as_list=True)
print(f"CSI300成分股数量: {len(stock_list)}")
print(f"部分成分股: {stock_list[:5]}")


from qlib.contrib.report import analysis_model, analysis_position

# 获取记录器
recorder = R.get_recorder(recorder_id=ba_rid, experiment_name="backtest_analysis")

# 加载回测结果
pred_df = recorder.load_object("pred.pkl")  # 预测结果
report_normal_df = recorder.load_object("portfolio_analysis/report_normal_1day.pkl")  # 普通报告
positions = recorder.load_object("portfolio_analysis/positions_normal_1day.pkl")  # 持仓记录
analysis_df = recorder.load_object("portfolio_analysis/port_analysis_1day.pkl")  # 分析报告