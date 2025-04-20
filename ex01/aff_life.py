from load_csv import load
import matplotlib.pyplot as plt
import sys
import signal


def on_ctrl_c(signal, frame):
    print("Ctrl+C received! Exiting gracefully...")
    sys.exit(0)


def on_ctrl_z(signal, frame):
    print("Ctrl+Z received! Suspending the program...")
    signal.pause()


def main():
    df = load("/home/ylamkhan/Downloads/life_expectancy_years.csv")
    morocco_data = df[df['country'] == 'Morocco'].iloc[0, 1:].values.astype(
        float)
    # france_data = df[df['country'] == 'France'].iloc[0, 1:].values.astype(
    # float)
    # usa_data = df[df['country'] == 'United States'].iloc[0, 1:].
    # values.astype(
    # float)
    Years = df.columns[1:].astype(int)
    plt.figure(figsize=(15, 8))
    plt.plot(Years, morocco_data, marker=None, label='Morocco')
    # plt.plot(Years, france_data, marker='s', label='France')
    # plt.plot(Years, usa_data, marker='^', label='USA')
    plt.title('Morocco Life Expectancy Projections', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Life Expectancy', fontsize=12)
    plt.xlim(1760, 2120)
    plt.ylim(20, 100)
    signal.signal(signal.SIGINT, on_ctrl_c)
    signal.signal(signal.SIGTSTP, on_ctrl_z)
    plt.show()


if __name__ == "__main__":
    main()
