


def remove_unusable_features(df_train, df_test, features):
    """
    Remove  categorical features where train and test dataframe have different unique values
"""
    for feat in features :
        if len(set(df_train[feat].unique()) ^ set(df_test[feat].unique()))> 0 :
            print(f"cat. features {feat} takes different values in train and test set \n "
                  f" -> {feat} deleted \n")

            print(df_train[feat].unique(), df_test[feat].unique(),"\n")
            del df_train[feat]
            del df_test[feat]



