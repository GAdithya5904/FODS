def temperature_variability_analysis(df):
    # Get the mean and standard deviation of temperature for each city
    mean_temp = df.groupby("city")["temperature"].mean()
    std_temp = df.groupby("city")["temperature"].std()

    # Find the city with the highest temperature range
    max_range = df["temperature"].max() - df["temperature"].min()
    city_with_max_range = df[df["temperature"] == max_range]["city"].values[0]

    # Find the city with the lowest standard deviation
    city_with_min_std = std_temp.sort_values().index[0]

    # Print the results
    print("City with the highest temperature range:", city_with_max_range)
    print("City with the lowest standard deviation:", city_with_min_std)
