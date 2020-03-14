# General Analysis on US Accidents
* The scripts folder contains the python scripts for analysis and visulization.
* The src fiolder contains the function definitions used during processing.
* The files folder contains the datasets needed for the processing.

## Steps:
#### Data Loading:  

* Import the main dataset *US Accidents* via python command `data = pd.read_csv('./US_Accidents_Dec19.csv')`. Remember to import necessary libaries, for example, Pandas libarary is utilized here.

#### Data Analysis and Visulazation:

	1. General Analysis over nationwide data

		a). Number of accidents versus different weather condition in general

	   	-> location: scripts/weather_plot_bar.py

	   	-> run command: python scripts/weather_plot_bar.py

	   	-> description: The script utilized the data imported earlier and  plot
			  out the bar char of numbers of nationwide accidents with regard to the  
			  diverse weather conditions.

		b). Number of Accidents regarding to different timing

	   	-> location: scripts/date_of_week.py
						src/which_day.py

	   	-> run command: python scripts/date_of_week.py

	   	-> description: The function being called is "which day(date_time)".
			  The "date_time" is the dataset sorted with respect to "Start time".
			  The script is calling the function to determine the date of a week and
			  plot out the number distribution with respect to different date of a
			  week as well as diverse hours of a day.

		c) Distribution over highway data with regard to severity

	   	-> location: src/severity_nationwide.py

	   	-> run command: python src/severity_nationwide.py

	   	-> description: This script analyzes our original dataset and plots how
			  severity is related to highway trafic and the day of the week.
			  Detection of a highway is done by checking if a highway was
			  mentioned in the description of the accident, and the day of
			  accident is provided.

		d). Number of Accidents regarding to poverity distribution

	   	-> location: src/poverty_calculations.py

	   	-> run command: src/poverty_calculations.py

	   	-> description: This script extracts poverty, population, and vehicle
			  statistics from multiple sources (Census Bureau, DMV) and
			  processes them to find correlations between poverty rates
			  and accidents per capita nationwide, as well as poverty rates
			  vs accidents per vehicle in California 


	2. Analysis focusing on California dataset:

	    a) Analysis on Weather conditions versus Severity

	        -> location: scripts/weather_severity_analysis.py

	        -> run command: python scripts/weather_severity_analysis.py

	        -> description: The script strips out the data for California and process
		   	the data and reports numbers of accidents sorted by severity level as
		   	well as the comparison of severity percentage to different weather
			   conditions.

		b) Analysis on effect of California's county densities to numbers of accidets:

			-> location: src/get_cali_data.py
						 src/CA_county_density_functions.py
						 src/county_ratio.py

			-> run command: python src/get_cali_data.py
							python src/CA_county_density_functions.py
							python src/county_ratio.py

			-> description: The "get_cali_data" function strips out the dataset for
			   California from the entire nationwide dataset. The script then process
			   the new California dataset to observe the numbers of accidents through
			   "get_n_accidents_CA", which returns the number of accidents
			   in California. The called function "get_area_CA" returns the
			   calculated area of California. The called function "get_population_CA"
			   returns the polupation of California. The function "get_n_vehicles_CA"
			   returns the registrated vehicles number in California. The function
			   "factor1_county(fname)" returns the number of accidents happened in
			   each county with input "fname" to be the filename of the dataset.
			   Then the scripts plot out the relationships of numbers of accidents
			   versus population per area and numbers of accidents versus the number
			   of vehicle sper area.



#### Jupyter File Demo:
* The Demo contains all the graphs used in our presentation plotted.
* The Demo contains all our code to generate our analysis.
