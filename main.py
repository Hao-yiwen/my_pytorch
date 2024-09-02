import torch

def main():
    # 创建一个简单的张量
    x = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print("张量 x:")
    print(x)

    # 检查 GPU 是否可用
    if torch.cuda.is_available():
        print("CUDA is available. You can use GPU for computations.")
    else:
        print("CUDA is not available. Computations will be on CPU.")

if __name__ == "__main__":
    main()