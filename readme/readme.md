conda create --name qlib_env  python=3.8 -y
conda activate qlib_env
pip install --upgrade pip 

pip install -e . -i https://mirrors.aliyun.com/pypi/simple/ 


### 1. 准备工作 (前置条件)
由于 `qlib` 包含需要编译的 C/C++ 扩展（Cython），在 macOS 上您必须确保已安装开发工具：
```bash
xcode-select --install
```
*如果终端提示已安装，则忽略此步。*

### 2. 创建并激活环境
推荐使用 Python 3.8 或 3.10（兼容性较好），避免使用过新的 Python 3.12+（部分科学计算库可能尚未完全支持）。

```bash
# 创建名为 qlib_env 的环境，指定 python 版本
conda create -n qlib_env python=3.10 -y

# 激活环境
conda activate qlib_env
```

### 3. 安装项目
在项目根目录（`/Users/yangcailu/chengtay_code/qlib`）下执行以下命令。`pip` 会自动读取 `pyproject.toml` 中的依赖并进行安装。

#### 方案 A：标准安装（作为库使用）
如果您只是想运行 Qlib 的功能，不打算修改源码：
```bash
pip install .
```

#### 方案 B：开发模式安装（推荐 ⭐）
如果您打算阅读源码、调试或修改代码，使用开发模式（Editable Mode），这样您对代码的修改会立即生效，无需重装：
```bash
pip install -e .
```

### 4. 安装可选依赖 (Optional Dependencies)
在 `pyproject.toml` 的 `[project.optional-dependencies]` 部分定义了额外的功能模块。您可以根据需要安装：

- **安装强化学习支持 (RL)** (包含 PyTorch 等):
  ```bash
  pip install -e ".[rl]"
  ```
  *注意：在 Mac 上安装 PyTorch 可能需要较长时间下载。*

- **安装开发工具** (包含 pytest, black 等):
  ```bash
  pip install -e ".[dev]"
  ```

- **安装所有常用依赖** (组合写法):
  ```bash
  pip install -e ".[rl,dev,analysis]"
  ```

### 5. 验证安装
安装完成后，运行以下命令检查是否成功：

```bash
# 检查 qlib 版本
python -c "import qlib; print(qlib.__version__)"

# 检查 qrun 命令是否可用
qrun --help
```

### 常见问题提示
- **构建时 Numpy 版本**: `pyproject.toml` 第 2 行指定了构建时需要 `numpy>=1.24.0`。`pip` 会在一个隔离环境中自动处理这个构建依赖，通常不需要您手动干预。
- **Mac M1/M2/M3**: 如果您使用 Apple Silicon 芯片，`lightgbm` 有时会报错 `libomp` 缺失。如果遇到，请运行 `brew install libomp`。