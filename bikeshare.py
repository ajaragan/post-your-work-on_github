#from pickle import TRUE
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'D:/DataAnalysisCourse/bikeshare-2/chicago.csv',
              'new york city': 'D:/DataAnalysisCourse/bikeshare-2/new_york_city.csv',
              'washington': 'D:/DataAnalysisCourse/bikeshare-2/washington.csv' }

# Lists of necessary data to validate user input

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYOFWEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # Get and validate user input.
    # Take user input and convert into lower case to standardize input.
    
    while True:
        city = input('Tell me the city you would like to explore: "Chicago", "New York City" or "Washington" \n').lower()
        if city not in CITIES:
            print('Oops ... that was an invalid entry. Please choose from "Chicago", "New York City" or "Washington"')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    # User can input 'All' to choose all months.
    
    while True:
        month = input('Tell me which month you would like to analyse: "January", "February", "March", "April", "May", "June", or "all" if you can\'t decide \n' ).lower()
        if month not in MONTHS:
            print('Oops ... that was an invalid entry. Please choose one of "January", "February", "March", "April", "May", "June" or "all"')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # User can input 'All' to select all days.

    while True:
        day = input('What day would you like to analyse: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" or "all" if you can\'t decide \n' ).lower()
        if day not in DAYOFWEEK:
            print('Oops ... that was an invalid entry. Please choose one of "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" or "all"')
            continue
        else:
            break
            
    print(f"\nYou selected: \nCity: {city.title()} \nMonth/s: {month.title()} \nDay/s: {day.title()}")    
    
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
    
    # Load data file into a dataframe 
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month
    #df['month'] = df['Start Time'].dt.month_name()
    df['month'] = df['Start Time'].dt.month
    
    # Extract day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Extract hour of day
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month and use month index to return corresponding int
    if month != 'all':
        #months = MONTHS
        month = MONTHS.index(month) + 1
        
        # Filter by month to create a new dataframe
        df = df[df['month'] == month]
        
    # Filter by day of week
    if day != 'all':
        
        # Filter by day of week to create a new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Use MODE to determine the value that appears most often
    
    # TO DO: display the most common month
    
    most_common_month = df['month'].mode()[0]
    print(f'\nThe most common month is: {most_common_month}')
        
    # TO DO: display the most common day of week
    
    most_common_dayofweek = df['day_of_week'].mode()[0]
    print(f'\nThe most common day of week is: {most_common_dayofweek}')

    # TO DO: display the most common start hour
       
    most_common_starthour = df['hour'].mode()[0]
    print(f'\nThe most common start hour is: {most_common_starthour}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Calculating and presenting STATION statistics
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print(f'\nThe most common start station is: {most_common_start_station}')

    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].mode()[0]
    print(f'\nThe most common end station is: {most_common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    # Create a new combined column called "Start to End" to determine most frequent combination of start and end station trip
    
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most frequent combination of start to end station trip is: {combo}.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Use SUM to calculate total trip duration and divide by 60 to convert to minutes
    
    total_travel_time = df['Trip Duration'].sum()/60
    result = '{:.2f}'.format(total_travel_time)
    print(f'\nThe total trip duration is: {result} minutes')

    # TO DO: display mean travel time
    # Use MEAN to calculate average travel time and divide by 60 to convert to minutes
    
    mean_travel_time = df['Trip Duration'].mean()/60
    result = '{:.2f}'.format(mean_travel_time)
    print(f'\nThe mean trip duration is: {result} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Calculating and presenting RIDER statistics
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Total users counted using value_counts method and displayed by type - Subscriber, Customer, Dependent
    
    user_type = df['User Type'].value_counts()
    print(f'\nCount of user types are given below:\n\n{user_type}')

    # TO DO: Display counts of gender
    # Washington does not include GENDER data. Use TRY and EXCEPT to handle this anomaly
    
    try:
        gender_type = df['Gender'].value_counts()
        print(f'\nUser count by gender is given below:\n\n{gender_type}')
    except:
        print('\nUnfortunately there is no GENDER data for Washington.')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # Washington does not include BIRTH YEAR data. Use TRY and EXCEPT to handle this anomaly
    # Use MIN, MAX and MODE to calculate earliest, most recent, and most common year of birth
    
    try:
        earliest_birth_year = df['Birth Year'].min()
        print(f'\nEarliest birth year is: {earliest_birth_year}')
        most_recent_birth_year = df['Birth Year'].max()
        print(f'\nMost recent birth year is: {most_recent_birth_year}')
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(f'\nMost common birth year is: {most_common_birth_year}')
    except:
        print('\nUnfortunately there is no BIRTH YEAR data for Washington.')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
# Give the user the option to view the individual trip data:

def display_data(df):
    row = 0
    while True:
    #Ask user if they would like to view individual trip data 
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data == 'yes':
            print(df.iloc[row : row + 5])
            row += 5
        elif view_data == 'no':
            break
        else:
            print('\n Sorry, that input was invalid. Please try again')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
