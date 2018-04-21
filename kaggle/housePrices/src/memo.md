# 欠損率高いもの

	Missing Ratio
PoolQC	99.691464
MiscFeature	96.400411
Alley	93.212204
Fence	80.425094
FireplaceQu	48.680151
LotFrontage	16.660953
GarageQual	5.450806
GarageCond	5.450806
GarageFinish	5.450806
GarageYrBlt	5.450806
GarageType	5.382242
BsmtExposure	2.811107
BsmtCond	2.811107
BsmtQual	2.776826
BsmtFinType2	2.742544
BsmtFinType1	2.708262
MasVnrType	0.822763
MasVnrArea	0.788481
MSZoning	0.137127
BsmtFullBath	0.068564
BsmtHalfBath	0.068564
Utilities	0.068564
Functional	0.068564
Electrical	0.034282
BsmtUnfSF	0.034282
Exterior1st	0.034282
Exterior2nd	0.034282
TotalBsmtSF	0.034282
GarageArea	0.034282
GarageCars	0.034282
BsmtFinSF2	0.034282
BsmtFinSF1	0.034282
KitchenQual	0.034282
SaleType	0.034282



##

- MiscFeature
	- 96.400411
	- いいことも、悪いことも書いて有りそうで、内容見ないとわからない。
	- 削除してもいいような気はするが。。








## dropしない

- PoolQC
  - PoolQC	99.691464
  - poolの質。あるなしだけで、貴重な特徴だ。
- Alley
	- 小道へのアクセス
	- 93.212204
	- 貴重な特徴だとは思う
- Fence	80.425094
	- 貴重な特徴だとは思う
- FireplaceQu	48.680151
	- 暖炉の質
	- 貴重
- LotFrontage	16.660953
- GarageQual	5.450806
- GarageCond	5.450806
- GarageFinish	5.450806
- GarageYrBlt	5.450806
- GarageType	5.382242
- GarageArea	0.034282
- GarageCars	0.034282

Garage系の特徴は欠損率が似ている。Garageがないから全部記入なしなのだろうか。


- BsmtFinSF2	0.034282
- BsmtFinSF1	0.034282
- BsmtFullBath	0.068564
- BsmtHalfBath	0.068564
- BsmtUnfSF	0.034282
- TotalBsmtSF	0.034282
- BsmtExposure	2.811107
- BsmtCond	2.811107
- BsmtQual	2.776826
- BsmtFinType2	2.742544
- BsmtFinType1	2.708262

- MasVnrType	0.822763
- MasVnrArea	0.788481

- MSZoning	0.137127

- Utilities	0.068564
- Functional	0.068564
- Electrical	0.034282
- KitchenQual	0.034282
- Exterior1st	0.034282
- Exterior2nd	0.034282
- SaleType	0.034282




## dropさせてもいいかと思う特徴量
