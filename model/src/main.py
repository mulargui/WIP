
from data import Data
d = Data('/data/train.csv')
#d.data_validation()
d.data_engineering()
d.split(0.2)

from model import Model
m = Model()
m.train(d.x_train, d.y_train, d.x_test, d.y_test)
m.save()
