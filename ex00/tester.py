from load_csv import load
# import pandas as pd


def main():
    load("/home/ylamkhan/Downloads/life_expectancy_years.csv")
    # print("================== HEADER DATA =======================")
    # print(df.head())
    # print("===================== END DATA =======================")
    # print(df.tail())
    # print("===================== filter my contry ===============")
    # print(df[df['country'] == 'Morocco'])
    # print("================== SHAPE DATA ========================")
    # print(df.shape)
    # print("==================== colums Name =====================")
    # print(df.columns)
    # print("==================== Summary statistics ==============")
    # print(df.describe())


if __name__ == "__main__":
    main()
