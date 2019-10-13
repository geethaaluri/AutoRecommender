# RecServe
*Recommendations as a service*


## Project Description

RecServe is a recommendations as a service tool that allows users to input their custom datasets and obtain recommendations easily. It is evident that personalization technologies provide great business results and engage users dramatically increasing customer retention. Only larger organizations like Amazon and Netflix were able to leverage and customize the recommendation engines sustained by specific business units. Maintaining specific teams within the company involves developmental cost that is simply too high for most SME's and small businesses. Automated recommendation systems which can be easily integrated with their existing systems is an elegant solution to this problem.

RecServe is an intelligent recommendation system that recommends a single algorithm without training and tuning five or more different ML algorithms!

A google slide presentation can be found [here](http://bit.ly/geetha-recserve)

After downloading this repo and follow the installation instuctions below you will be able to experiment with RecServe through an interactive command line interface.

The command line interface will prompt you for information and display your results, for example: 

> *"Welcome to RecServe! Let me help you with the product recommendations."*

> *Enter the path for your sample data:* data_subset.csv


> *"Geetha, do you want to recommend items for users to purchase? [y/N]*"
> ***Yes***

> *Enter the customer id: 18055986

> Enter the product name: SimpliSafe Wireless Home Security Command

> These products were selected for your customer by using similar user profiles for recommendations

	The top recommendation are:
	1. 5mm Black Plastic LED Holders x50
	2. General Electric WD12X10278 Roller Stud
	3. TaoTronics Sound Activated RGB Music Control
	4. S14 Bulbs by Deneve, 11 Watts, Clear Glass S14
	5. Rheem Ruud Weather King, RGP Mid Efficiency
	
	
> *"Geetha, do you want to recommend similar items for users to purchase? [y/N]*"
> ***Yes****

> Enter the product name: SimpliSafe Wireless Home Security Command

> These items were selected for your customer by using item similarities

	The top recommendations are:
	1. GE Simon XT Wireless Home Security System
	2. 1byone Wireless Home Security Driveway Alarm
	3. AAS 100 Wireless Home Security Alarm kit
	4. AAS V500 Wireless Home Security Alarm System
	5. JEBSENS - Home Security TV STV-21 Burglar detector
	

The goal of RecServe is to be deployed within a company's system to suggest a recommendation algortihm that works best for their data and ultimately give appropriate recommendations based on user input.

## Data

RecServe is currently using the Amazon Reviews Dataset.

	142.8 million reviews
	review data - ratings, text, helpfulness votes
	product data - descriptions, category information
	data spanning from May 1996 - July 2014.

SAMPLE CONTENT:
https://s3.amazonaws.com/amazon-reviews-pds/tsv/sample_us.tsv
https://s3.amazonaws.com/amazon-reviews-pds/tsv/sample_fr.tsv 


## Requirements / Dependencies
	Python 3.6
	Pandas 
	Click 
	Colorama 
	Surprise  
	Scikit-learn 
Scikit-learn requires:

    Python (>= 2.7 or >= 3.3)
    NumPy (>= 1.8.2)
    SciPy (>= 0.13.3)	
