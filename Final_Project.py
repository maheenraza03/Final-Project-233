## ENDG 233 F21 Final Project
## Maheen Raza (UCID: 30137445) and Clara Lodwig (UCID: 30141017) (Block 3)

import numpy as np
import matplotlib.pyplot as plt

class CountryInfo:
    """A class used to create a CountryInfo object.

        Attributes:
            language (str): String that represents the country's language
            country (str): String that represents the country's name
    """

    def __init__(self, language, country):
        self.language = language
        self.country = country
    
    def print_country_lang(self):
        """A function that prints the country's name and langauge of the country instance.

        Parameters: None
        Return: None

        """
        print("The most spoken language in {0} is {1}".format(self.country, self.language))


def highest_population(my_years_list, country_info, population_info, user_choice1, user_choice2):           
    """A function that returns the given region's country's highest population

        Parameters: my_years, country_data, population_data, user_input1, user_input2
        Return: the highest population

    """
    # Gets position of the inputted year in the list of years
    my_index = my_years_list.index(user_choice2)
    # Gets all countries in the inputted continent
    countries_region = country_info[(country_info[:,1] == user_choice1) , 0]
    # Gets rows in population array that have all the countries in the continent 
    pop_0 = population_info[np.in1d(population_info[:,0], countries_region), my_index + 1]   
    # Creates a list of all the populations in the countries for the year 
    pop_list_str = list(pop_0)
    pop_list_int = list(map(int, pop_list_str))
    # Finds maximum population in list
    high_pop = max(pop_list_int)
    return high_pop
    
     

def lowest_population(user_year_list, data_country, data_population, user_pick1, user_pick2):           
    """A function that returns the given region's country's lowest population

        Parameters: user_year_list, country_data, population_data, user_input1, user_input2
        Return: the lowest population

    """
    my_index = user_year_list.index(user_pick2)
    # Gets countries in the given continent
    countries_region = data_country[(data_country[:,1] == user_pick1) , 0] 
    # Gets rows in population array that have all the countries in the continent 
    pop_0 = data_population[np.in1d(data_population[:,0], countries_region), my_index + 1]   
    # Creates a list of all the populations in the countries for the year 
    pop_list_str = list(pop_0)
    pop_list_int = list(map(int, pop_list_str))
    # Finds minimum population in list
    low_pop = min(pop_list_int)
    return low_pop

def main():
    print()
    print('WELCOME TO THE POPULATION PROGRAM')
    print('This program will tell you:\n 1. The highest & lowest population of a specific continent. \n 2. The most common language of a given country.')
    print()

    # Importing the three csv files for the country, population and langauge data
    lang_data = np.genfromtxt('country_lang.csv', delimiter = ',', skip_header = True, dtype = str)
    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, dtype = str)
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = False, dtype = str)


    # Creates a list for the years from the header of the population data csv
    my_years = []
    i = 1
    length_yrs = len(population_data[0])
    
    # Appends each year in the first row to the list my_years
    while i <= (length_yrs - 1):
        my_years.append(population_data[0][0 + i])
        i += 1
    
    # Loop for validity of user input without terminating the program if it is not valid
    x = 0
    while x == 0:
        user_input1 = input('Enter a continent: ')
        user_input2 = input('Enter a year from 2000-2020: ')
        # check the country data CSV file in the second coloumn and check the list of years
        if user_input1 in country_data[:,1] and user_input2 in my_years:
            break
        else:
            print('The input is invalid, please enter a year from 2000-2020, and enter one of the continents; Asia, Africa, Europe, Americas or Oceania.') 

    print()

    # to calculate the continent's highest population, the highest population fucntion will be used using the following parameters
    main_h_pop = highest_population(my_years, country_data, population_data, user_input1, user_input2)  
    print('Of all of the countries in', user_input1, 'the highest population was', main_h_pop, 'in', user_input2)
    
    # to calculate the continent's lowest population, the lowest population fucntion will be used using the following parameters
    main_l_pop = lowest_population(my_years, country_data, population_data, user_input1, user_input2)   
    print('Of all of the countries in', user_input1,'the lowest population was', main_l_pop, 'in', user_input2)

    # this will calculate the average of the two values
    average_pop = ((main_h_pop) + (main_l_pop)) // 2
    print('The average of the two populations is', average_pop)

    # Find index for each year in the list of years
    index_2015 = my_years.index('2015')
    index_2016 = my_years.index('2016')
    index_2017 = my_years.index('2017')
    index_2018 = my_years.index('2018')
    index_2019 = my_years.index('2019')
    index_2020 = my_years.index('2020')

    # Gets countries in the given continent
    countries_region = country_data[(country_data[:,1] == user_input1) , 0]
    # Finds the elements in the population array that have all the countires in the continent for each year
    pop_2015 = population_data[np.in1d(population_data[:,0], countries_region), index_2015]
    pop_2016 = population_data[np.in1d(population_data[:,0], countries_region), index_2016]
    pop_2017 = population_data[np.in1d(population_data[:,0], countries_region), index_2017]
    pop_2018 = population_data[np.in1d(population_data[:,0], countries_region), index_2018]
    pop_2019 = population_data[np.in1d(population_data[:,0], countries_region), index_2019]
    pop_2020 = population_data[np.in1d(population_data[:,0], countries_region), index_2020]

    # Converts the poulations into a list
    list_pop_2015 = list(pop_2015)
    # Makes the list into integers
    list_pop_2015_int = list(map(int, list_pop_2015))
    # Sums all elements in the list
    sum_2015 = sum(list_pop_2015_int)
    
    list_pop_2016 = list(pop_2016)
    list_pop_2016_int = list(map(int, list_pop_2016))
    sum_2016 = sum(list_pop_2016_int)

    list_pop_2017 = list(pop_2017)
    list_pop_2017_int = list(map(int, list_pop_2017))
    sum_2017 = sum(list_pop_2017_int)

    list_pop_2018 = list(pop_2018)
    list_pop_2018_int = list(map(int, list_pop_2018))
    sum_2018 = sum(list_pop_2018_int)
    
    list_pop_2019 = list(pop_2019)
    list_pop_2019_int = list(map(int, list_pop_2019))
    sum_2019 = sum(list_pop_2019_int)
    
    list_pop_2020 = list(pop_2020)
    list_pop_2020_int = list(map(int, list_pop_2020))
    sum_2020 = sum(list_pop_2020_int)

    # Creates plot points for the sum of population for each year in blue and labels them on the legend
    plt.plot([2015], sum_2015, 'bo', label = '2015 Population')
    plt.plot([2016], sum_2016, 'bo', label = '2016 Population')
    plt.plot([2017], sum_2017, 'bo', label = '2017 Population')
    plt.plot([2018], sum_2018, 'bo', label = '2018 Population')
    plt.plot([2019], sum_2019, 'bo', label = '2019 Population')
    plt.plot([2020], sum_2020, 'bo', label = '2020 Population')
    # Creates legend and fixes it to the upper left corner of the graph
    plt.legend(shadow=True, loc="upper left" )                                      
    # Sets the x axis ticks
    plt.xticks([2015, 2016, 2017, 2018, 2019, 2020])                                                          
    plt.xlabel("Years")                                                       
    plt.ylabel("Population")                                                  
    plt.title("Population of the continent over the last 5 years ")
    # Prints the graph
    plt.show()      

    print()

    # Creates a list of all the countries in the population data array
    list_of_countries = country_data[:, 0].tolist()
    # Creates a list of all the languages from the country language array
    list_of_languages = lang_data[:, 2].tolist()
    # will create a dictionary that maps every country to their respective language 
    country_lang_dict = dict(zip(list_of_countries, list_of_languages))

    # While loop to check if the country the user input is valid or not
    x = 0
    while x == 0:
        user_input3 = input('Now, enter a specific country name: ')
        if user_input3 in list_of_countries:
            break
        else:
            # Reprompt without terminating the program
            print('Enter a valid country: ')

    # Find the language of the input  using the dictionary        
    lang_of_country = country_lang_dict[user_input3]
    # By using the CountryInfo class, parameters will be passed in to print the country and its respective language
    given_lang = CountryInfo(lang_of_country, user_input3)
    given_lang.print_country_lang()

    # Finds the index of the inputted country in the created list of countries
    country_index = list_of_countries.index(user_input3)
    # Finds the population at the country index in 2015 
    pt_2015 = [population_data[country_index][16]]
    # Makes population into an integer
    point_2015 = int(' '.join(pt_2015))
    # Finds the population at the country index in 2016
    pt_2016 = [population_data[country_index][17]]
    point_2016 = int(' '.join(pt_2016))
    # Finds the population at the country index in 2017   
    pt_2017 = [population_data[country_index][18]]
    point_2017 = int(' '.join(pt_2017))
    # Finds the population at the country index in 2018
    pt_2018 = [population_data[country_index][19]]
    point_2018 = int(' '.join(pt_2018))
    # Finds the population at the country index in 2019    
    pt_2019 = [population_data[country_index][20]]
    point_2019 = int(' '.join(pt_2019))
    # Finds the population at the country index in 2020
    pt_2020 = [population_data[country_index][21]]
    point_2020 = int(' '.join(pt_2020))

    # Creates plot points for the years in different colors and labels them on the legend
    plt.plot([2015], point_2015, 'bo', label = '2015 Population')
    plt.plot([2016], point_2016, 'ro', label = '2016 Population')
    plt.plot([2017], point_2017, 'ko', label = '2017 Population')
    plt.plot([2018], point_2018, 'yo', label = '2018 Population')
    plt.plot([2019], point_2019, 'mo', label = '2019 Population')
    plt.plot([2020], point_2020, 'co', label = '2020 Population')
    # Creates legend and fixes it to the upper left corner of the graph
    plt.legend(shadow=True, loc="upper left" )                                      
    # Sets the x axis ticks
    plt.xticks([2015, 2016, 2017, 2018, 2019, 2020])                                                          
    plt.xlabel("Years")                                                       
    plt.ylabel("Population")                                                  
    plt.title("Population for the last 5 years in this country")              
    # Prints the graph
    plt.show()     
    

if __name__ == '__main__':
    main()