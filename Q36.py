def stock_price_variability_analysis(df):
    # Calculate the daily stock price change
    df["daily_price_change"] = df["Close"] - df["Open"]

    # Calculate the mean and standard deviation of the daily stock price change
    mean = df["daily_price_change"].mean()
    std = df["daily_price_change"].std()

    # Print the mean and standard deviation
    print("Mean:", mean)
    print("Standard deviation:", std)

    # Plot the distribution of the daily stock price change
    plt.hist(df["daily_price_change"])
    plt.show()
