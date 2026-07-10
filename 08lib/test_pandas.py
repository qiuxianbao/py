import numpy as np
import pandas as pd


def test_dataframe():
    # 设置随机种子，确保每次运行结果一致
    np.random.seed(42)

    # 模拟 10 条人类标注的数据：包含前提句、假设句和真实的二分类标签 (0或1)
    gold_data = {
        "sentence1": [f"黄金前提句_{i}" for i in range(10)],
        "sentence2": [f"黄金假设句_{i}" for i in range(10)],
        "label": np.random.choice([0, 1], size=10),  # 从指定数组中随机选取值
    }
    gold_df = pd.DataFrame(gold_data)
    print(f"🥇 黄金数据（共 {len(gold_df)} 条）预览：")
    print(gold_df.head(3))

    output_path = "pandas_practice_output.csv"
    gold_df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"💾 数据已成功保存至本地: {output_path}")


def _main():
    test_dataframe()


if __name__ == '__main__':
    _main()
