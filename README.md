# RecServe
*Recommendations as a service*


## Project Description

RecServe is a recommendations as a service tool that allows users to input their custom datasets and obtain recommendations easily. It is evident that personalization technologies provide great business results and engage users dramatically increasing customer retention. Only larger organizations like Amazon and Netflix were able to leverage and customize the recommendation engines sustained by specific business units. Maintaining specific teams within the company involves developmental cost that is simply too high for most SME's and small businesses. Automated recommendation systems which can be easily integrated with their existing systems is an elegant solution to this problem.

RecServe is an intelligent recommendation system that recommends a single algorithm without training and tuning five or more different ML algorithms!

A google slide presentation can be found [here](http://bit.ly/geetha-recserve).

After downloading this repo and follow the installation instuctions below you will be able to experiment with RecServe through an interactive command line interface.

The command line interface will prompt you for information and display your results, for example: 

> *"Welcome to RecServe! Let me help you with the product recommendations."*

> *Enter the path for your sample data:* data_subset.csv


> *"Geetha, do you want to recommend items for users to purchase? [y/N]*"
> ***Yes***

> *Enter the customer id*: 18055986

	These products were selected for your customer by using similar user profiles for recommendations
	The top recommendation are:
	1. 5mm Black Plastic LED Holders x50
	2. General Electric WD12X10278 Roller Stud
	3. TaoTronics Sound Activated RGB Music Control
	4. S14 Bulbs by Deneve, 11 Watts, Clear Glass S14
	5. Rheem Ruud Weather King, RGP Mid Efficiency
	
	
> *"Geetha, do you want to recommend similar items for users to purchase? [y/N]*"
> ***Yes****

> *Enter the product name:* SimpliSafe Wireless Home Security Command

	These items were selected for your customer by using item similarities
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
    
 ## Package Installations
	pip install pandas
	pip install click
	pip install colorama
	pip install surprise 
	pip install scikit-learn or pip install sklearn

## Installation / Setup
Clone repository and update python path:
The easiest way to download this project is by using git from the command-line:

	git clone https://github.com/geethaaluri/AutoRecommender.git
	
Unzip pickeled data file from command line:

	cd Data/
	unzip predicted_ratings.pkl.zip


## Environment
I recommend creating a conda environoment so you do not destroy your main installation in case you make a mistake somewhere:

    conda create --name RecServe_3.6 python=3.6 ipykernel
You can activate the new environment by running the following (on Linux):

    source activate RecServe_3.6 
And deactivate it:

    source deactivate RecServe_3.6 

## Build Environment (***Optional***)

> Before running your Orient.py script:
 
If you would like to rerun the Keras model to fill in the User x Movie matrix run:
	
	python fill_user_matrix.py
	
This will build a Keras factorization model to predict previously unrated movies for users with embeddings. The resulting pkl file will be: (also option to generate a csv file)

	predicted_ratings.pkl

This file is already available in the Orient 'Data' folder once you unpack the predicted_ratings.pkl.zip file. 
	
To generate occupation embeddings you can run:
	
	python Word2Vec_occupations.py

To generate the csv file (which is also provided to you in the repo, but in the Word2Vec folder):

	Occupation_embeddings.csv
	
I would only recommend this to those who would like to download Google's [Word2Vec](http://word2vec.googlecode.com/svn/trunk/) tool. 

## Serving Orient

Now you should be all set to get your movie recommendations through the Orient.py interactive command-line interface using:

	cd src/
	Python Orient.py
	
Thank you for choosing Orient to optimize your ***Movie Night*** experience!

## Licensing
MovieLens Dataset [LICENSE](https://github.com/AstronomerAmber/Project-Orient/edit/master/LICENSE.md)
