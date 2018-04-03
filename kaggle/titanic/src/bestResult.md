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





## 2 GradientBoostingClassifier

- [x] 10 age band
- [x] familysize
- [ ] embarked num category
- [x] rare title&map value
- [x] no Name_Len
- [x] no Ticket_Len
- [x] one Cabin_Letter feature
- [x] del Cabin_Num features
- [x] activate Age*Class again
- [x] try another title mapping. from 5 category(inc. rare) to 6 category(complete map rare to other title)

best parameters: {'learning_rate': 0.2, 'max_depth': 4, 'max_features': 'sqrt', 'min_samples_split': 3, 'n_estimators': 200}
Mean cross-validated score of the best_estimator:  0.8413173652694611
test:  0.8026905829596412
confusion matrix:  [[111  23]
 [ 21  68]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.841317(std:0.035094)|[0.2, 4, 'sqrt', 3, 200]
1|0.841317(std:0.040693)|[0.2, 5, 'log2', 3, 500]
1|0.841317(std:0.044309)|[0.2, 6, 'log2', 4, 50]
4|0.839820(std:0.042660)|[0.1, 5, 'log2', 4, 500]
4|0.839820(std:0.038233)|[0.1, 7, 'sqrt', 3, 300]
4|0.839820(std:0.038477)|[0.2, 4, 'sqrt', 2, 500]
4|0.839820(std:0.043400)|[0.2, 5, 'sqrt', 5, 500]
4|0.839820(std:0.035467)|[0.2, 5, 'log2', 6, 500]
9|0.838323(std:0.032846)|[0.01, 3, 'log2', 4, 400]
9|0.838323(std:0.031760)|[0.02, 3, 'sqrt', 2, 200]
9|0.838323(std:0.035516)|[0.02, 4, 'log2', 2, 100]
9|0.838323(std:0.031760)|[0.1, 3, 'sqrt', 2, 50]
9|0.838323(std:0.023865)|[0.1, 3, 'sqrt', 3, 100]
9|0.838323(std:0.034811)|[0.1, 4, 'sqrt', 4, 400]
9|0.838323(std:0.038222)|[0.1, 4, 'log2', 6, 500]
9|0.838323(std:0.038489)|[0.2, 3, 'sqrt', 3, 400]
9|0.838323(std:0.028746)|[0.2, 3, 'log2', 3, 50]
9|0.838323(std:0.030492)|[0.2, 4, 'sqrt', 3, 300]
9|0.838323(std:0.032917)|[0.2, 4, 'sqrt', 4, 300]
9|0.838323(std:0.040226)|[0.2, 4, 'log2', 3, 500]
9|0.838323(std:0.044777)|[0.2, 5, 'sqrt', 3, 500]
9|0.838323(std:0.049236)|[0.2, 5, 'log2', 4, 500]
9|0.838323(std:0.038436)|[0.2, 5, 'log2', 6, 100]
9|0.838323(std:0.039069)|[0.2, 6, 'sqrt', 5, 400]



## 3 GradientBoostingClassifier


- age
  - [ ] 5 age band
  - [x] 10 age band
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [x] integer encoding
  - [ ] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class


best parameters: {'learning_rate': 0.05, 'max_depth': 4, 'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8413173652694611
test:  0.8295964125560538
confusion matrix:  [[121  13]
 [ 25  64]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.841317(std:0.032879)|[0.05, 4, 'log2', 2, 50]
1|0.841317(std:0.031308)|[0.1, 4, 'sqrt', 4, 300]
1|0.841317(std:0.028452)|[0.2, 3, 'sqrt', 2, 500]
1|0.841317(std:0.037397)|[0.2, 4, 'sqrt', 4, 100]
5|0.839820(std:0.036424)|[0.02, 4, 'sqrt', 6, 100]
5|0.839820(std:0.028735)|[0.05, 4, 'log2', 4, 100]
5|0.839820(std:0.028186)|[0.1, 5, 'sqrt', 5, 10]
8|0.838323(std:0.032153)|[0.005, 4, 'sqrt', 2, 400]
8|0.838323(std:0.036036)|[0.02, 6, 'sqrt', 6, 400]
8|0.838323(std:0.028844)|[0.1, 4, 'log2', 4, 200]
8|0.838323(std:0.030687)|[0.1, 4, 'log2', 5, 10]
8|0.838323(std:0.038513)|[0.1, 4, 'log2', 6, 200]
8|0.838323(std:0.032141)|[0.2, 3, 'sqrt', 2, 400]
8|0.838323(std:0.029254)|[0.2, 4, 'log2', 3, 200]
8|0.838323(std:0.036152)|[0.2, 4, 'log2', 3, 300]



## 4 GradientBoostingClassifier


- age
  - [ ] 5 age band
  - [x] 10 age band
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class



best parameters: {'learning_rate': 0.2, 'max_depth': 4, 'max_features': 'log2', 'min_samples_split': 6, 'n_estimators': 7}
Mean cross-validated score of the best_estimator:  0.8413173652694611
test:  0.820627802690583
confusion matrix:  [[120  14]
 [ 26  63]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.841317(std:0.020392)|[0.2, 4, 'log2', 6, 7]
2|0.838323(std:0.029889)|[0.005, 6, 'log2', 5, 500]
2|0.838323(std:0.023627)|[0.05, 5, 'log2', 6, 50]
2|0.838323(std:0.029022)|[0.05, 5, 'log2', 6, 100]
2|0.838323(std:0.026800)|[0.1, 4, 'sqrt', 6, 10]
2|0.838323(std:0.025506)|[0.2, 4, 'log2', 6, 10]
2|0.838323(std:0.017545)|[0.2, 5, 'log2', 6, 10]
8|0.836826(std:0.025457)|[0.005, 6, 'log2', 6, 500]
8|0.836826(std:0.023403)|[0.1, 4, 'sqrt', 4, 500]
8|0.836826(std:0.041012)|[0.2, 3, 'sqrt', 3, 400]
8|0.836826(std:0.031987)|[0.2, 3, 'log2', 6, 300]





## 5 GradientBoostingClassifier


- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band


best parameters: {'learning_rate': 0.05, 'max_depth': 4, 'max_features': 'sqrt', 'min_samples_split': 5, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.8305084745762712
confusion matrix:  [[157  18]
 [ 32  88]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.043581)|[0.05, 4, 'sqrt', 5, 50]
1|0.838926(std:0.042192)|[0.05, 4, 'log2', 5, 50]
1|0.838926(std:0.023001)|[0.2, 6, 'sqrt', 4, 7]
4|0.835570(std:0.031270)|[0.007, 4, 'log2', 4, 300]
4|0.835570(std:0.034221)|[0.007, 5, 'log2', 5, 300]
4|0.835570(std:0.041902)|[0.02, 3, 'log2', 2, 200]
4|0.835570(std:0.041165)|[0.02, 5, 'sqrt', 5, 100]
4|0.835570(std:0.030212)|[0.05, 4, 'log2', 3, 50]
4|0.835570(std:0.027369)|[0.1, 4, 'log2', 5, 50]
10|0.833893(std:0.034889)|[0.005, 4, 'sqrt', 5, 400]
10|0.833893(std:0.042252)|[0.007, 3, 'log2', 5, 500]
10|0.833893(std:0.037025)|[0.007, 4, 'sqrt', 6, 300]
10|0.833893(std:0.034968)|[0.007, 4, 'log2', 4, 400]
10|0.833893(std:0.037256)|[0.007, 4, 'log2', 6, 300]
10|0.833893(std:0.039120)|[0.007, 5, 'log2', 2, 300]
10|0.833893(std:0.034968)|[0.007, 5, 'log2', 3, 300]
10|0.833893(std:0.037856)|[0.007, 5, 'log2', 5, 500]
10|0.833893(std:0.039621)|[0.01, 3, 'log2', 3, 300]
10|0.833893(std:0.035607)|[0.01, 4, 'sqrt', 2, 200]
10|0.833893(std:0.034889)|[0.01, 5, 'log2', 5, 300]
10|0.833893(std:0.033209)|[0.01, 6, 'sqrt', 3, 200]
10|0.833893(std:0.044094)|[0.02, 3, 'log2', 3, 200]
10|0.833893(std:0.032869)|[0.02, 4, 'sqrt', 4, 100]
10|0.833893(std:0.037076)|[0.02, 4, 'log2', 3, 200]
10|0.833893(std:0.038304)|[0.05, 3, 'sqrt', 3, 50]
10|0.833893(std:0.038599)|[0.05, 4, 'log2', 6, 50]
10|0.833893(std:0.031626)|[0.05, 5, 'log2', 5, 50]
10|0.833893(std:0.035619)|[0.1, 3, 'log2', 2, 200]
10|0.833893(std:0.029561)|[0.1, 4, 'sqrt', 2, 50]
10|0.833893(std:0.021312)|[0.1, 7, 'log2', 5, 7]
10|0.833893(std:0.034889)|[0.2, 3, 'log2', 3, 50]






## 6 GradientBoostingClassifier

Name_Len

0.78468

- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [x] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band










## 7 GradientBoostingClassifier

Ticket_Len
clean up data

0.78468
->
0.74641

- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [x] Name_Len
- [x] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band


best parameters: {'learning_rate': 0.005, 'max_depth': 5, 'max_features': 'sqrt', 'min_samples_split': 6, 'n_estimators': 400}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.8406779661016949
confusion matrix:  [[160  15]
 [ 32  88]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.031249)|[0.005, 5, 'sqrt', 6, 400]
2|0.837248(std:0.034610)|[0.005, 5, 'sqrt', 4, 400]
2|0.837248(std:0.027113)|[0.005, 5, 'log2', 2, 300]
2|0.837248(std:0.030703)|[0.007, 5, 'sqrt', 2, 300]
2|0.837248(std:0.031240)|[0.007, 5, 'log2', 4, 300]
2|0.837248(std:0.032080)|[0.01, 4, 'log2', 4, 300]
2|0.837248(std:0.033710)|[0.02, 5, 'sqrt', 5, 100]
2|0.837248(std:0.029727)|[0.02, 5, 'log2', 6, 100]
2|0.837248(std:0.040008)|[0.05, 4, 'log2', 2, 50]
10|0.835570(std:0.031355)|[0.005, 4, 'log2', 3, 400]
10|0.835570(std:0.030404)|[0.005, 5, 'log2', 2, 400]
10|0.835570(std:0.031582)|[0.005, 5, 'log2', 4, 300]
10|0.835570(std:0.032066)|[0.005, 5, 'log2', 6, 500]
10|0.835570(std:0.035535)|[0.007, 4, 'log2', 4, 400]
10|0.835570(std:0.030321)|[0.007, 5, 'sqrt', 5, 300]
10|0.835570(std:0.032503)|[0.007, 5, 'log2', 2, 300]
10|0.835570(std:0.029937)|[0.007, 5, 'log2', 5, 300]
10|0.835570(std:0.031983)|[0.007, 5, 'log2', 6, 400]
10|0.835570(std:0.038453)|[0.01, 4, 'log2', 6, 400]
10|0.835570(std:0.033779)|[0.01, 5, 'sqrt', 2, 200]
10|0.835570(std:0.032503)|[0.01, 5, 'log2', 6, 200]



## 8 GradientBoostingClassifier

del Name_Len, Ticket_Len

0.74641
->



- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band


best parameters: {'learning_rate': 0.1, 'max_depth': 4, 'max_features': 'log2', 'min_samples_split': 5, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.823728813559322
confusion matrix:  [[155  20]
 [ 32  88]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.032683)|[0.1, 4, 'log2', 5, 50]
1|0.838926(std:0.025813)|[0.2, 5, 'sqrt', 2, 10]
3|0.837248(std:0.036250)|[0.01, 5, 'log2', 6, 200]
3|0.837248(std:0.036250)|[0.05, 4, 'log2', 3, 50]
3|0.837248(std:0.035011)|[0.2, 4, 'log2', 2, 50]
6|0.835570(std:0.037786)|[0.007, 4, 'log2', 5, 400]
6|0.835570(std:0.036091)|[0.02, 5, 'log2', 3, 100]
6|0.835570(std:0.039745)|[0.1, 4, 'sqrt', 4, 50]
6|0.835570(std:0.023415)|[0.1, 5, 'log2', 6, 50]
6|0.835570(std:0.038305)|[0.2, 4, 'sqrt', 6, 10]



## 9 GradientBoostingClassifier

keep all family feature

**not good**



- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [x] parch,sib
  - [x] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band



best parameters: {'learning_rate': 0.2, 'max_depth': 5, 'max_features': 'sqrt', 'min_samples_split': 6, 'n_estimators': 10}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.8169491525423729
confusion matrix:  [[154  21]
 [ 33  87]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.033381)|[0.2, 5, 'sqrt', 6, 10]
2|0.835570(std:0.038600)|[0.02, 4, 'log2', 2, 100]
3|0.832215(std:0.013889)|[0.005, 6, 'log2', 5, 200]
3|0.832215(std:0.015007)|[0.007, 7, 'log2', 6, 100]
3|0.832215(std:0.026738)|[0.01, 5, 'sqrt', 4, 100]
3|0.832215(std:0.031944)|[0.2, 4, 'log2', 3, 10]
7|0.830537(std:0.030607)|[0.005, 5, 'log2', 4, 300]
7|0.830537(std:0.019537)|[0.005, 6, 'log2', 4, 200]
7|0.830537(std:0.023661)|[0.01, 5, 'log2', 2, 100]
7|0.830537(std:0.027483)|[0.02, 4, 'sqrt', 4, 100]
7|0.830537(std:0.023549)|[0.2, 5, 'sqrt', 3, 10]
7|0.830537(std:0.041031)|[0.2, 5, 'log2', 3, 10]
7|0.830537(std:0.026733)|[0.2, 5, 'log2', 4, 7]






## 10 GradientBoostingClassifier

only familysize


- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [x] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band







best parameters: {'learning_rate': 0.1, 'max_depth': 3, 'max_features': 'log2', 'min_samples_split': 3, 'n_estimators': 100}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.823728813559322
confusion matrix:  [[155  20]
 [ 32  88]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.034610)|[0.1, 3, 'log2', 3, 100]
2|0.837248(std:0.032162)|[0.1, 6, 'log2', 6, 10]
3|0.835570(std:0.033386)|[0.005, 4, 'log2', 4, 500]
3|0.835570(std:0.045235)|[0.007, 3, 'log2', 6, 500]
3|0.835570(std:0.031270)|[0.007, 4, 'sqrt', 3, 300]
3|0.835570(std:0.043504)|[0.01, 3, 'log2', 2, 400]
3|0.835570(std:0.042988)|[0.01, 3, 'log2', 3, 400]
3|0.835570(std:0.039821)|[0.01, 3, 'log2', 5, 400]
3|0.835570(std:0.037713)|[0.01, 4, 'sqrt', 5, 200]
3|0.835570(std:0.035776)|[0.05, 4, 'log2', 6, 50]
3|0.835570(std:0.039695)|[0.2, 4, 'sqrt', 6, 7]
3|0.835570(std:0.027061)|[0.2, 6, 'sqrt', 3, 10]



## 11 GradientBoostingClassifier


activate Name_Len, Cabin_Num


- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [x] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [x] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band



best parameters: {'learning_rate': 0.007, 'max_depth': 4, 'max_features': 'log2', 'min_samples_split': 6, 'n_estimators': 400}
Mean cross-validated score of the best_estimator:  0.8456375838926175
test:  0.8271186440677966
confusion matrix:  [[156  19]
 [ 32  88]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.845638(std:0.040610)|[0.007, 4, 'log2', 6, 400]
2|0.843960(std:0.037780)|[0.007, 4, 'log2', 3, 400]
2|0.843960(std:0.036237)|[0.01, 5, 'log2', 6, 200]
2|0.843960(std:0.044345)|[0.05, 4, 'log2', 3, 50]
5|0.842282(std:0.039675)|[0.005, 4, 'log2', 4, 500]
6|0.840604(std:0.042189)|[0.005, 4, 'sqrt', 2, 500]
6|0.840604(std:0.042669)|[0.005, 5, 'log2', 5, 400]
6|0.840604(std:0.035105)|[0.007, 4, 'sqrt', 3, 300]
6|0.840604(std:0.036326)|[0.007, 4, 'sqrt', 6, 400]
6|0.840604(std:0.040684)|[0.007, 4, 'log2', 5, 400]
6|0.840604(std:0.042787)|[0.01, 4, 'sqrt', 5, 200]
6|0.840604(std:0.036326)|[0.01, 4, 'log2', 5, 300]




# 12 random forest

0.79425


- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [x] parch,sib
  - [x] isalone
- embarked
  - [ ] integer encoding
  - [x] one hot encoding
- Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [x] Name_Len
- [ ] Ticket_Len
- Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [x] one hot encoding
- [x] Age*Class
- [x] FareBand
  - [x] 4 band


## eval model

best parameters: {'randomforestclassifier__max_depth': 7, 'randomforestclassifier__max_features': 'sqrt', 'randomforestclassifier__min_samples_split': 8, 'randomforestclassifier__n_estimators': 60}
Mean cross-validated score of the best_estimator:  0.8422818791946308
test:  0.8406779661016949
confusion matrix:  [[159  16]
 [ 31  89]]

Rank|Score(std)|Params ['randomforestclassifier__max_depth', 'randomforestclassifier__max_features', 'randomforestclassifier__min_samples_split', 'randomforestclassifier__n_estimators']
1|0.842282(std:0.037699)|[7, 'sqrt', 8, 60]
2|0.838926(std:0.039486)|[6, 'log2', 6, 20]
2|0.838926(std:0.037935)|[6, 'log2', 7, 300]
2|0.838926(std:0.033637)|[7, 'sqrt', 9, 200]
2|0.838926(std:0.025510)|[7, 'log2', 4, 50]
2|0.838926(std:0.031249)|[7, 'log2', 9, 700]
2|0.838926(std:0.030510)|[9, 'sqrt', 9, 200]
8|0.837248(std:0.036467)|[5, 'sqrt', 5, 50]
8|0.837248(std:0.036250)|[6, 'sqrt', 6, 700]
8|0.837248(std:0.032517)|[6, 'sqrt', 9, 100]
8|0.837248(std:0.033792)|[6, 'log2', 4, 30]
8|0.837248(std:0.036250)|[6, 'log2', 4, 700]
8|0.837248(std:0.027113)|[6, 'log2', 5, 30]
8|0.837248(std:0.028384)|[7, 'sqrt', 6, 40]
8|0.837248(std:0.034560)|[7, 'sqrt', 6, 500]
8|0.837248(std:0.033104)|[7, 'sqrt', 8, 200]
8|0.837248(std:0.034636)|[7, 'sqrt', 8, 500]
8|0.837248(std:0.032517)|[7, 'sqrt', 9, 300]
8|0.837248(std:0.041304)|[7, 'log2', 7, 40]
8|0.837248(std:0.032162)|[7, 'log2', 7, 300]
8|0.837248(std:0.032162)|[7, 'log2', 8, 300]
8|0.837248(std:0.037020)|[7, 'log2', 8, 500]
8|0.837248(std:0.022276)|[8, 1, 3, 100]
8|0.837248(std:0.024014)|[8, 'sqrt', 4, 20]
8|0.837248(std:0.033792)|[8, 'sqrt', 7, 40]


## submission

best parameters: {'randomforestclassifier__max_depth': 8, 'randomforestclassifier__max_features': 'log2', 'randomforestclassifier__min_samples_split': 3, 'randomforestclassifier__n_estimators': 10}
Mean cross-validated score of the best_estimator:  0.8417508417508418
Rank|Score(std)|Params ['randomforestclassifier__max_depth', 'randomforestclassifier__max_features', 'randomforestclassifier__min_samples_split', 'randomforestclassifier__n_estimators']
1|0.841751(std:0.023075)|[8, 'log2', 3, 10]
2|0.840629(std:0.018609)|[8, 1, 6, 50]
3|0.839506(std:0.030570)|[8, 1, 5, 60]
3|0.839506(std:0.029845)|[9, 1, 9, 60]
5|0.838384(std:0.026129)|[7, 1, 5, 40]
5|0.838384(std:0.037062)|[7, 1, 9, 300]
5|0.838384(std:0.032934)|[8, 1, 9, 50]
8|0.837262(std:0.025256)|[9, 1, 6, 100]
9|0.836139(std:0.023981)|[7, 'sqrt', 3, 50]
9|0.836139(std:0.009261)|[8, 1, 9, 100]
9|0.836139(std:0.017224)|[8, 'sqrt', 8, 60]
9|0.836139(std:0.024330)|[9, 1, 9, 100]





# 13 random forest

reduce so many features except very important features

almost no effect to score. 
it means these features are not so important...


- age
  - [x] 5 age band
  - [ ] 10 age band
- [ ] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [ ] embarked
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [ ] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- [x] Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- [ ] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Age*Class
- [x] Fare
  - [x] 4 band




## eval model



## submission



# 14 gradient boosting

Add Family_Survival feature

Age 	FamilySize 	Family_Survival 	Fare 	PassengerId 	Pclass 	Sex


0.81339
by gradient boosting

- age
  - [x] 5 age band
  - [ ] 10 age band
- [ ] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [ ] embarked
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [ ] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- [ ] Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- [ ] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Age*Class
- [x] Fare
  - [x] 4 band
- [x] Family_Survival




## eval model

### SVC, robust

**First time to get a score higher than 0.86 !!**

best parameters: {'svc__C': 100, 'svc__gamma': 0.05}
Mean cross-validated score of the best_estimator:  0.8355704697986577
test:  0.864406779661017
confusion matrix:  [[165  10]
 [ 30  90]]

Rank|Score(std)|Params ['svc__C', 'svc__gamma']
1|0.835570(std:0.043700)|[100, 0.05]
1|0.835570(std:0.045218)|[500, 0.03]
3|0.832215(std:0.044323)|[50, 0.04]
3|0.832215(std:0.041167)|[80, 0.05]
3|0.832215(std:0.044323)|[90, 0.03]
3|0.832215(std:0.041167)|[90, 0.05]
3|0.832215(std:0.039307)|[1000, 0.01]
8|0.830537(std:0.042918)|[10, 0.1]
8|0.830537(std:0.044461)|[30, 0.05]
8|0.830537(std:0.042918)|[70, 0.05]
8|0.830537(std:0.044461)|[90, 0.04]
8|0.830537(std:0.046558)|[100, 0.03]
8|0.830537(std:0.044461)|[100, 0.04]
8|0.830537(std:0.039462)|[500, 0.01]
8|0.830537(std:0.039462)|[1000, 0.008]



### svc, standard scaler

**score was 0.87.. so high**

submit score was 0.80861


best parameters: {'svc__C': 10, 'svc__gamma': 0.04}
Mean cross-validated score of the best_estimator:  0.8322147651006712
test:  0.8711864406779661
confusion matrix:  [[167   8]
 [ 30  90]]

Rank|Score(std)|Params ['svc__C', 'svc__gamma']
1|0.832215(std:0.044375)|[10, 0.04]
2|0.828859(std:0.038708)|[1, 0.1]
2|0.828859(std:0.042616)|[30, 0.03]
2|0.828859(std:0.038755)|[30, 0.05]
2|0.828859(std:0.025254)|[70, 0.1]
2|0.828859(std:0.037744)|[500, 0.01]
2|0.828859(std:0.040311)|[1000, 0.008]
8|0.827181(std:0.040471)|[50, 0.04]
8|0.827181(std:0.024540)|[50, 0.1]
8|0.827181(std:0.038744)|[80, 0.03]
8|0.827181(std:0.042261)|[90, 0.03]
8|0.827181(std:0.042261)|[100, 0.03]
8|0.827181(std:0.042261)|[1000, 0.01]



### random forest


best parameters: {'randomforestclassifier__max_depth': 8, 'randomforestclassifier__max_features': 'sqrt', 'randomforestclassifier__min_samples_split': 4, 'randomforestclassifier__n_estimators': 30}
Mean cross-validated score of the best_estimator:  0.8406040268456376
test:  0.8406779661016949
confusion matrix:  [[160  15]
 [ 32  88]]

Rank|Score(std)|Params ['randomforestclassifier__max_depth', 'randomforestclassifier__max_features', 'randomforestclassifier__min_samples_split', 'randomforestclassifier__n_estimators']
1|0.840604(std:0.026401)|[8, 'sqrt', 4, 30]
2|0.838926(std:0.035513)|[5, 'sqrt', 3, 50]
2|0.838926(std:0.030419)|[7, 1, 6, 300]
2|0.838926(std:0.030419)|[7, 'log2', 9, 50]
5|0.837248(std:0.045751)|[6, 'log2', 4, 30]
5|0.837248(std:0.028062)|[7, 1, 3, 200]
5|0.837248(std:0.023744)|[7, 'log2', 5, 60]
5|0.837248(std:0.023256)|[7, 'log2', 6, 30]
5|0.837248(std:0.027005)|[8, 'sqrt', 6, 20]
5|0.837248(std:0.038761)|[8, 'sqrt', 9, 20]


variable 	importance
5 	Sex 	0.399386
2 	Family_Survival 	0.141263
4 	Pclass 	0.135416
1 	FamilySize 	0.125451
0 	Age 	0.105186
3 	Fare 	0.093299

**this is not so high result...why...**
but apparently Family_Survival is important feature.



### gradient boosting

best parameters: {'learning_rate': 0.02, 'max_depth': 4, 'max_features': 'log2', 'min_samples_split': 4, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8389261744966443
test:  0.847457627118644
confusion matrix:  [[163  12]
 [ 33  87]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.838926(std:0.023766)|[0.02, 4, 'log2', 4, 300]
1|0.838926(std:0.039294)|[0.1, 3, 'log2', 2, 50]
3|0.837248(std:0.036746)|[0.02, 3, 'sqrt', 3, 300]
3|0.837248(std:0.021329)|[0.02, 4, 'log2', 2, 300]
3|0.837248(std:0.043168)|[0.1, 3, 'log2', 4, 50]
6|0.835570(std:0.042747)|[0.007, 3, 'sqrt', 6, 500]
6|0.835570(std:0.019167)|[0.007, 5, 'sqrt', 5, 400]
6|0.835570(std:0.019167)|[0.007, 5, 'log2', 4, 400]
6|0.835570(std:0.042747)|[0.01, 3, 'sqrt', 3, 400]
6|0.835570(std:0.037892)|[0.01, 3, 'sqrt', 3, 500]
6|0.835570(std:0.042747)|[0.01, 3, 'sqrt', 4, 500]
6|0.835570(std:0.042747)|[0.01, 3, 'sqrt', 6, 400]
6|0.835570(std:0.037892)|[0.01, 3, 'log2', 3, 500]
6|0.835570(std:0.037892)|[0.01, 3, 'log2', 6, 500]
6|0.835570(std:0.028545)|[0.01, 4, 'sqrt', 6, 500]
6|0.835570(std:0.028545)|[0.01, 4, 'log2', 2, 500]
6|0.835570(std:0.028545)|[0.01, 4, 'log2', 3, 500]
6|0.835570(std:0.030142)|[0.01, 5, 'sqrt', 2, 400]
6|0.835570(std:0.019167)|[0.01, 5, 'sqrt', 4, 300]
6|0.835570(std:0.042747)|[0.02, 3, 'sqrt', 4, 200]
6|0.835570(std:0.042747)|[0.02, 3, 'log2', 2, 200]
6|0.835570(std:0.042747)|[0.02, 3, 'log2', 6, 200]
6|0.835570(std:0.037892)|[0.05, 3, 'sqrt', 2, 100]
6|0.835570(std:0.037892)|[0.05, 3, 'sqrt', 3, 100]
6|0.835570(std:0.040449)|[0.05, 3, 'log2', 5, 100]
6|0.835570(std:0.033533)|[0.05, 4, 'sqrt', 6, 100]
6|0.835570(std:0.017753)|[0.05, 4, 'log2', 6, 100]
6|0.835570(std:0.037892)|[0.1, 3, 'sqrt', 3, 50]



## submission

### gradient boosting

best parameters: {'learning_rate': 0.005, 'max_depth': 4, 'max_features': None, 'min_samples_split': 2, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8507295173961841
Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.850730(std:0.021999)|[0.005, 4, None, 2, 300]
1|0.850730(std:0.021999)|[0.005, 4, None, 3, 300]
1|0.850730(std:0.021999)|[0.005, 4, None, 4, 300]
1|0.850730(std:0.021999)|[0.005, 4, None, 5, 300]
1|0.850730(std:0.021999)|[0.005, 4, None, 6, 300]
1|0.850730(std:0.020023)|[0.02, 5, 'sqrt', 2, 50]
1|0.850730(std:0.018184)|[0.1, 6, 'sqrt', 5, 7]
1|0.850730(std:0.016036)|[0.1, 6, 'sqrt', 6, 10]
1|0.850730(std:0.016475)|[0.1, 7, 'log2', 4, 7]
10|0.849607(std:0.021661)|[0.005, 3, None, 2, 200]
10|0.849607(std:0.021661)|[0.005, 3, None, 2, 300]
10|0.849607(std:0.021661)|[0.005, 3, None, 2, 400]
10|0.849607(std:0.021661)|[0.005, 3, None, 3, 200]
10|0.849607(std:0.021661)|[0.005, 3, None, 3, 300]
10|0.849607(std:0.021661)|[0.005, 3, None, 3, 400]
10|0.849607(std:0.021661)|[0.005, 3, None, 4, 200]
10|0.849607(std:0.021661)|[0.005, 3, None, 4, 300]
10|0.849607(std:0.021661)|[0.005, 3, None, 4, 400]
10|0.849607(std:0.021661)|[0.005, 3, None, 5, 200]
10|0.849607(std:0.021661)|[0.005, 3, None, 5, 300]
10|0.849607(std:0.021661)|[0.005, 3, None, 5, 400]
10|0.849607(std:0.021661)|[0.005, 3, None, 6, 200]
10|0.849607(std:0.021661)|[0.005, 3, None, 6, 300]
10|0.849607(std:0.021661)|[0.005, 3, None, 6, 400]
10|0.849607(std:0.020426)|[0.005, 3, 'log2', 3, 400]
10|0.849607(std:0.021661)|[0.005, 4, None, 2, 200]
10|0.849607(std:0.021661)|[0.005, 4, None, 3, 200]
10|0.849607(std:0.021661)|[0.005, 4, None, 4, 200]
10|0.849607(std:0.021661)|[0.005, 4, None, 5, 200]
10|0.849607(std:0.021661)|[0.005, 4, None, 6, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 2, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 2, 300]
10|0.849607(std:0.021661)|[0.007, 3, None, 3, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 3, 300]
10|0.849607(std:0.021661)|[0.007, 3, None, 4, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 4, 300]
10|0.849607(std:0.021661)|[0.007, 3, None, 5, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 5, 300]
10|0.849607(std:0.021661)|[0.007, 3, None, 6, 200]
10|0.849607(std:0.021661)|[0.007, 3, None, 6, 300]
10|0.849607(std:0.020426)|[0.007, 3, 'log2', 6, 300]
10|0.849607(std:0.021661)|[0.007, 4, None, 2, 200]
10|0.849607(std:0.021661)|[0.007, 4, None, 3, 200]
10|0.849607(std:0.021661)|[0.007, 4, None, 4, 200]
10|0.849607(std:0.021661)|[0.007, 4, None, 5, 200]
10|0.849607(std:0.021661)|[0.007, 4, None, 6, 200]
10|0.849607(std:0.021661)|[0.01, 3, None, 2, 100]
10|0.849607(std:0.021661)|[0.01, 3, None, 3, 100]
10|0.849607(std:0.021661)|[0.01, 3, None, 3, 200]
10|0.849607(std:0.021661)|[0.01, 3, None, 4, 100]
10|0.849607(std:0.021661)|[0.01, 3, None, 4, 200]
10|0.849607(std:0.021661)|[0.01, 3, None, 5, 100]
10|0.849607(std:0.021661)|[0.01, 3, None, 6, 100]
10|0.849607(std:0.021661)|[0.01, 3, None, 6, 200]
10|0.849607(std:0.020426)|[0.01, 3, 'sqrt', 6, 200]
10|0.849607(std:0.020426)|[0.01, 3, 'log2', 3, 200]
10|0.849607(std:0.021661)|[0.01, 4, None, 2, 100]
10|0.849607(std:0.021661)|[0.01, 4, None, 3, 100]
10|0.849607(std:0.021661)|[0.01, 4, None, 4, 100]
10|0.849607(std:0.021661)|[0.01, 4, None, 5, 100]
10|0.849607(std:0.021661)|[0.01, 4, None, 6, 100]
10|0.849607(std:0.021661)|[0.02, 3, None, 2, 50]
10|0.849607(std:0.021661)|[0.02, 3, None, 3, 50]
10|0.849607(std:0.021661)|[0.02, 3, None, 4, 50]
10|0.849607(std:0.021661)|[0.02, 3, None, 5, 50]
10|0.849607(std:0.021661)|[0.02, 3, None, 6, 50]
10|0.849607(std:0.021661)|[0.02, 3, None, 6, 100]
10|0.849607(std:0.020426)|[0.02, 3, 'sqrt', 4, 100]
10|0.849607(std:0.021661)|[0.02, 4, None, 2, 50]
10|0.849607(std:0.021661)|[0.02, 4, None, 3, 50]
10|0.849607(std:0.021661)|[0.02, 4, None, 4, 50]
10|0.849607(std:0.021661)|[0.02, 4, None, 5, 50]
10|0.849607(std:0.021661)|[0.02, 4, None, 6, 50]
10|0.849607(std:0.021661)|[0.1, 3, None, 2, 10]
10|0.849607(std:0.021661)|[0.1, 3, None, 3, 10]
10|0.849607(std:0.021661)|[0.1, 3, None, 4, 10]
10|0.849607(std:0.021661)|[0.1, 3, None, 5, 10]
10|0.849607(std:0.021661)|[0.1, 3, None, 6, 10]
10|0.849607(std:0.021661)|[0.1, 4, None, 2, 10]
10|0.849607(std:0.021661)|[0.1, 4, None, 3, 10]
10|0.849607(std:0.021661)|[0.1, 4, None, 4, 10]
10|0.849607(std:0.021661)|[0.1, 4, None, 5, 10]
10|0.849607(std:0.021661)|[0.1, 4, None, 6, 10]
10|0.849607(std:0.021661)|[0.2, 3, None, 2, 7]
10|0.849607(std:0.021661)|[0.2, 3, None, 2, 10]
10|0.849607(std:0.021661)|[0.2, 3, None, 3, 7]
10|0.849607(std:0.021661)|[0.2, 3, None, 3, 10]
10|0.849607(std:0.021661)|[0.2, 3, None, 4, 7]
10|0.849607(std:0.021661)|[0.2, 3, None, 4, 10]
10|0.849607(std:0.021661)|[0.2, 3, None, 5, 7]
10|0.849607(std:0.021661)|[0.2, 3, None, 5, 10]
10|0.849607(std:0.021661)|[0.2, 3, None, 6, 7]
10|0.849607(std:0.021661)|[0.2, 3, None, 6, 10]
10|0.849607(std:0.020426)|[0.2, 4, None, 2, 7]
10|0.849607(std:0.020426)|[0.2, 4, None, 3, 7]
10|0.849607(std:0.020426)|[0.2, 4, None, 4, 7]
10|0.849607(std:0.020426)|[0.2, 4, None, 5, 7]
10|0.849607(std:0.020426)|[0.2, 4, None, 6, 7]
10|0.849607(std:0.018378)|[0.2, 4, 'log2', 5, 7]




# 15 gradient boosting

activate other features


0.81339
by gradient boosting
Age 	FamilySize 	Family_Survival 	Fare 	PassengerId 	Pclass 	Sex

->
'Age', 'Age*Class', 'Age_Null_Flag', 'Cabin_Letter_0', 'Cabin_Letter_A',
       'Cabin_Letter_B', 'Cabin_Letter_C', 'Cabin_Letter_D', 'Cabin_Letter_E',
       'Cabin_Letter_F', 'Cabin_Letter_G', 'Cabin_Letter_T', 'Cabin_num_0.0',
       'Cabin_num_1.0', 'Cabin_num_2.0', 'Cabin_num_nan', 'FamilySize',
       'Family_Survival', 'Fare', 'Name_Len', 'Pclass', 'Sex', 'Survived',
       'Ticket_Len', 'Title_Dr', 'Title_Master', 'Title_Miss', 'Title_Mr',
       'Title_Mrs', 'Title_Rev', 'Embarked_C', 'Embarked_Q', 'Embarked_S'

0.78947


- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [x] embarked
  - [ ] integer encoding
  - [x] one hot encoding
- [x] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [x] Name_Len
- [x] Ticket_Len
- [x] Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- [x] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [x] one hot encoding
- [x] Age*Class
- [x] Fare
  - [x] 4 band
- [x] Family_Survival




## eval model



best parameters: {'learning_rate': 0.1, 'max_depth': 3, 'max_features': None, 'min_samples_split': 2, 'n_estimators': 200}
Mean cross-validated score of the best_estimator:  0.860738255033557
test:  0.8542372881355932
confusion matrix:  [[158  17]
 [ 26  94]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.860738(std:0.048862)|[0.1, 3, None, 2, 200]
1|0.860738(std:0.049096)|[0.1, 3, None, 3, 200]
3|0.859060(std:0.038004)|[0.01, 4, 'log2', 3, 400]
3|0.859060(std:0.025102)|[0.05, 4, 'sqrt', 5, 500]
5|0.857383(std:0.043999)|[0.05, 3, None, 6, 300]
5|0.857383(std:0.021381)|[0.05, 4, 'log2', 3, 400]
5|0.857383(std:0.027790)|[0.1, 3, 'log2', 3, 300]
8|0.855705(std:0.036478)|[0.01, 4, 'sqrt', 4, 400]
8|0.855705(std:0.046402)|[0.05, 3, None, 5, 400]
8|0.855705(std:0.048074)|[0.05, 3, None, 5, 500]
8|0.855705(std:0.024054)|[0.05, 4, 'sqrt', 4, 400]
8|0.855705(std:0.029726)|[0.05, 4, 'log2', 2, 400]
8|0.855705(std:0.049233)|[0.1, 3, None, 5, 300]
8|0.855705(std:0.042498)|[0.1, 3, None, 5, 400]
8|0.855705(std:0.039038)|[0.1, 3, None, 6, 300]


variable 	importance
19 	Name_Len 	0.262546
22 	Ticket_Len 	0.150992
17 	Family_Survival 	0.063495
16 	FamilySize 	0.060235
18 	Fare 	0.054798
0 	Age 	0.046717
1 	Age*Class 	0.045358
21 	Sex 	0.036591
26 	Title_Mr 	0.035357
24 	Title_Master 	0.034175
6 	Cabin_Letter_C 	0.028984
12 	Cabin_num_0.0 	0.026444
20 	Pclass 	0.023445
2 	Age_Null_Flag 	0.019910
27 	Title_Mrs 	0.017638
23 	Title_Dr 	0.014275
31 	Embarked_S 	0.011359
28 	Title_Rev 	0.011230
8 	Cabin_Letter_E 	0.009773
7 	Cabin_Letter_D 	0.009052
5 	Cabin_Letter_B 	0.008060
13 	Cabin_num_1.0 	0.007347
29 	Embarked_C 	0.005631
25 	Title_Miss 	0.004526
15 	Cabin_num_nan 	0.003047
14 	Cabin_num_2.0 	0.002296
30 	Embarked_Q 	0.002040
3 	Cabin_Letter_0 	0.001984
10 	Cabin_Letter_G 	0.001490
4 	Cabin_Letter_A 	0.001207
11 	Cabin_Letter_T 	0.000000
9 	Cabin_Letter_F 	0.000000



------------------------------------------------------------------------------------------------------

# 16 gradient boosting

from my best score's feature, activate some other features


0.81339
by gradient boosting
Age 	FamilySize 	Family_Survival 	Fare 	PassengerId 	Pclass 	Sex

->
0.80861

'Age', 'Age*Class', 'Cabin_Letter_0', 'Cabin_Letter_A',
       'Cabin_Letter_B', 'Cabin_Letter_C', 'Cabin_Letter_D', 'Cabin_Letter_E',
       'Cabin_Letter_F', 'Cabin_Letter_G', 'Cabin_Letter_T', 'FamilySize',
       'Family_Survival', 'Fare', 'Pclass', 'Sex', 'Survived', 'Title_Dr',
       'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'Title_Rev'
       
       
       

- age
  - [x] 5 age band
  - [ ] 10 age band
- [x] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [ ] embarked
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- [x] Cabin_Letter
  - [ ] integer encoding
  - [x] one hot encoding
- [ ] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] Fare
  - [x] 4 band
- [x] Family_Survival




## eval model




best parameters: {'learning_rate': 0.01, 'max_depth': 7, 'max_features': 'sqrt', 'min_samples_split': 5, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8691275167785235
test:  0.8508474576271187
confusion matrix:  [[159  16]
 [ 28  92]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.869128(std:0.032851)|[0.01, 7, 'sqrt', 5, 300]
2|0.867450(std:0.032914)|[0.02, 6, 'log2', 5, 200]
3|0.865772(std:0.028552)|[0.007, 7, 'sqrt', 5, 400]
3|0.865772(std:0.030768)|[0.01, 7, 'sqrt', 6, 400]
3|0.865772(std:0.028552)|[0.01, 7, 'log2', 4, 300]
3|0.865772(std:0.029077)|[0.02, 5, 'log2', 3, 400]
3|0.865772(std:0.030358)|[0.1, 6, 'sqrt', 6, 50]
3|0.865772(std:0.025021)|[0.2, 4, 'sqrt', 4, 100]
9|0.864094(std:0.033065)|[0.005, 6, 'sqrt', 6, 400]
9|0.864094(std:0.030492)|[0.007, 7, 'log2', 5, 400]
9|0.864094(std:0.030492)|[0.007, 7, 'log2', 5, 500]




variable 	importance
12 	Family_Survival 	0.140182
11 	FamilySize 	0.110453
15 	Sex 	0.109319
19 	Title_Mr 	0.108352
1 	Age*Class 	0.089542
13 	Fare 	0.087858
14 	Pclass 	0.075205
0 	Age 	0.070104
20 	Title_Mrs 	0.047357
18 	Title_Miss 	0.033210
2 	Cabin_Letter_0 	0.029603
7 	Cabin_Letter_E 	0.022340
5 	Cabin_Letter_C 	0.015174
4 	Cabin_Letter_B 	0.014316
6 	Cabin_Letter_D 	0.013123
17 	Title_Master 	0.012666
21 	Title_Rev 	0.005642
16 	Title_Dr 	0.005506
3 	Cabin_Letter_A 	0.004217
9 	Cabin_Letter_G 	0.002709
8 	Cabin_Letter_F 	0.002143
10 	Cabin_Letter_T 	0.000979




## submission

best parameters: {'learning_rate': 0.1, 'max_depth': 3, 'max_features': 'log2', 'min_samples_split': 4, 'n_estimators': 50}
Mean cross-validated score of the best_estimator:  0.8619528619528619
Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.861953(std:0.019079)|[0.1, 3, 'log2', 4, 50]
2|0.860831(std:0.018977)|[0.02, 4, 'log2', 2, 200]
3|0.859708(std:0.014470)|[0.02, 3, 'sqrt', 6, 400]
3|0.859708(std:0.023592)|[0.02, 7, 'log2', 6, 400]
3|0.859708(std:0.018845)|[0.2, 3, 'sqrt', 4, 50]
3|0.859708(std:0.030924)|[0.2, 3, 'sqrt', 6, 500]
3|0.859708(std:0.026440)|[0.2, 4, 'sqrt', 4, 200]
8|0.858586(std:0.018607)|[0.01, 4, 'log2', 2, 500]
8|0.858586(std:0.020222)|[0.01, 4, 'log2', 4, 500]
8|0.858586(std:0.019454)|[0.02, 3, 'sqrt', 5, 300]
8|0.858586(std:0.018020)|[0.05, 3, 'sqrt', 5, 200]
8|0.858586(std:0.029469)|[0.05, 5, 'sqrt', 5, 400]
8|0.858586(std:0.025569)|[0.2, 4, 'log2', 6, 200]


variable 	importance
12 	Family_Survival 	0.196397
19 	Title_Mr 	0.122763
15 	Sex 	0.114981
14 	Pclass 	0.102806
11 	FamilySize 	0.073945
20 	Title_Mrs 	0.068186
1 	Age*Class 	0.058663
18 	Title_Miss 	0.035862
13 	Fare 	0.034717
17 	Title_Master 	0.031685
21 	Title_Rev 	0.029663
2 	Cabin_Letter_0 	0.029327
0 	Age 	0.028851
7 	Cabin_Letter_E 	0.022412
6 	Cabin_Letter_D 	0.016429
5 	Cabin_Letter_C 	0.010170
16 	Title_Dr 	0.007173
3 	Cabin_Letter_A 	0.007032
9 	Cabin_Letter_G 	0.003673
10 	Cabin_Letter_T 	0.002045
8 	Cabin_Letter_F 	0.001939
4 	Cabin_Letter_B 	0.001281



------------------------------------------------------------------------------------------------------



# 17 gradient boosting

from my best score's feature, activate some other features

only Title and Age*Class was activated

0.81339
by gradient boosting
Age 	FamilySize 	Family_Survival 	Fare 	PassengerId 	Pclass 	Sex

->



- age
  - [x] 5 age band
  - [ ] 10 age band
- [ ] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [ ] embarked
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [x] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- [ ] Cabin_Letter
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] Fare
  - [x] 4 band
- [x] Family_Survival




## eval model

best parameters: {'learning_rate': 0.01, 'max_depth': 6, 'max_features': 'sqrt', 'min_samples_split': 4, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8506711409395973
test:  0.847457627118644
confusion matrix:  [[160  15]
 [ 30  90]]

Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.850671(std:0.033308)|[0.01, 6, 'sqrt', 4, 300]
1|0.850671(std:0.030291)|[0.01, 6, 'sqrt', 6, 300]
1|0.850671(std:0.033308)|[0.01, 6, 'log2', 5, 300]
1|0.850671(std:0.029288)|[0.05, 6, 'sqrt', 6, 50]
5|0.848993(std:0.031904)|[0.007, 6, 'log2', 2, 400]
5|0.848993(std:0.039840)|[0.02, 5, 'log2', 3, 100]
5|0.848993(std:0.031796)|[0.02, 7, 'log2', 5, 100]
5|0.848993(std:0.028620)|[0.05, 6, 'sqrt', 5, 50]
5|0.848993(std:0.028620)|[0.05, 6, 'log2', 5, 50]
10|0.847315(std:0.032691)|[0.005, 5, 'sqrt', 3, 300]
10|0.847315(std:0.044367)|[0.005, 5, 'sqrt', 5, 400]
10|0.847315(std:0.032691)|[0.005, 5, 'log2', 3, 300]
10|0.847315(std:0.036017)|[0.005, 5, 'log2', 3, 400]
10|0.847315(std:0.032691)|[0.005, 5, 'log2', 4, 300]
10|0.847315(std:0.028982)|[0.005, 6, 'log2', 6, 400]
10|0.847315(std:0.032257)|[0.007, 5, 'sqrt', 2, 300]
10|0.847315(std:0.032691)|[0.007, 5, 'log2', 2, 200]
10|0.847315(std:0.032691)|[0.007, 5, 'log2', 3, 200]
10|0.847315(std:0.036017)|[0.007, 5, 'log2', 3, 300]
10|0.847315(std:0.032257)|[0.007, 6, 'sqrt', 2, 200]
10|0.847315(std:0.026270)|[0.007, 6, 'log2', 5, 500]
10|0.847315(std:0.028982)|[0.01, 5, 'sqrt', 2, 200]
10|0.847315(std:0.032257)|[0.01, 5, 'sqrt', 2, 300]
10|0.847315(std:0.036017)|[0.01, 5, 'sqrt', 4, 200]
10|0.847315(std:0.032257)|[0.01, 5, 'log2', 2, 300]
10|0.847315(std:0.036017)|[0.01, 5, 'log2', 4, 200]
10|0.847315(std:0.030576)|[0.01, 5, 'log2', 6, 500]
10|0.847315(std:0.033040)|[0.01, 6, 'sqrt', 5, 200]
10|0.847315(std:0.030229)|[0.01, 6, 'log2', 3, 300]
10|0.847315(std:0.026869)|[0.01, 6, 'log2', 4, 300]
10|0.847315(std:0.028338)|[0.01, 6, 'log2', 6, 300]
10|0.847315(std:0.030229)|[0.05, 7, 'log2', 6, 50]
10|0.847315(std:0.027157)|[0.1, 3, 'sqrt', 6, 10]
10|0.847315(std:0.036334)|[0.2, 4, 'sqrt', 2, 50]
10|0.847315(std:0.033615)|[0.2, 7, 'sqrt', 3, 10]

variable 	importance
3 	Family_Survival 	0.156077
10 	Title_Mr 	0.134597
2 	FamilySize 	0.124868
6 	Sex 	0.120565
1 	Age*Class 	0.101800
5 	Pclass 	0.100482
4 	Fare 	0.096184
0 	Age 	0.058360
11 	Title_Mrs 	0.045163
9 	Title_Miss 	0.036238
8 	Title_Master 	0.013085
12 	Title_Rev 	0.006587
7 	Title_Dr 	0.005995



## submission


best parameters: {'learning_rate': 0.005, 'max_depth': 4, 'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 300}
Mean cross-validated score of the best_estimator:  0.8540965207631874
Rank|Score(std)|Params ['learning_rate', 'max_depth', 'max_features', 'min_samples_split', 'n_estimators']
1|0.854097(std:0.019683)|[0.005, 4, 'sqrt', 2, 300]
1|0.854097(std:0.019683)|[0.005, 4, 'sqrt', 3, 300]
1|0.854097(std:0.019683)|[0.005, 4, 'sqrt', 5, 300]
1|0.854097(std:0.019683)|[0.005, 4, 'log2', 2, 300]
1|0.854097(std:0.019683)|[0.005, 4, 'log2', 3, 300]
1|0.854097(std:0.019683)|[0.007, 4, 'log2', 2, 200]
1|0.854097(std:0.019683)|[0.007, 4, 'log2', 4, 200]
1|0.854097(std:0.020448)|[0.1, 4, 'sqrt', 3, 10]
1|0.854097(std:0.019683)|[0.2, 5, 'sqrt', 4, 7]
10|0.852974(std:0.018886)|[0.005, 4, 'sqrt', 4, 300]
10|0.852974(std:0.019174)|[0.005, 4, 'log2', 4, 300]
10|0.852974(std:0.018886)|[0.005, 4, 'log2', 5, 300]
10|0.852974(std:0.018886)|[0.005, 4, 'log2', 6, 300]
10|0.852974(std:0.021645)|[0.007, 4, 'sqrt', 4, 200]
10|0.852974(std:0.018886)|[0.007, 4, 'sqrt', 5, 200]
10|0.852974(std:0.018886)|[0.007, 4, 'log2', 3, 200]
10|0.852974(std:0.018798)|[0.01, 4, 'log2', 6, 200]
10|0.852974(std:0.018886)|[0.1, 4, 'log2', 6, 10]


variable 	importance
10 	Title_Mr 	0.210912
6 	Sex 	0.192913
3 	Family_Survival 	0.181704
5 	Pclass 	0.108436
1 	Age*Class 	0.063053
11 	Title_Mrs 	0.059279
2 	FamilySize 	0.058998
9 	Title_Miss 	0.041856
4 	Fare 	0.039237
0 	Age 	0.017047
8 	Title_Master 	0.014967
12 	Title_Rev 	0.009474
7 	Title_Dr 	0.002124
















------------------------------------------------------------------------------------------------------


# 17 gradient boosting

from my best score's feature, activate some other features

only Age*Class was activated

0.81339
by gradient boosting
Age 	FamilySize 	Family_Survival 	Fare 	PassengerId 	Pclass 	Sex

->



- age
  - [x] 5 age band
  - [ ] 10 age band
- [ ] Age_Null_Flag
- family
  - [x] familysize
  - [ ] parch,sib
  - [ ] isalone
- [ ] embarked
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Title
  - [ ] keep rare title and integer encoding
  - [ ] change rare title to "Rare" and integer encoding
  - [ ] change rare title to "Rare" and one hot encoding
  - [ ] change some rare title to usual title, other rare title to "Rare" and one hot encoding
- [ ] Name_Len
- [ ] Ticket_Len
- [ ] Cabin_Letter
  - [ ] integer encoding
  - [ ] one hot encoding
- [ ] Cabin_Num
  - [ ] no
  - [ ] integer encoding
  - [ ] one hot encoding
- [x] Age*Class
- [x] Fare
  - [x] 4 band
- [x] Family_Survival




## eval model

## submission





















------------------------------------------------------------------------------------------------------










## eval model

## submission

















------------------------------------------------------------------------------------------------------










## eval model

## submission














------------------------------------------------------------------------------------------------------










## eval model

## submission












------------------------------------------------------------------------------------------------------










## eval model

## submission















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
- [ ] make title numerical feature including rare titles
- [ ] try PolynomialFeatures(degree=2)
  - pipe = make_pipeline(PolynomialFeatures(degree=2), RobustScaler(), SVC())
- [ ] one hot encoding for importatnt feature, sex, pclass, title, age, 
- [ ] make Embarked_Null_Flag after checked the survived rate of null row
- [ ] make Fare_Null_Flag after checked the survived rate of null row


--------------
