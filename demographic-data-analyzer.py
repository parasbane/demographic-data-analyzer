import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = df[higher_education & (df['salary'] == '>50K')]
    percentage_higher_education_rich = round(len(higher_education_rich) / len(df[higher_education]) * 100, 1)

    # 5. Percentage without advanced education earning >50K
    lower_education = ~higher_education
    lower_education_rich = df[lower_education & (df['salary'] == '>50K')]
    percentage_lower_education_rich = round(len(lower_education_rich) / len(df[lower_education]) * 100, 1)

    # 6. Minimum number of work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work fewest hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest percentage of rich
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country = (country_rich / country_total * 100).idxmax()
    highest_earning_country_percentage = round((country_rich / country_total * 100).max(), 1)

    # 9. Most popular occupation in India for those earning >50K
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {percentage_lower_education_rich}%")
        print("Min work time:", min_work_hours)
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
