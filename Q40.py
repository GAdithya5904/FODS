def top_5_soccer_players(df):
    # Sort by number of goals scored
    df = df.sort_values(by=["goals_scored"], ascending=False)

    # Get the top 5 players
    top_5_players = df[0:5]

    # Print the top 5 players
    print(top_5_players)



    # Study the correlation between study time and exam scores
    correlation_study(df)

    # Analyze the temperature variability for different cities
    temperature_variability_analysis(df)

    # Print the top 5 soccer players with the highest number of goals scored and salaries
    top_5_soccer_players(df)
