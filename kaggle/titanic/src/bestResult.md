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




- [x] increase gradient boosting param : min_samples_leaf . add 4
- [ ] make ticket null
- [ ] 