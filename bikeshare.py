import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# ====================================================================================================================
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # --------------------------------------------------------------------------------------------------
    running = True
    City = ['Chicago', 'New York City', 'Washington']
    while running:
        try:
            city = float(
                input(
                    '\nPlease enter the number of one the following cities: \n'+
                    '1 - Chicago\n'+
                    '2 - New York City\n'+
                    '3 - Washington\n'+
                    'Enter your value: '
                )
            )
            print('')
            if ( city>=1 ) & ( city<=3 ) & ( city-int(city)==0 ):
                city = int(city)
                running = False
            elif (city-int(city)!=0):
                print('\nYour value is not an integer.\n')
            else:
                print('\nYour value is associated with any city name. Please choose a correct value.\n')
                
        except (ValueError, TypeError):
            print('\nThat is not a valid number.\n')

    city = City[city-1]
    print('You have selected {}.'.format(city))
    print('')
        
    # get user input for month (all, january, february, ... , june)
    # --------------------------------------------------------------------------------------------------
    running = True
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    while running:
        try:
            month = float(
                input(
                    '\nPlease enter the number of one the following months (Select the last number as "All"): \n'+
                    '1 - January\n'+
                    '2 - February\n'+
                    '3 - March\n'+
                    '4 - April\n'+
                    '5 - May\n'+
                    '6 - June\n'+
                    '7 - All\n'+
                    'Enter your value: '
                )
            )
            print('')
            if ( month>=1 ) & ( month<=7 ) & ( month-int(month)==0 ):
                month = int(month)
                running = False
            elif (month-int(month)!=0):
                print('\nYour value is not an integer.\n')
            else:
                print('\nYour value is associated with any city name. Please choose a correct value.\n')
        except ValueError:
            print('\nThat is not a valid number.\n')
            
    print('\nYour choice is {}.\n'.format(Months[month-1]))
    print('')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # --------------------------------------------------------------------------------------------------
    running = True
    Days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while running:
        try:
            day = str(
                input(
                    '\nPlease select one a day of the week (Select "All"): \n'+
                    '- All \n'+
                    '- Monday\n'+
                    '- Tuesday\n'+
                    '- Wednesday\n'+
                    '- Thursday\n'+
                    '- Friday\n'+
                    '- Saturday\n'+
                    '- Sunday\n'+
                    '- Enter your desired day: '
                )
            )
            print('')
            if day.title() in Days:
                day = day.title()
                running = False
            else:
                print('\n{} is not a day.\n'.format(day))
        except ValueError:
            print('\nThat is not a valid input.\n')
            
    print('\nYour selected day is {}.\n'.format(day))

    print('-'*40)
    return city, month, day

# ====================================================================================================================     
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
    # ---------------------------------------------------
    filename = {
        'Chicago':'chicago.csv',
        'New York City':'new_york_city.csv',
        'Washington':'washington.csv',
    }
    
    # ---------------------------------------------------
    df = pd.read_csv(filename[city])
    
    # ---------------------------------------------------
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # ---------------------------------------------------
    df['Month'] = df['Start Time'].dt.month
    df['Hour'] = df['Start Time'].dt.hour
    df['Month Name'] = df['Start Time'].dt.month_name()
    df['Day Name']   = df['Start Time'].dt.strftime("%A")
    
    # ---------------------------------------------------
    if month!=7:
        df = df[df['Month']==month]
    if day!='All':
        df = df[df['Day Name']==day]

    return df

# ====================================================================================================================
def display_raw_data(df):
    """
    Show the raw data from the CSV file upon request.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    i = 0
    pd.set_option('display.max_columns',200)
    while True:
        if (i>=len(df)):
            print('\nThere is no more data to show. You have reached the end of the dataframe.\n')
            break
        raw = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
        if (raw=='no')|(raw=='n'):
            break
        elif (raw == 'yes')|(raw == 'y'):
            print(df.iloc[i:i+5,:])
            i += 5
        else:
            print('\nYour input is invalid. Please enter only "yes" or "no"\n')

# ====================================================================================================================
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month: ', df['Month Name'].mode()[0])

    # display the most common day of week
    print('The most common month: ', df['Day Name'].mode()[0])

    # display the most common start hour
    print('The most common start hour: ', df['Hour'].mode()[0])

    print('\nThis took {} seconds.'.format(time.time() - start_time))
    print('-'*40)

# ====================================================================================================================
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most common used end station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: '+
          ' %s - %s'%df.groupby(['Start Station', 'End Station']).size().idxmax())

    print('\nThis took {} seconds.'.format(time.time() - start_time))
    print('-'*40)

# ====================================================================================================================
def convert(sec):
    '''
    convert seconds to days, hours, minute, and seconds format.

    Args:
       - seconds
    '''
    day   = sec // (24 * 3600)
    sec  %= (24 * 3600)
    hour  = sec // 3600
    sec  %= 3600
    mins  = sec // 60
    sec  %= 60
    
    return '%i days %d:%02d:%02d'%(day, hour, mins, sec)

# ====================================================================================================================
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time: {}'.format(convert(df['Trip Duration'].sum())))

    # display mean travel time
    print('The mean travel time: {}'.format(convert(df['Trip Duration'].mean())))

    print('\nThis took {} seconds.'.format(time.time() - start_time))
    print('-'*40)

# ====================================================================================================================
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.keys():
        print('The counts of user types:\n', df['User Type'].value_counts())
    else:
        print('User type does not exist in this dataset.')

    # Display counts of gender
    if 'Gender' in df.keys():
        print('The counts of gender:\n', df['Gender'].value_counts())
    else:
        print('Information about gender does not exist in this dataset.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.keys():
        print('The youngest year of birth: {}'.format(int(df['Birth Year'].max())))
        print('The oldest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('The most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('Year of birth is not in the data.')
    
    print('\nThis took {} seconds.'.format(time.time() - start_time))
    print('-'*40)

# ====================================================================================================================
def main():
    running=True
    while running:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        running2=True
        while running2:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if (restart.lower() == 'no')|(restart.lower() == 'n'):
                running=False
                running2=False
                break
            elif (restart.lower() == 'yes')|(restart.lower() == 'y'):
                running=True
                running2=False
            else:
                print('\nYour answer is invalid. Please enter "yes" or "no".')
        


if __name__ == "__main__":
	main()
