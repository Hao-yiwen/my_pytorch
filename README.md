# my_pytorch

![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.0-EE4C2C?logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.9.2-11557C)

个人 PyTorch 入门学习记录：用一段 NumPy / Python 基础脚本热身，再用一个最小示例创建张量并检查 CUDA。仓库里没有训练、模型、数据集或 Web 应用。

PyCharm 工程名与 Conda 环境名都是 `my_pytorch`，解释器记为 Python 3.11（`.idea/misc.xml`）。

## 仓库里有什么

| 文件 | 作用 |
| --- | --- |
| `main.py` | 创建 `2×3` 整型张量并打印；调用 `torch.cuda.is_available()`，有 CUDA 时提示可用 GPU，否则提示在 CPU 上计算。没有把张量搬到 GPU，也没有其他运算。 |
| `py_base.py` | 学习脚本，自上而下直接执行（没有 `main`）。内容见下表。 |
| `example.txt` | 当前内容为 `hello, world`。`py_base.py` 每次运行都会用同样的文字覆盖它。 |
| `environment.yml` | 从本机 Anaconda 导出的完整环境（`prefix: /opt/anaconda3/envs/my_pytorch`）。 |
| `.idea/` | PyCharm 工程配置，运行脚本不需要它。 |

`py_base.py` 按源码顺序做这些事：

1. 用 NumPy 计算 `dot([1, 2, 3, 4, 5], [0.2, 0.4, 0.6, 0.8, 1.0])`，打印 `11.0`。
2. 演示变量、列表、元组、集合、字典、条件、`for` / `while`、函数 `add`、类 `Dog`。
3. 列表与字典的增删改和遍历。
4. 把 `hello, world` 写入 `example.txt` 再读出打印。
5. 捕获 `10 / 0`，打印 `division by zero`，`finally` 中打印 `this is always executed`。
6. 列表推导：`0` 到 `9` 的平方。
7. 生成器 `countdown(5)`：打印倒计时，**每步 `time.sleep(2)`**，五步大约 10 秒。
8. `math.sqrt(16)`，打印 `4.0`。
9. 用 Matplotlib 画 `Z = sin(sqrt(X² + Y²))` 的 3D 曲面（`cmap='viridis'`），然后 `plt.show()`。

仓库中没有截图。

## 技术栈

版本来自 `environment.yml`（导出日期对应的锁定版本）：

| 组件 | 版本 | 脚本是否直接使用 |
| --- | --- | --- |
| Python | 3.11.9 | 是 |
| PyTorch | 2.4.0（`py3.11_0`） | `main.py` |
| torchvision | 0.19.0（`py311_cpu`） | 否 |
| torchaudio | 2.4.0（`py311_cpu`） | 否 |
| NumPy | 1.26.4 | `py_base.py` |
| Matplotlib | 3.9.2 | `py_base.py` |
| SymPy | 1.13.2 | 否（随 PyTorch 环境装上） |

`torchvision`、`torchaudio`、Pillow、NetworkX 等出现在锁定文件里，当前两个脚本没有 import 它们。

## 目录结构

```text
.
├── .idea/                 # PyCharm 工程
├── environment.yml        # Conda 环境锁定文件
├── example.txt            # py_base.py 写出的示例文本
├── main.py                # PyTorch 张量示例
├── py_base.py             # Python / NumPy / Matplotlib 练习
└── README.md
```

## 环境要求

- 复现作者环境：Anaconda / Miniconda，Python 3.11。
- 只跑现有脚本：Python 3.11 或 3.12，以及 `torch`、`numpy`、`matplotlib`。
- GPU 可选。`main.py` 只检测 CUDA，检测失败时继续在 CPU 上打印张量。
- `py_base.py` 末尾会打开 Matplotlib 窗口；没有图形界面时需要非交互后端（见下文）。

`environment.yml` 含 macOS 专用包（如 `libcxx`）和 Apple Silicon 构建号（如 `hca03da5`），前缀指向 `/opt/anaconda3/envs/my_pytorch`。它对应导出该文件的那台 macOS 机器。在 Linux 上执行 `conda env create -f environment.yml` 会因平台包不匹配而失败。本仓库验证用的 Linux 环境没有安装 Conda，因此**没有执行**这条 Conda 命令。

## 安装与运行

在仓库根目录执行。

### Conda（与 `environment.yml` 同一平台时）

```shell
conda env create -f environment.yml
conda activate my_pytorch
python main.py
python py_base.py
```

### pip（已在 Linux 上验证）

下面这条在本仓库的验证机上跑通：Ubuntu，Python 3.12.3，无 GPU。PyPI 上的 `torch==2.4.0` Linux x86_64 轮子会带上 CUDA 12.1 运行库；本机没有 CUDA，脚本仍按 CPU 路径执行。

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install "torch==2.4.0" "numpy==1.26.4" "matplotlib==3.9.2"
python main.py
```

`main.py` 的实际输出：

```text
张量 x:
tensor([[1, 2, 3],
        [4, 5, 6]])
CUDA is not available. Computations will be on CPU.
```

有图形界面时直接运行练习脚本（窗口会停在 `plt.show()`，关掉后进程结束）：

```shell
python py_base.py
```

无图形界面时使用 Agg 后端。脚本仍会执行到 `plt.show()`，并打印一条 `FigureCanvasAgg is non-interactive, and thus cannot be shown` 警告，然后正常退出。3D 图不会弹窗，也不会另存为文件。

```shell
MPLBACKEND=Agg python py_base.py
```

该次运行的可见结果包括：点积 `11.0`、条件与循环打印、`add(1, 2)` 的结果 `3`、`Dog("Rex", 2)` 的叫声与名字、列表和字典操作、读出的 `hello, world`、除零异常的两行提示、`0` 到 `9` 的平方、倒计时 `5` 到 `1`（约 10 秒）、`math.sqrt(16)` 的 `4.0`。运行会覆盖当前目录下的 `example.txt`。

## 备注

- 两个文件都是教学片段，导入后就会产生打印和文件写入；`py_base.py` 不适合被其他模块 import。
- `countdown` 里的 `time.sleep(2)` 是源码里的固定延时，不是卡死。
- 环境锁定文件里的 `sympy`、`torchvision`、`torchaudio` 没有对应示例代码。
