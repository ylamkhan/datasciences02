import sys
import signal
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def on_ctrl_c(signal, frame):
    print("Ctrl+C received! Exiting gracefully...")
    sys.exit(0)


def on_ctrl_z(signal, frame):
    print("Ctrl+Z received! Suspending the program...")
    signal.pause()


def main():
    income_data = load("/home/ylamkhan/Downloads/income.csv")
    life_data = load("/home/ylamkhan/Downloads/life_expectancy_years.csv")
    income_1900 = income_data["1900"]
    life_1900 = life_data["1900"]
    data = pd.concat([income_1900, life_1900], axis=1, join='inner')
    data.columns = ["income", "life_expectancy"]
    data = data.dropna()
    if data["income"].dtype == object:
        data["income"] = data["income"].replace(
            '[kK]', '', regex=True).astype(float) * 1000
    plt.figure(figsize=(10, 6))
    plt.scatter(data["income"], data["life_expectancy"], alpha=0.7)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.xlim(300, 11000)
    plt.xticks(
        ticks=[1000 * i for i in range(
            1, 12)], labels=[f"{i}k" for i in range(1, 12)])
    signal.signal(signal.SIGINT, on_ctrl_c)
    signal.signal(signal.SIGTSTP, on_ctrl_z)
    plt.show()


if __name__ == "__main__":
    main()
