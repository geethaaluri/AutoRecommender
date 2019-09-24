import pandas as pd
import data_surprise as ds

from surprise import Reader, Dataset
from surprise.model_selection import train_test_split
from surprise import KNNBaseline, KNNBasic, KNNWithMeans, KNNWithZScore
from surprise import accuracy

import recommendations_cf as rec
import matrix_factorization as mf

data = ds.get_data('amazon_reviews_us_Home_Improvement_v1_00.tsv', 'data_subset.csv')
data_surprise = ds.convert_data_surprise('data_subset.csv', 'data_surprise.csv')

reader = Reader(rating_scale=(1.0, 5.0))
df_loaded = Dataset.load_from_df(data_surprise, reader)

# split data to test and train
data_train, data_test = train_test_split(df_loaded, random_state=42)


def fit_model(loaded_data, model_selection='user_user'):

    # default model is user-user based collaborative filtering
    if model_selection == 'user_user':
        algo = KNNWithMeans(k=50, sim_options={'name': 'pearson_baseline', 'user_based': True})
    elif model_selection == 'item_item':
        algo = KNNWithMeans(k=50, sim_options={'name': 'pearson_baseline', 'user_based': False})
    else:
        algo = mf.matrix_factorization_param(loaded_data)

    algo.fit(data_train)
    return algo


model = fit_model(df_loaded, model_selection='user_user')
# predicting on train set
print("User-User based Model : Training Set")
train_pred = model.test(data_train.build_testset())
accuracy.rmse(train_pred)

# run the trained model against the testset
test_pred = model.test(data_test)
# get RMSE
print("User-User based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)

# A look at the recommendations generated
top_n = rec.get_top_n(test_pred, n=5)

# For a particular user
user = '10946321'
data_subset = pd.read_csv('data_subset.csv')
productid_to_product = dict(zip(data_subset.product_id, data_subset.product_title))

# items bought in the past
print('Items the user {0} bought in the past: \n'.format(user))
print(data_subset[data_subset.customer_id == user].product_title)

# recommendations for future purchase
print('Top recommendations are: \n')
print([productid_to_product[i[0]] for i in top_n[user]])
