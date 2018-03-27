# myPredict_079425.ipynb

## feature

- Title
  - one hot encoding
  - keep rare Title
- Age
  - fill NaN by mean grouped by Sex&Pclass
  - change to AgeBand
    - 5
- Age*Pclass
  - Age*Pclass
- Faimly related(Parch, SibSp, FamilySize, IsAlone)
  - Parch, SibSp
- Embarked
  - one hot encoding
- Fare
  - fill NaN by median of test_df
  - change to FareBand
    - 4
-
-

## model

- GradientBoostingClassifier
- grid search result by train_df, all train data
  - n_estimators, learning_rate, max_depth


param_grid = {'n_estimators': [3, 5, 7, 10, 50, 100, 200, 500],
              'learning_rate': [0.001, 0.01, 0.1, 1, 10, 100],
             'max_depth':[1,2,3,4,5,6]}
grid_search = GridSearchCV(GradientBoostingClassifier(), param_grid, cv=5, n_jobs=3)
grid_search.fit(X_train_df, y_train_df)

=>

Mean cross-validated score of the best_estimator:  0.8249158249158249
best parameters: {'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 200}


----

# current testing model

## GradientBoostingClassifier: 10 age band, parch&sibsp, embarked num category, rare title&map value

- forgot to delete Cabin_Letter_0
- Converting Embarked categorical feature to numeric
- change rare title to "Rare" and map value

0.75119

## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value

- use familysize



## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value, no Name_Len

- del Name_Len


## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value, no Name_Len, no Ticket_Len

- del Ticket_Len

0.78468



## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value, no Name_Len, no Ticket_Len, one Cabin_Letter feature


- make one Cabin_Letter feature 

0.78468



best parameters: {'learning_rate': 0.1, 'max_depth': 4, 'max_features': 'sqrt', 'min_samples_leaf': 5, 'min_samples_split': 3, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8489932885906041
test:  0.8305084745762712

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_leaf', 'min_samples_split', 'n_estimators']
1|0.848993(std:0.042450)|[0.1, 4, 'sqrt', 5, 3, 50]
2|0.847315(std:0.033216)|[0.005, 5, 'log2', 4, 4, 400]
3|0.845638(std:0.039315)|[0.02, 3, 'sqrt', 4, 4, 300]
3|0.845638(std:0.036244)|[0.02, 4, 'sqrt', 4, 5, 100]
3|0.845638(std:0.033711)|[0.05, 5, 'sqrt', 2, 6, 50]
3|0.845638(std:0.033790)|[0.1, 4, 'sqrt', 4, 6, 50]
3|0.845638(std:0.026592)|[0.1, 7, 'sqrt', 1, 2, 7]
8|0.843960(std:0.031987)|[0.005, 5, 'log2', 4, 2, 400]
8|0.843960(std:0.031263)|[0.01, 4, 'log2', 4, 6, 400]
8|0.843960(std:0.036095)|[0.01, 5, 'sqrt', 1, 4, 200]
8|0.843960(std:0.046819)|[0.02, 3, 'sqrt', 3, 5, 300]
8|0.843960(std:0.036310)|[0.02, 3, 'log2', 3, 6, 300]
8|0.843960(std:0.029286)|[0.02, 6, 'sqrt', 5, 2, 100]
8|0.843960(std:0.042761)|[0.05, 3, 'sqrt', 4, 3, 100]
8|0.843960(std:0.037832)|[0.05, 3, 'log2', 4, 4, 100]
8|0.843960(std:0.041079)|[0.05, 3, 'log2', 4, 5, 100]
8|0.843960(std:0.033724)|[0.05, 4, 'log2', 1, 4, 50]
8|0.843960(std:0.029372)|[0.05, 5, 'sqrt', 4, 5, 50]
8|0.843960(std:0.025402)|[0.05, 5, 'log2', 5, 5, 50]



## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value, no Name_Len, no Ticket_Len, one Cabin_Letter feature, del Cabin_Num features


- del Cabin_Num features

best parameters: {'learning_rate': 0.1, 'max_depth': 3, 'max_features': 'log2', 'min_samples_leaf': 5, 'min_samples_split': 2, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8422818791946308
test:  0.8305084745762712

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_leaf', 'min_samples_split', 'n_estimators']
1|0.842282(std:0.039318)|[0.1, 3, 'log2', 5, 2, 50]
2|0.838926(std:0.037329)|[0.007, 4, 'log2', 5, 2, 400]
2|0.838926(std:0.041292)|[0.02, 3, 'sqrt', 4, 6, 400]
2|0.838926(std:0.038219)|[0.1, 3, 'sqrt', 4, 5, 50]
2|0.838926(std:0.033613)|[0.1, 3, 'log2', 1, 5, 50]
2|0.838926(std:0.041584)|[0.1, 3, 'log2', 4, 4, 50]
2|0.838926(std:0.028890)|[0.1, 4, 'sqrt', 5, 4, 50]
8|0.837248(std:0.040103)|[0.02, 3, 'sqrt', 5, 4, 300]
8|0.837248(std:0.036323)|[0.02, 4, 'sqrt', 4, 4, 200]
8|0.837248(std:0.028291)|[0.05, 3, None, 1, 2, 200]
8|0.837248(std:0.028291)|[0.05, 3, None, 1, 4, 200]
8|0.837248(std:0.033345)|[0.05, 5, 'log2', 5, 5, 50]
8|0.837248(std:0.037624)|[0.1, 3, 'log2', 1, 4, 100]
8|0.837248(std:0.025055)|[0.1, 3, 'log2', 1, 6, 200]
8|0.837248(std:0.041710)|[0.1, 4, 'sqrt', 1, 3, 50]
8|0.837248(std:0.030870)|[0.1, 4, 'log2', 5, 3, 50]


## GradientBoostingClassifier: 10 age band, familysize, embarked num category, rare title&map value, no Name_Len, no Ticket_Len, one Cabin_Letter feature, del Cabin_Num features, activate Age*Class again

- activate Age*Class again

0.77990

best parameters: {'learning_rate': 0.2, 'max_depth': 4, 'max_features': 'sqrt', 'min_samples_leaf': 2, 'min_samples_split': 3, 'n_estimators': 10}
Mean cross-validated score of the best_estimator:  0.8406040268456376
test:  0.8406779661016949

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_leaf', 'min_samples_split', 'n_estimators']
1|0.840604(std:0.039600)|[0.2, 4, 'sqrt', 2, 3, 10]
2|0.838926(std:0.044443)|[0.01, 3, 'log2', 4, 2, 400]
2|0.838926(std:0.044709)|[0.02, 3, 'sqrt', 4, 4, 200]
2|0.838926(std:0.044443)|[0.02, 3, 'sqrt', 4, 5, 200]
2|0.838926(std:0.041648)|[0.02, 4, 'log2', 5, 4, 100]
2|0.838926(std:0.043104)|[0.05, 3, 'sqrt', 4, 3, 100]
2|0.838926(std:0.044903)|[0.1, 3, 'log2', 1, 2, 50]
2|0.838926(std:0.025955)|[0.2, 6, 'sqrt', 4, 3, 7]
9|0.837248(std:0.044516)|[0.01, 3, 'log2', 4, 4, 400]
9|0.837248(std:0.043828)|[0.02, 3, 'sqrt', 4, 6, 300]
9|0.837248(std:0.044516)|[0.02, 3, 'log2', 4, 6, 200]
9|0.837248(std:0.043383)|[0.02, 4, 'sqrt', 1, 5, 200]
9|0.837248(std:0.046819)|[0.05, 3, 'sqrt', 4, 4, 100]
9|0.837248(std:0.031411)|[0.05, 3, 'sqrt', 5, 6, 100]
9|0.837248(std:0.044677)|[0.05, 3, 'log2', 2, 5, 100]
9|0.837248(std:0.043704)|[0.05, 3, 'log2', 4, 4, 100]
9|0.837248(std:0.044711)|[0.05, 3, 'log2', 4, 6, 100]
9|0.837248(std:0.032774)|[0.05, 5, 'log2', 4, 5, 50]
9|0.837248(std:0.041284)|[0.1, 3, 'log2', 5, 2, 50]
9|0.837248(std:0.040684)|[0.2, 4, 'sqrt', 5, 4, 7]



## 1 GradientBoostingClassifier

- 10 age band
- familysize
- embarked num category
- rare title&map value
- no Name_Len
- no Ticket_Len
- one Cabin_Letter feature
- del Cabin_Num features
- activate Age*Class again
- try another title mapping. from 5 category(inc. rare) to 6 category(complete map rare to other title)

mapping = {'Mlle': 'Miss', 
            'Major': 'Mr', 
            'Col': 'Mr', 
            'Sir': 'Mr',
            'Don': 'Mr', 
            'Mme': 'Miss',
            'Jonkheer': 'Mr',
            'Lady': 'Mrs', 
            'Capt': 'Mr', 
            'Countess': 'Mrs',
            'Ms': 'Miss',
            'Dona': 'Mrs'}
titles = ['Dr', 'Master', 'Miss', 'Mr', 'Mrs', 'Rev']





best parameters: {'learning_rate': 0.2, 'max_depth': 4, 'max_features': 'log2', 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8473053892215568
test:  0.8026905829596412
confusion matrix:  [[113  21]
 [ 23  66]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_leaf', 'min_samples_split', 'n_estimators']
1|0.847305(std:0.023510)|[0.2, 4, 'log2', 4, 5, 300]
2|0.844311(std:0.035000)|[0.2, 5, 'log2', 5, 3, 400]
2|0.844311(std:0.024509)|[0.2, 6, 'sqrt', 4, 2, 50]
4|0.842814(std:0.027134)|[0.1, 5, 'log2', 4, 3, 400]
4|0.842814(std:0.028805)|[0.2, 4, 'log2', 5, 4, 400]
4|0.842814(std:0.035875)|[0.2, 6, 'log2', 5, 6, 300]
4|0.842814(std:0.029787)|[0.2, 7, 'sqrt', 3, 2, 300]
8|0.841317(std:0.034481)|[0.01, 4, 'sqrt', 3, 5, 200]
8|0.841317(std:0.042157)|[0.1, 4, 'sqrt', 1, 4, 200]
8|0.841317(std:0.039613)|[0.1, 4, 'log2', 5, 6, 400]
8|0.841317(std:0.042075)|[0.1, 5, 'sqrt', 1, 4, 100]
8|0.841317(std:0.029249)|[0.1, 5, 'log2', 4, 5, 400]
8|0.841317(std:0.030651)|[0.1, 5, 'log2', 4, 6, 400]
8|0.841317(std:0.035506)|[0.1, 6, 'sqrt', 1, 2, 100]
8|0.841317(std:0.040615)|[0.1, 6, 'log2', 1, 6, 100]
8|0.841317(std:0.026786)|[0.1, 7, 'log2', 5, 5, 300]
8|0.841317(std:0.039613)|[0.2, 3, 'sqrt', 4, 4, 400]
8|0.841317(std:0.039354)|[0.2, 3, 'log2', 2, 2, 400]
8|0.841317(std:0.035071)|[0.2, 3, 'log2', 5, 2, 400]
8|0.841317(std:0.026313)|[0.2, 4, 'sqrt', 4, 4, 200]
8|0.841317(std:0.027297)|[0.2, 4, 'sqrt', 4, 4, 300]
8|0.841317(std:0.028622)|[0.2, 4, 'sqrt', 4, 5, 400]
8|0.841317(std:0.031055)|[0.2, 4, 'log2', 2, 5, 300]
8|0.841317(std:0.028887)|[0.2, 4, 'log2', 5, 6, 400]
8|0.841317(std:0.031810)|[0.2, 6, 'sqrt', 2, 2, 400]
8|0.841317(std:0.028887)|[0.2, 6, 'sqrt', 5, 2, 400]
8|0.841317(std:0.034788)|[0.2, 6, 'log2', 1, 2, 100]





## 1 GradientBoostingClassifier

- [x] 10 age band
- [x] familysize
- [x] embarked num category
- [x] rare title&map value
- [ ] no Name_Len
- [x] no Ticket_Len
- [x] one Cabin_Letter feature
- [x] del Cabin_Num features
- [x] activate Age*Class again
- [x] try another title mapping. from 5 category(inc. rare) to 6 category(complete map rare to other title)








----

# 

- [x] increase gradient boosting param : min_samples_leaf . add 4
- [ ] make ticket null
- [x] make one Cabin_Letter feature from Cabin_Letter features
- [x] del Cabin_Num features
- [x] narrow down random forest
- [ ] back to AgeBand from 10 to 5
- [ ] make bigger FareBand from 4 to 5
- [x] try another title mapping. from 5 category(inc. rare) to 6 category(complete map rare to other title)

mapping = {'Mlle': 'Miss', 
            'Major': 'Mr', 
            'Col': 'Mr', 
            'Sir': 'Mr',
            'Don': 'Mr', 
            'Mme': 'Miss',
            'Jonkheer': 'Mr',
            'Lady': 'Mrs', 
            'Capt': 'Mr', 
            'Countess': 'Mrs',
            'Ms': 'Miss',
            'Dona': 'Mrs'}
titles = ['Dr', 'Master', 'Miss', 'Mr', 'Mrs', 'Rev']

- [ ] make title numerical feature including rare titles
