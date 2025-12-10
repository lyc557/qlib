[![Python 版本](https://img.shields.io/pypi/pyversions/pyqlib.svg?logo=python&logoColor=white)](https://pypi.org/project/pyqlib/#files)
[![平台支持](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)](https://pypi.org/project/pyqlib/#files)
[![PyPI 版本](https://img.shields.io/pypi/v/pyqlib)](https://pypi.org/project/pyqlib/#history)
[![上传 Python 包](https://github.com/microsoft/qlib/workflows/Upload%20Python%20Package/badge.svg)](https://pypi.org/project/pyqlib/)
[![Github Actions 测试状态](https://github.com/microsoft/qlib/workflows/Test/badge.svg?branch=main)](https://github.com/microsoft/qlib/actions)
[![文档状态](https://readthedocs.org/projects/qlib/badge/?version=latest)](https://qlib.readthedocs.io/en/latest/?badge=latest)
[![许可证](https://img.shields.io/pypi/l/pyqlib)](LICENSE)
[![在 Gitter 上加入聊天](https://badges.gitter.im/Microsoft/qlib.svg)](https://gitter.im/Microsoft/qlib?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## :newspaper: **最新动态!** &nbsp;   :sparkling_heart: 

近期发布的功能

### 介绍 <a href="https://github.com/microsoft/RD-Agent"><img src="docs/_static/img/rdagent_logo.png" alt="RD_Agent" style="height: 2em"></a>：基于LLM的工业数据驱动研发自主演进智能体

我们很高兴宣布发布 **RD-Agent**📢，这是一个强大的工具，支持量化投资研发中的自动化因子挖掘和模型优化。

RD-Agent 现已在 [GitHub](https://github.com/microsoft/RD-Agent) 上可用，欢迎您为其点星🌟！

了解更多信息，请访问我们的 [♾️演示页面](https://rdagent.azurewebsites.net/)。在这里，您将找到英文和中文的演示视频，帮助您更好地理解 RD-Agent 的应用场景和使用方法。

我们为您准备了几个演示视频：
| 场景 | 演示视频 (英文) | 演示视频 (中文) |
| --                      | ------    | ------    |
| 量化因子挖掘 | [链接](https://rdagent.azurewebsites.net/factor_loop?lang=en) | [链接](https://rdagent.azurewebsites.net/factor_loop?lang=zh) |
| 基于报告的量化因子挖掘 | [链接](https://rdagent.azurewebsites.net/report_factor?lang=en) | [链接](https://rdagent.azurewebsites.net/report_factor?lang=zh) |
| 量化模型优化 | [链接](https://rdagent.azurewebsites.net/model_loop?lang=en) | [链接](https://rdagent.azurewebsites.net/model_loop?lang=zh) |

- 📃**论文**: [R&D-Agent-Quant: 一个面向数据中心的因子与模型联合优化的多智能体框架](https://arxiv.org/abs/2505.15155)
- 👾**代码**: https://github.com/microsoft/RD-Agent/
```BibTeX
@misc{li2025rdagentquant,
    title={R\&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization},
    author={Yuante Li and Xu Yang and Xiao Yang and Minrui Xu and Xisen Wang and Weiqing Liu and Jiang Bian},
    year={2025},
    eprint={2505.15155},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
![image](https://github.com/user-attachments/assets/3198bc10-47ba-4ee0-8a8e-46d5ce44f45d)

***

| 功能 | 状态 |
| --                      | ------    |
| [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155) 发布 | 将 R&D-Agent 应用于 Qlib 进行量化交易 | 
| 用于端到端学习的 BPQP | 📈即将推出！([审核中](https://github.com/microsoft/qlib/pull/1863)) |
| 🔥LLM驱动的自动量化工厂🔥 | 🚀 已于 2024年8月8日 在 [♾️RD-Agent](https://github.com/microsoft/RD-Agent) 中发布 |
| KRNN 和 Sandwich 模型 | :chart_with_upwards_trend: 已于 2023年5月26日 [发布](https://github.com/microsoft/qlib/pull/1414/) |
| 发布 Qlib v0.9.0 | :octocat: 已于 2022年12月9日 [发布](https://github.com/microsoft/qlib/releases/tag/v0.9.0) |
| 强化学习框架 | :hammer: :chart_with_upwards_trend: 已于 2022年11月10日 发布。 [#1332](https://github.com/microsoft/qlib/pull/1332), [#1322](https://github.com/microsoft/qlib/pull/1322), [#1316](https://github.com/microsoft/qlib/pull/1316),[#1299](https://github.com/microsoft/qlib/pull/1299),[#1263](https://github.com/microsoft/qlib/pull/1263), [#1244](https://github.com/microsoft/qlib/pull/1244), [#1169](https://github.com/microsoft/qlib/pull/1169), [#1125](https://github.com/microsoft/qlib/pull/1125), [#1076](https://github.com/microsoft/qlib/pull/1076)|
| HIST 和 IGMTF 模型 | :chart_with_upwards_trend: 已于 2022年4月10日 [发布](https://github.com/microsoft/qlib/pull/1040) |
| Qlib [notebook 教程](https://github.com/microsoft/qlib/tree/main/examples/tutorial) | 📖 已于 2022年4月7日 [发布](https://github.com/microsoft/qlib/pull/1037) | 
| Ibovespa 指数数据 | :rice: 已于 2022年4月6日 [发布](https://github.com/microsoft/qlib/pull/990) |
| 时点数据库 | :hammer: 已于 2022年3月10日 [发布](https://github.com/microsoft/qlib/pull/343) |
| Arctic 提供者后端及订单簿数据示例 | :hammer: 已于 2022年1月17日 [发布](https://github.com/microsoft/qlib/pull/744) |
| 基于元学习的框架 & DDG-DA  | :chart_with_upwards_trend:  :hammer: 已于 2022年1月10日 [发布](https://github.com/microsoft/qlib/pull/743) | 
| 基于规划的资产组合优化 | :hammer: 已于 2021年12月28日 [发布](https://github.com/microsoft/qlib/pull/754) | 
| 发布 Qlib v0.8.0 | :octocat: 已于 2021年12月8日 [发布](https://github.com/microsoft/qlib/releases/tag/v0.8.0) |
| ADD 模型 | :chart_with_upwards_trend: 已于 2021年11月22日 [发布](https://github.com/microsoft/qlib/pull/704) |
| ADARNN 模型 | :chart_with_upwards_trend: 已于 2021年11月14日 [发布](https://github.com/microsoft/qlib/pull/689) |
| TCN 模型 | :chart_with_upwards_trend: 已于 2021年11月4日 [发布](https://github.com/microsoft/qlib/pull/668) |
| 嵌套决策框架 | :hammer: 已于 2021年10月1日 [发布](https://github.com/microsoft/qlib/pull/438)。[示例](https://github.com/microsoft/qlib/blob/main/examples/nested_decision_execution/workflow.py) 和 [文档](https://qlib.readthedocs.io/en/latest/component/highfreq.html) |
| 时序路由适配器 (TRA) | :chart_with_upwards_trend: 已于 2021年7月30日 [发布](https://github.com/microsoft/qlib/pull/531) |
| Transformer & Localformer | :chart_with_upwards_trend: 已于 2021年7月22日 [发布](https://github.com/microsoft/qlib/pull/508) |
| 发布 Qlib v0.7.0 | :octocat: 已于 2021年7月12日 [发布](https://github.com/microsoft/qlib/releases/tag/v0.7.0) |
| TCTS 模型 | :chart_with_upwards_trend: 已于 2021年7月1日 [发布](https://github.com/microsoft/qlib/pull/491) |
| 在线服务与自动模型滚动 | :hammer:  已于 2021年5月17日 [发布](https://github.com/microsoft/qlib/pull/290) | 
| DoubleEnsemble 模型 | :chart_with_upwards_trend: 已于 2021年3月2日 [发布](https://github.com/microsoft/qlib/pull/286) | 
| 高频数据处理示例 | :hammer: 已于 2021年2月5日 [发布](https://github.com/microsoft/qlib/pull/257)  |
| 高频交易示例 | :chart_with_upwards_trend: [部分代码已发布](https://github.com/microsoft/qlib/pull/227) 于 2021年1月28日  | 
| 高频数据(1分钟) | :rice: 已于 2021年1月27日 [发布](https://github.com/microsoft/qlib/pull/221) |
| Tabnet 模型 | :chart_with_upwards_trend: 已于 2021年1月22日 [发布](https://github.com/microsoft/qlib/pull/205) |

2021年之前发布的功能未在此列出。

<p align="center">
  <img src="docs/_static/img/logo/1.png" />
</p>

Qlib 是一个开源的、面向AI的量化投资平台，旨在利用AI技术实现量化投资的潜力、赋能研究、并从探索想法到生产部署创造价值。Qlib 支持多种机器学习建模范式，包括监督学习、市场动态建模和强化学习。

越来越多的不同范式下的SOTA量化研究工作和论文正在 Qlib 中发布，以协作解决量化投资中的关键挑战。例如：1) 使用监督学习从丰富且异构的金融数据中挖掘市场复杂的非线性模式；2) 使用自适应概念漂移技术对金融市场的动态特性进行建模；3) 使用强化学习对连续投资决策进行建模，并帮助投资者优化其交易策略。

它包含了数据处理、模型训练、回测的完整机器学习流水线；并涵盖了量化投资的整个链条：阿尔法信号寻求、风险建模、资产组合优化和订单执行。
更多细节，请参考我们的论文 ["Qlib: 一个面向AI的量化投资平台"](https://arxiv.org/abs/2009.11189)。


<table>
  <tbody>
    <tr>
      <th>框架、教程、数据与 DevOps</th>
      <th>量化研究中的主要挑战与解决方案</th>
    </tr>
    <tr>
      <td>
        <li><a href="#开发计划"><strong>开发计划</strong></a></li>
        <li><a href="#qlib框架">Qlib 框架</a></li>
        <li><a href="#快速开始">快速开始</a></li>
          <ul dir="auto">
            <li type="circle"><a href="#安装">安装</a> </li>
            <li type="circle"><a href="#数据准备">数据准备</a></li>
            <li type="circle"><a href="#自动化量化研究工作流">自动化量化研究工作流</a></li>
            <li type="circle"><a href="#通过代码构建自定义量化研究工作流">通过代码构建自定义量化研究工作流</a></li></ul>
        <li><a href="#量化数据集动物园"><strong>量化数据集动物园</strong></a></li>
        <li><a href="#学习框架">学习框架</a></li>
        <li><a href="#更多关于qlib">更多关于 Qlib</a></li>
        <li><a href="#离线模式与在线模式">离线模式与在线模式</a>
        <ul>
          <li type="circle"><a href="#qlib数据服务器性能">Qlib 数据服务器性能</a></li></ul>
        <li><a href="#相关报告">相关报告</a></li>
        <li><a href="#联系我们">联系我们</a></li>
        <li><a href="#贡献指南">贡献指南</a></li>
      </td>
      <td valign="baseline">
        <li><a href="#量化研究中的主要挑战与解决方案">量化研究中的主要挑战与解决方案</a>
          <ul>
            <li type="circle"><a href="#预测寻找有价值的信号模式">预测：寻找有价值的信号/模式</a>
              <ul>
                <li type="disc"><a href="#量化模型论文动物园"><strong>量化模型（论文）动物园</strong></a>
                  <ul>
                    <li type="circle"><a href="#运行单个模型">运行单个模型</a></li>
                    <li type="circle"><a href="#运行多个模型">运行多个模型</a></li>
                  </ul>
                </li>
              </ul>
            </li>
          <li type="circle"><a href="#适应市场动态">适应市场动态</a></li>
          <li type="circle"><a href="#强化学习对连续决策进行建模">强化学习：对连续决策进行建模</a></li>
          </ul>
        </li>
      </td>
    </tr>
  </tbody>
</table>

# 开发计划
正在开发中的新功能（按预计发布时间排序）。
您对这些功能的反馈非常重要。
<!-- | 功能                        | 状态      | -->
<!-- | --                      | ------    | -->

# Qlib 框架

<div style="align: center">
<img src="docs/_static/img/framework-abstract.jpg" />
</div>

上图展示了 Qlib 的高层框架（用户可以在深入研究细节时找到 Qlib 设计的[详细框架](https://qlib.readthedocs.io/en/latest/introduction/introduction.html#framework)）。
各组件被设计为松耦合的模块，每个组件都可以独立使用。

Qlib 为量化研究提供了强大的基础设施。[数据](https://qlib.readthedocs.io/en/latest/component/data.html)始终是重要的一环。
一个强大的学习框架被设计用于支持多样的学习范式（例如 [强化学习](https://qlib.readthedocs.io/en/latest/component/rl.html)、[监督学习](https://qlib.readthedocs.io/en/latest/component/workflow.html#model-section)）和不同级别的模式（例如 [市场动态建模](https://qlib.readthedocs.io/en/latest/component/meta.html)）。
通过对市场建模，[交易策略](https://qlib.readthedocs.io/en/latest/component/strategy.html)将生成将被执行的交易决策。不同级别或粒度的多个交易策略和执行器可以[被嵌套在一起进行优化和运行](https://qlib.readthedocs.io/en/latest/component/highfreq.html)。
最后，将提供全面的[分析](https://qlib.readthedocs.io/en/latest/component/report.html)，并且模型可以以低成本进行[在线服务](https://qlib.readthedocs.io/en/latest/component/online.html)。


# 快速开始

本快速入门指南旨在演示：
1. 使用 _Qlib_ 构建一个完整的量化研究工作流并尝试您的想法是非常容易的。
2. 尽管使用*公开数据*和*简单模型*，机器学习技术在实践量化投资中**效果非常好**。

这里有一个快速 **[演示](https://terminalizer.com/view/3f24561a4470)**，展示了如何安装 ``Qlib``，并使用 ``qrun`` 运行 LightGBM。**但是**，请确保您已按照[说明](#数据准备)准备好了数据。


## 安装

下表展示了 `Qlib` 支持的 Python 版本：
|               | 使用 pip 安装      | 从源代码安装  |        绘图        |
| ------------- |:---------------------:|:--------------------:|:------------------:|
| Python 3.8    | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.9    | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.10   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.11   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |
| Python 3.12   | :heavy_check_mark:    | :heavy_check_mark:   | :heavy_check_mark: |

**注意**：
1. 建议使用 **Conda** 管理您的 Python 环境。在某些情况下，在 `conda` 环境之外使用 Python 可能导致缺少头文件，从而导致某些包安装失败。
2. 请注意，在 Python 3.6 中安装 cython 会导致从源代码安装 ``Qlib`` 时出现一些错误。如果用户在其机器上使用 Python 3.6，建议将 Python *升级*到 3.8 或更高版本，或使用 `conda` 的 Python 从源代码安装 ``Qlib``。

### 使用 pip 安装
用户可以根据以下命令轻松通过 pip 安装 ``Qlib``。

```bash
  pip install pyqlib
```

**注意**：pip 将安装最新稳定的 qlib 版本。然而，qlib 的主分支正在积极开发中。如果您想测试主分支中的最新脚本或功能，请使用以下方法安装 qlib。

### 从源代码安装
用户也可以根据以下步骤从源代码安装最新的开发版本 ``Qlib``：

* 在从源代码安装 ``Qlib`` 之前，用户需要安装一些依赖项：

  ```bash
  pip install numpy
  pip install --upgrade cython
  ```

* 克隆仓库并安装 ``Qlib`` 如下所示。
    ```bash
    git clone https://github.com/microsoft/qlib.git && cd qlib
    pip install .  # 对于开发，建议使用 `pip install -e .[dev]`。详情请查看 docs/developer/code_standard_and_dev_guide.rst
    ```

**提示**：如果您无法在您的环境中安装 `Qlib` 或运行示例，将您的步骤与 [CI 工作流](.github/workflows/test_qlib_from_source.yml) 进行比较可能有助于您发现问题。

**Mac 用户提示**：如果您使用配备 M1 芯片的 Mac，可能会在构建 LightGBM 的 wheel 时遇到问题，这是由于缺少 OpenMP 的依赖项。要解决此问题，请先使用 ``brew install libomp`` 安装 openmp，然后运行 ``pip install .`` 以成功构建。

## 数据准备
❗ 由于数据安全政策更加严格，官方数据集暂时停用。您可以尝试社区贡献的[此数据源](https://github.com/chenditc/investment_data/releases)。
以下是下载最新数据的示例。
```bash
wget https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz
mkdir -p ~/.qlib/qlib_data/cn_data
tar -zxvf qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1
rm -f qlib_bin.tar.gz
```

以下官方数据集将在短期内恢复。

----

通过运行以下代码加载和准备数据：

### 通过模块获取
  ```bash
  # 获取日频数据
  python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

  # 获取分钟频数据
  python -m qlib.cli.data qlib_data --target_dir ~/.qlib/qlib_data/cn_data_1min --region cn --interval 1min

  ```

### 从源代码获取

  ```bash
  # 获取日频数据
  python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

  # 获取分钟频数据
  python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/cn_data_1min --region cn --interval 1min

  ```

该数据集由 [爬虫脚本](scripts/data_collector/) 收集的公开数据创建，这些脚本已在同一仓库中发布。
用户可以使用它创建相同的数据集。[数据集描述](https://github.com/microsoft/qlib/tree/main/scripts/data_collector#description-of-dataset)

*请**注意**，数据收集自 [Yahoo Finance](https://finance.yahoo.com/lookup)，数据可能并不完美。
如果用户拥有高质量的数据集，我们建议用户准备自己的数据。更多信息，用户可以参阅[相关文档](https://qlib.readthedocs.io/en/latest/component/data.html#converting-csv-format-into-qlib-format)*。

### 日频数据的自动更新（来自雅虎财经）
  > 如果用户只想在历史数据上尝试其模型和策略，此步骤是*可选的*。
  >
  > 建议用户先手动更新一次数据（--trading_date 2021-05-25），然后将其设置为自动更新。
  >
  > **注意**：用户无法基于 Qlib 提供的离线数据增量更新数据（某些字段已被移除以减少数据大小）。用户应使用 [雅虎收集器](https://github.com/microsoft/qlib/tree/main/scripts/data_collector/yahoo#automatic-update-of-daily-frequency-datafrom-yahoo-finance) 从头开始下载雅虎数据，然后进行增量更新。
  >
  > 更多信息，请参考：[雅虎收集器](https://github.com/microsoft/qlib/tree/main/scripts/data_collector/yahoo#automatic-update-of-daily-frequency-datafrom-yahoo-finance)

  * 每个交易日自动更新数据到 "qlib" 目录 (Linux)
      * 使用 *crontab*：`crontab -e`
      * 设置定时任务：

        ```
        * * * * 1-5 python <脚本路径> update_data_to_bin --qlib_data_1d_dir <用户数据目录>
        ```
        * **脚本路径**：*scripts/data_collector/yahoo/collector.py*

  * 手动更新数据
      ```
      python scripts/data_collector/yahoo/collector.py update_data_to_bin --qlib_data_1d_dir <用户数据目录> --trading_date <开始日期> --end_date <结束日期>
      ```
      * *trading_date*：交易日开始日期
      * *end_date*：交易日结束日期（不包含）

### 检查数据健康状况
  * 我们提供了一个脚本来检查数据健康状况，您可以运行以下命令来检查数据是否健康。
    ```
    python scripts/check_data_health.py check_data --qlib_dir ~/.qlib/qlib_data/cn_data
    ```
  * 当然，您也可以添加一些参数来调整测试结果，例如这样。
    ```
    python scripts/check_data_health.py check_data --qlib_dir ~/.qlib/qlib_data/cn_data --missing_data_num 30055 --large_step_threshold_volume 94485 --large_step_threshold_price 20
    ```
  * 如果您想了解更多关于 `check_data_health` 的信息，请参阅[文档](https://qlib.readthedocs.io/en/latest/component/data.html#checking-the-health-of-the-data)。

<!--
- 运行初始化代码并获取股票数据：

  ```python
  import qlib
  from qlib.data import D
  from qlib.constant import REG_CN

  # 初始化
  mount_path = "~/.qlib/qlib_data/cn_data"  # target_dir
  qlib.init(mount_path=mount_path, region=REG_CN)

  # 通过 Qlib 获取股票数据
  # 加载给定时间范围和频率的交易日历
  print(D.calendar(start_time='2010-01-01', end_time='2017-12-31', freq='day')[:2])

  # 将给定的市场名称解析为股票池配置
  instruments = D.instruments('csi500')
  print(D.list_instruments(instruments=instruments, start_time='2010-01-01', end_time='2017-12-31', as_list=True)[:6])

  # 加载给定时间范围内特定标的的特征
  instruments = ['SH600000']
  fields = ['$close', '$volume', 'Ref($close, 1)', 'Mean($close, 3)', '$high-$low']
  print(D.features(instruments, fields, start_time='2010-01-01', end_time='2017-12-31', freq='day').head())
  ```
 -->

## Docker 镜像
1. 从 Docker Hub 仓库拉取镜像
    ```bash
    docker pull pyqlib/qlib_image_stable:stable
    ```
2. 启动新的 Docker 容器
    ```bash
    docker run -it --name <容器名称> -v <挂载的本地目录>:/app pyqlib/qlib_image_stable:stable
    ```
3. 此时您已进入 Docker 环境，可以运行 qlib 脚本。示例如下：
    ```bash
    >>> python scripts/get_data.py qlib_data --name qlib_data_simple --target_dir ~/.qlib/qlib_data/cn_data --interval 1d --region cn
    >>> python qlib/cli/run.py examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
4. 退出容器
    ```bash
    >>> exit
    ```
5. 重启容器
    ```bash
    docker start -i -a <容器名称>
    ```
6. 停止容器
    ```bash
    docker stop <容器名称>
    ```
7. 删除容器
    ```bash
    docker rm <容器名称>
    ```
8. 如果您想了解更多信息，请参阅[文档](https://qlib.readthedocs.io/en/latest/developer/how_to_build_image.html)。

## 自动化量化研究工作流
Qlib 提供了一个名为 `qrun` 的工具来自动运行整个工作流（包括构建数据集、训练模型、回测和评估）。您可以按照以下步骤启动自动化量化研究工作流，并获得图形化的报告分析：

1. 量化研究工作流：使用 lightgbm 工作流配置 ([workflow_config_lightgbm_Alpha158.yaml](examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml) 运行 `qrun`，如下所示。
    ```bash
      cd examples  # 避免在包含 `qlib` 的目录下运行程序
      qrun benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
    如果用户想在调试模式下使用 `qrun`，请使用以下命令：
    ```bash
    python -m pdb qlib/cli/run.py examples/benchmarks/LightGBM/workflow_config_lightgbm_Alpha158.yaml
    ```
    `qrun` 的结果如下所示，关于结果的更多解释请参考[文档](https://qlib.readthedocs.io/en/latest/component/strategy.html#result)。

    ```bash

    '以下是无成本超额收益的分析结果。'
                           风险指标
    均值               0.000708
    标准差              0.005626
    年化收益率          0.178316
    信息比率            1.996555
    最大回撤            -0.081806
    '以下是考虑成本后超额收益的分析结果。'
                           风险指标
    均值               0.000512
    标准差              0.005626
    年化收益率          0.128982
    信息比率            1.444287
    最大回撤            -0.091078
    ```
    这里是 `qrun` 和 [工作流](https://qlib.readthedocs.io/en/latest/component/workflow.html) 的详细文档。

2. 图形化报告分析：首先，运行 `python -m pip install .[analysis]` 安装所需的依赖项。然后使用 `jupyter notebook` 运行 `examples/workflow_by_code.ipynb` 以获得图形化报告。
    - 预测信号（模型预测）分析
      - 分组累计收益
      ![累计收益](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_cumulative_return.png)
      - 收益分布
      ![多空收益](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_long_short.png)
      - 信息系数 (IC)
      ![信息系数](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_IC.png)
      ![月度 IC](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_monthly_IC.png)
      ![IC](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_NDQ.png)
      - 预测信号（模型预测）的自相关
      ![自相关](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/analysis_model_auto_correlation.png)

    - 资产组合分析
      - 回测收益
      ![报告](https://github.com/microsoft/qlib/blob/main/docs/_static/img/analysis/report.png)
      <!--
      - 分数 IC
      ![分数 IC](docs/_static/img/score_ic.png)
      - 累计收益
      ![累计收益](docs/_static/img/cumulative_return.png)
      - 风险分析
      ![风险分析](docs/_static/img/risk_analysis.png)
      - 排名标签
      ![排名标签](docs/_static/img/rank_label.png)
      -->
   - 上述结果的[说明](https://qlib.readthedocs.io/en/latest/component/report.html)

## 通过代码构建自定义量化研究工作流
自动化工作流可能并不适合所有量化研究人员的研究流程。为了支持灵活的量化研究工作流，Qlib 还提供了模块化接口，允许研究人员通过代码构建自己的工作流。[这里](examples/workflow_by_code.ipynb) 是一个通过代码自定义量化研究工作流的演示。

# 量化研究中的主要挑战与解决方案
量化投资是一个非常独特的场景，存在许多需要解决的关键挑战。
目前，Qlib 为其中几个挑战提供了一些解决方案。

## 预测：寻找有价值的信号/模式
准确预测股票价格趋势是构建盈利投资组合非常重要的一环。
然而，金融市场中存在大量不同格式的数据，这使得构建预测模型具有挑战性。

越来越多的SOTA量化研究工作/论文，专注于构建预测模型以从复杂的金融数据中挖掘有价值的信号/模式，正在 `Qlib` 中发布。

### [量化模型（论文）动物园](examples/benchmarks)

以下是在 `Qlib` 上构建的模型列表。
- [基于 XGBoost 的 GBDT (Tianqi Chen, 等人. KDD 2016)](examples/benchmarks/XGBoost/)
- [基于 LightGBM 的 GBDT (Guolin Ke, 等人. NIPS 2017)](examples/benchmarks/LightGBM/)
- [基于 Catboost 的 GBDT (Liudmila Prokhorenkova, 等人. NIPS 2018)](examples/benchmarks/CatBoost/)
- [基于 pytorch 的 MLP](examples/benchmarks/MLP/)
- [基于 pytorch 的 LSTM (Sepp Hochreiter, 等人. Neural computation 1997)](examples/benchmarks/LSTM/)
- [基于 pytorch 的 GRU (Kyunghyun Cho, 等人. 2014)](examples/benchmarks/GRU/)
- [基于 pytorch 的 ALSTM (Yao Qin, 等人. IJCAI 2017)](examples/benchmarks/ALSTM)
- [基于 pytorch 的 GATs (Petar Velickovic, 等人. 2017)](examples/benchmarks/GATs/)
- [基于 pytorch 的 SFM (Liheng Zhang, 等人. KDD 2017)](examples/benchmarks/SFM/)
- [基于 tensorflow 的 TFT (Bryan Lim, 等人. International Journal of Forecasting 2019)](examples/benchmarks/TFT/)
- [基于 pytorch 的 TabNet (Sercan O. Arik, 等人. AAAI 2019)](examples/benchmarks/TabNet/)
- [基于 LightGBM 的 DoubleEnsemble (Chuheng Zhang, 等人. ICDM 2020)](examples/benchmarks/DoubleEnsemble/)
- [基于 pytorch 的 TCTS (Xueqing Wu, 等人. ICML 2021)](examples/benchmarks/TCTS/)
- [基于 pytorch 的 Transformer (Ashish Vaswani, 等人. NeurIPS 2017)](examples/benchmarks/Transformer/)
- [基于 pytorch 的 Localformer (Juyong Jiang, 等人.)](examples/benchmarks/Localformer/)
- [基于 pytorch 的 TRA (Hengxu, Dong, 等人. KDD 2021)](examples/benchmarks/TRA/)
- [基于 pytorch 的 TCN (Shaojie Bai, 等人. 2018)](examples/benchmarks/TCN/)
- [基于 pytorch 的 ADARNN (YunTao Du, 等人. 2021)](examples/benchmarks/ADARNN/)
- [基于 pytorch 的 ADD (Hongshun Tang, 等人.2020)](examples/benchmarks/ADD/)
- [基于 pytorch 的 IGMTF (Wentao Xu, 等人.2021)](examples/benchmarks/IGMTF/)
- [基于 pytorch 的 HIST (Wentao Xu, 等人.2021)](examples/benchmarks/HIST/)
- [基于 pytorch 的 KRNN](examples/benchmarks/KRNN/)
- [基于 pytorch 的 Sandwich](examples/benchmarks/Sandwich/)

您提交新的量化模型的 Pull Request 将非常受欢迎。

各模型在 `Alpha158` 和 `Alpha360` 数据集上的性能可以在[这里](examples/benchmarks/README.md)找到。

### 运行单个模型
以上列出的所有模型都可以用 ``Qlib`` 运行。用户可以通过 [benchmarks](examples/benchmarks) 文件夹找到我们提供的配置文件以及有关模型的一些细节。更多信息可以在上面列出的模型文件中找到。

`Qlib` 提供了三种不同的方式来运行单个模型，用户可以选择最适合自己情况的方式：
- 用户可以使用上面提到的工具 `qrun`，基于配置文件运行模型的工作流。
- 用户可以基于 `examples` 文件夹中列出的[脚本](examples/workflow_by_code.py) 创建一个 `workflow_by_code` Python 脚本。
- 用户可以使用 `examples` 文件夹中列出的脚本 [`run_all_model.py`](examples/run_all_model.py) 来运行模型。以下是一个具体的 Shell 命令示例：`python run_all_model.py run --models=lightgbm`，其中 `--models` 参数可以接受上面列出的任意数量的模型（可用模型可以在 [benchmarks](examples/benchmarks/) 中找到）。更多用例，请参考该文件的[文档字符串](examples/run_all_model.py)。
    - **注意**：每个基线都有不同的环境依赖，请确保您的 Python 版本符合要求（例如，由于 `tensorflow==1.15.0` 的限制，TFT 仅支持 Python 3.6~3.7）

### 运行多个模型
`Qlib` 还提供了一个脚本 [`run_all_model.py`](examples/run_all_model.py)，该脚本可以运行多个模型进行多次迭代。（**注意**：该脚本目前仅支持 *Linux*。未来将支持其他操作系统。此外，它也不支持并行运行同一模型多次，这也将在未来的开发中修复。）

该脚本将为每个模型创建一个独立的虚拟环境，并在训练后删除这些环境。因此，只会生成并存储诸如 `IC` 和 `backtest` 结果等实验成果。

以下是运行所有模型 10 次迭代的示例：
```python
python run_all_model.py run 10
```

它还提供了同时运行特定模型的 API。更多用例，请参考该文件的[文档字符串](examples/run_all_model.py)。

### 破坏性变更
在 `pandas` 中，`group_key` 是 `groupby` 方法的参数之一。从 `pandas` 的 1.5 版本到 2.0 版本，`group_key` 的默认值已从 `无默认值` 更改为 `True`，这将导致 qlib 在操作期间报告错误。因此我们设置 `group_key=False`，但这并不能保证某些程序能正确运行，包括：
* qlib\examples\rl_order_execution\scripts\gen_training_orders.py
* qlib\examples\benchmarks\TRA\src\dataset.MTSDatasetH.py
* qlib\examples\benchmarks\TFT\tft.py


## [适应市场动态](examples/benchmarks_dynamic)

由于金融市场环境的非平稳性，数据分布在不同时期可能会发生变化，这使得基于训练数据构建的模型在未来测试数据上的性能会下降。
因此，使预测模型/策略适应市场动态对模型/策略的性能至关重要。

以下是在 `Qlib` 上构建的解决方案列表。
- [滚动重训练](examples/benchmarks_dynamic/baseline/)
- [基于 pytorch 的 DDG-DA (Wendi, 等人. AAAI 2022)](examples/benchmarks_dynamic/DDG-DA/)

## 强化学习：对连续决策进行建模
Qlib 现在支持强化学习，这是一个旨在对连续投资决策进行建模的功能。此功能通过从与环境的交互中学习以最大化某种累积奖励的概念，帮助投资者优化其交易策略。

以下是根据场景分类的在 `Qlib` 上构建的解决方案列表。

### [订单执行强化学习](examples/rl_order_execution)
[这里](https://qlib.readthedocs.io/en/latest/component/rl/overall.html#order-execution) 是关于此场景的介绍。以下所有方法在此[对比](examples/rl_order_execution)。
- [TWAP](examples/rl_order_execution/exp_configs/backtest_twap.yml)
- [PPO: "An End-to-End Optimal Trade Execution Framework based on Proximal Policy Optimization", IJCAL 2020](examples/rl_order_execution/exp_configs/backtest_ppo.yml)
- [OPDS: "Universal Trading for Order Execution with Oracle Policy Distillation", AAAI 2021](examples/rl_order_execution/exp_configs/backtest_opds.yml)

# 量化数据集动物园
数据集在量化中扮演着非常重要的角色。以下是在 `Qlib` 上构建的数据集列表：

| 数据集                                    | 美国市场 | 中国市场 |
| --                                         | --        | --           |
| [Alpha360](./qlib/contrib/data/handler.py) |  √        |  √           |
| [Alpha158](./qlib/contrib/data/handler.py) |  √        |  √           |

[这里](https://qlib.readthedocs.io/en/latest/advanced/alpha.html) 是使用 `Qlib` 构建数据集的教程。
您提交构建新量化数据集的 Pull Request 将非常受欢迎。

# 学习框架
Qlib 具有高度可定制性，其许多组件是可学习的。
可学习的组件是 `预测模型` 和 `交易智能体` 的实例。它们基于 `学习框架` 层进行学习，然后应用于 `工作流` 层中的多个场景。
学习框架也利用了 `工作流` 层（例如共享 `信息提取器`，基于 `执行环境` 创建环境）。

根据学习范式，它们可以分为强化学习和监督学习。
- 对于监督学习，详细文档可以在[这里](https://qlib.readthedocs.io/en/latest/component/model.html)找到。
- 对于强化学习，详细文档可以在[这里](https://qlib.readthedocs.io/en/latest/component/rl.html)找到。Qlib 的 RL 学习框架利用 `工作流` 层中的 `执行环境` 来创建环境。值得注意的是，`嵌套执行器` 也受支持。这使得用户能够共同优化不同级别的策略/模型/智能体（例如，为特定的投资组合管理策略优化订单执行策略）。


# 更多关于 Qlib
如果您想快速了解 Qlib 最常用的组件，可以尝试 [这里](examples/tutorial/) 的 notebook。

详细文档组织在 [docs](docs/) 中。
需要 [Sphinx](http://www.sphinx-doc.org) 和 readthedocs 主题来构建 HTML 格式的文档。
```bash
cd docs/
conda install sphinx sphinx_rtd_theme -y
# 或者，您可以使用 pip 安装它们
# pip install sphinx sphinx_rtd_theme
make html
```
您也可以直接在线查看[最新文档](http://qlib.readthedocs.io/)。

Qlib 正在积极持续开发中。我们的计划在路线图中，该路线图作为一个 [github 项目](https://github.com/microsoft/qlib/projects/1) 进行管理。

# 离线模式与在线模式
Qlib 的数据服务器可以部署为 `离线` 模式或 `在线` 模式。默认模式是离线模式。

在 `离线` 模式下，数据将部署在本地。

在 `在线` 模式下，数据将部署为共享数据服务。数据及其缓存将由所有客户端共享。由于缓存命中率更高，数据检索性能有望得到提升。同时也会消耗更少的磁盘空间。在线模式的文档可以在 [Qlib-Server](https://qlib-server.readthedocs.io/) 中找到。在线模式可以使用 [基于 Azure CLI 的脚本](https://qlib-server.readthedocs.io/en/latest/build.html#one-click-deployment-in-azure) 自动部署。在线数据服务器的源代码可以在 [Qlib-Server 仓库](https://github.com/microsoft/qlib-server) 中找到。

## Qlib 数据服务器性能
数据处理性能对于像 AI 技术这样的数据驱动方法非常重要。作为一个面向 AI 的平台，Qlib 为数据存储和数据处理提供了一个解决方案。为了展示 Qlib 数据服务器的性能，我们将其与其他几种数据存储解决方案进行了比较。

我们通过完成相同的任务来评估几种存储解决方案的性能，
该任务从一个股票市场（2007年至2020年，每天800只股票）的基本日频 OHLCV 数据创建一个数据集（14个特征/因子）。该任务涉及数据查询和处理。

|                         | HDF5      | MySQL     | MongoDB   | InfluxDB  | Qlib -E -D  | Qlib +E -D   | Qlib +E +D  |
| --                      | ------    | ------    | --------  | --------- | ----------- | ------------ | ----------- |
| 总计 (1CPU) (秒)        | 184.4±3.7 | 365.3±7.5 | 253.6±6.7 | 368.2±3.6 | 147.0±8.8   | 47.6±1.0     | **7.4±0.3** |
| 总计 (64CPU) (秒)       |           |           |           |           | 8.8±0.6     | **4.2±0.2**  |             |
* `+(-)E` 表示 (不) 使用 `表达式缓存`
* `+(-)D` 表示 (不) 使用 `数据集缓存`

大多数通用数据库加载数据耗时太长。在深入了解底层实现后，我们发现通用数据库解决方案中的数据经过了太多层接口和不必要的格式转换。
这种开销极大地减慢了数据加载过程。
Qlib 数据以紧凑的格式存储，这种格式可以高效地组合成数组以进行科学计算。

# 相关报告
- [Qlib 指南：微软的 AI 投资平台](https://analyticsindiamag.com/qlib/)
- [微软也搞 AI 量化平台？还是开源的！](https://mp.weixin.qq.com/s/47bP5YwxfTp2uTHjUBzJQQ)
- [微矿 Qlib：业内首个 AI 量化投资开源平台](https://mp.weixin.qq.com/s/vsJv7lsgjEi-ALYUz4CvtQ)

# 联系我们
- 如果您有任何问题，请在此处创建 [issue](https://github.com/microsoft/qlib/issues/new/choose) 或在 [gitter](https://gitter.im/Microsoft/qlib) 中发送消息。
- 如果您想为 `Qlib` 做出贡献，请 [创建 pull requests](https://github.com/microsoft/qlib/compare)。
- 对于其他原因，欢迎通过邮件联系我们 ([qlib@microsoft.com](mailto:qlib@microsoft.com))。
  - 我们正在招募新成员（包括正式员工和实习生），欢迎投递您的简历！

加入 IM 讨论组：
|[Gitter](https://gitter.im/Microsoft/qlib)|
|----|
|![image](https://github.com/microsoft/qlib/blob/main/docs/_static/img/qrcode/gitter_qr.png)|

# 贡献指南
我们感谢所有的贡献，并感谢所有的贡献者！
<a href="https://github.com/microsoft/qlib/graphs/contributors"><img src="https://contrib.rocks/image?repo=microsoft/qlib" /></a>

在我们于 2020年9月 在 Github 上将 Qlib 作为开源项目发布之前，Qlib 是我们团队的一个内部项目。遗憾的是，内部提交历史没有保留。我们团队的许多成员也为 Qlib 做出了巨大贡献，包括 Ruihua Wang, Yinda Zhang, Haisu Yu, Shuyu Wang, Bochen Pang, 以及 [Dong Zhou](https://github.com/evanzd/evanzd)。特别感谢 [Dong Zhou](https://github.com/evanzd/evanzd)，因为他贡献了 Qlib 的初始版本。

## 指导原则

本项目欢迎贡献和建议。
**以下是一些[代码标准和开发指南](docs/developer/code_standard_and_dev_guide.rst)，用于提交 pull request。**

做出贡献并不是一件难事。解决一个问题（可能只是回答 [issues 列表](https://github.com/microsoft/qlib/issues) 或 [gitter](https://gitter.im/Microsoft/qlib) 中提出的问题）、修复/报告一个错误、改进文档，甚至修正一个拼写错误，都是对 Qlib 的重要贡献。

例如，如果您想为 Qlib 的文档/代码做出贡献，可以按照下图所示的步骤进行。
<p align="center">
  <img src="https://github.com/demon143/qlib/blob/main/docs/_static/img/change%20doc.gif" />
</p>

如果您不知道如何开始贡献，可以参考以下示例。
| 类型 | 示例 |
| -- | -- |
| 解决问题 | [回答问题](https://github.com/microsoft/qlib/issues/749)；[报告](https://github.com/microsoft/qlib/issues/765) 或 [修复](https://github.com/microsoft/qlib/pull/792) 一个错误 |
| 文档 | [提高文档质量](https://github.com/microsoft/qlib/pull/797/files) ;  [修正拼写错误](https://github.com/microsoft/qlib/pull/774) |
| 功能 |  实现一个[请求的功能](https://github.com/microsoft/qlib/projects)，例如[这个](https://github.com/microsoft/qlib/pull/754)；[重构接口](https://github.com/microsoft/qlib/pull/539/files) |
| 数据集 | [添加数据集](https://github.com/microsoft/qlib/pull/733) |
| 模型 |  [实现新模型](https://github.com/microsoft/qlib/pull/689), [贡献模型的说明](https://github.com/microsoft/qlib/tree/main/examples/benchmarks#contributing) |

[Good first issues](https://github.com/microsoft/qlib/labels/good%20first%20issue) 已被标记，表示它们易于开始您的贡献。

您可以通过 `rg 'TODO|FIXME' qlib` 在 Qlib 中找到一些不完美的实现。

如果您想成为 Qlib 的维护者之一以贡献更多（例如帮助合并 PR，处理 issues），请通过邮件 ([qlib@microsoft.com](mailto:qlib@microsoft.com)) 联系我们。我们很乐意帮助提升您的权限。

## 许可证
大多数贡献要求您同意
贡献者许可协议 (CLA)，声明您有权授予我们使用您的贡献的权利。有关详细信息，请访问 https://cla.opensource.microsoft.com。

当您提交 pull request 时，CLA 机器人将自动确定您是否需要提供 CLA 并相应地装饰 PR（例如，状态检查、评论）。只需按照机器人提供的说明操作即可。您只需在所有使用我们 CLA 的仓库中执行此操作一次。

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
有关更多信息，请参阅 [行为准则 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或
通过 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提出任何其他问题或评论。