import sys
import signal
import matplotlib.pyplot as plt
from load_csv import load


def on_ctrl_c(signal, frame):
    print("Ctrl+C received! Exiting gracefully...")
    sys.exit(0)


def on_ctrl_z(signal, frame):
    print("Ctrl+Z received! Suspending the program...")
    signal.pause()


def convert_to_float(value):
    try:
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('k'):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    except Exception:
        print("Error")
        return None  # or np.nan if you prefer


def main():
    df = load("/home/ylamkhan/Downloads/population_total.csv")
    # print("======================== HEADER DATA =========================")
    # print(df.head())
    # print("======================== END DATA ==========================")
    # print(df.tail)
    # print("======================== DATA SHAPE ===========================")
    # print(df.shape)
    # print("===================== DATA COLUMNS ========================")
    # print(df.columns)
    morocco_data = df[df['country'] == 'Morocco'].iloc[0, 1:].apply(
        convert_to_float).values.astype(float)
    print(morocco_data)
    france_data = df[df['country'] == 'France'].iloc[0, 1:].apply(
        convert_to_float).values.astype(float)
    years = df.columns[1:].astype(int)
    plt.figure(figsize=(15, 8))
    plt.plot(years, morocco_data, marker=None, label='Morocco')
    plt.plot(years, france_data, marker=None, label='France')
    plt.title('Population Projections', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Population', fontsize=12)
    plt.xticks(range(1760, 2050, 40))
    plt.xlim(1760, 2181)
    plt.yticks(
        range(0, 80_000_001, 20_000_000), ['0M', '20M', '40M', '60M', '80M'])
    plt.ylim(0, 80_000_000)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    signal.signal(signal.SIGINT, on_ctrl_c)
    signal.signal(signal.SIGTSTP, on_ctrl_z)
    plt.show()


if __name__ == "__main__":
    main()
