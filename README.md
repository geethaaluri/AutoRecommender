# RecServe
*Recommendations as a service*


## Project Description

RecServe is a recommendations as a service tool that allows users to input their custom datasets and obtain recommendations easily. It is evident that personalization technologies provide great business results and engage users dramatically increasing customer retention. Only larger organizations like Amazon and Netflix were able to leverage and customize the recommendation engines sustained by specific business units. Maintaining specific teams within the company involves developmental cost that is simply too high for most SME's and small businesses. Automated recommendation systems which can be easily integrated with their existing systems is an elegant solution to this problem.

RecServe is an intelligent recommendation system that recommends a single algorithm without training and tuning five or more different ML algorithms!

A Google slide presentation can be found here: http://bit.ly/geetha-recserve

After downloading this repo and follow the installation instuctions below you will be able to experiment with RecServe through an interactive command line interface.

The command line interface will prompt you for information and display your results, for example: 

> *Thank you Amber here are your recommendations:*
> Generating Movie Recommendations...
> Movies (year) Average Rating:

	['Return of the Jedi (1983)' 3.8]
	['Wizard of Oz, The (1939)' 3.78]
	['Empire Strikes Back, The (1980)' 3.76]

> *Would you like to view the factors that led to these particular movie recommendations? [y/N]*: 
> ***Yes***

> These movies were selected for by using ***10*** similar user profiles for movie recommendations
> These ***10*** user profiles profiles were ***>97.88%*** similar to your own.
	
	Atrribute breakdown of similar users:
	Female gender: 80.0%
	Over the age of 30: 30.0%
	Technical occupation: 100.0%
	Westcoast: 40.0%

## Setup
Clone repository and update python path
```
