import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = ''
    while city not in CITY_DATA:  
        city = input("Please select a city (chicago, new york city, washington): ").lower()

    month = input("Which month would you like to filter by? (all, january, february, ... , june): ").lower()

    day = input("Which day would you like to filter by? (all, monday, tuesday, ... sunday): ").lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])  

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        df = df[df['Start Time'].dt.month_name().str.lower() == month]

    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['Start Time'].dt.month.mode()[0]
    print(f'Most common month: {most_common_month}')

    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f'Most common day: {most_common_day}')

    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'Most common hour: {most_common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    print(f'Most common start station: {most_common_start_station}')

    most_common_end_station = df['End Station'].mode()[0]
    print(f'Most common end station: {most_common_end_station}')

    most_common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f'Most common trip: {most_common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time: {total_travel_time} seconds')

    mean_travel_time = df['Trip Duration'].mean()
    print(f'Average travel time: {mean_travel_time} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(f'User types:\n{user_types}')

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f'Gender counts:\n{gender_counts}')

        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print(f'Earliest year of birth: {earliest_year}')
        print(f'Most recent year of birth: {most_recent_year}')
        print(f'Most common year of birth: {most_common_year}')
    else:
        print("Gender and birth year information not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays 5 rows of raw data at a time upon user request.
    
    Args:
        df - Pandas DataFrame containing city data
    """
    row_index = 0
    raw_data = input("\nWould you like to see the first 5 rows of raw data? Enter yes or no.\n").lower()

    while raw_data == 'yes':
        print(df.iloc[row_index:row_index + 5])  
        row_index += 5
        
        
        if row_index >= len(df):
            print("You've reached the end of the data.")
            break

        raw_data = input("\nWould you like to see the next 5 rows of raw data? Enter yes or no.\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()