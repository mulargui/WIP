dftrain=pd.read_csv('/kaggle/input/learn-together/train.csv')

#validate files - nans per feature
print(dftrain.isnull().sum(axis = 0))

#validate files - no rows with all zeros
print(dftrain[dftrain.drop(['Id','Cover_Type'], axis=1).eq(0).all(1)].empty)

#split train data in features and labels
y = dftrain.Cover_Type
x = dftrain.drop(['Id','Cover_Type'], axis=1)


#normalize features
#in the future it can be done more elegantly, for now just using the max min values of the data that we know
#x['Elevation']=(x['Elevation']-x['Elevation'].min())/(x['Elevation'].max()-x['Elevation'].min())                             
x['Elevation']=(x['Elevation']-1859)/(3858-1859)                             
x['Aspect']=x['Aspect']/360                      
x['Slope']=x['Slope']/66                      
x['Horizontal_Distance_To_Hydrology']=x['Horizontal_Distance_To_Hydrology']/1397                      
x['Vertical_Distance_To_Hydrology']=(x['Vertical_Distance_To_Hydrology']+173)/(601+173)                             
x['Horizontal_Distance_To_Roadways']=x['Horizontal_Distance_To_Roadways']/7117                      
x['Hillshade_9am']=x['Hillshade_9am']/254                      
x['Hillshade_Noon']=x['Hillshade_Noon']/254                      
x['Hillshade_3pm']=x['Hillshade_3pm']/254                      
x['Horizontal_Distance_To_Fire_Points']=x['Horizontal_Distance_To_Fire_Points']/67173                      
                                

#validate data - no rows with all zeros
#x.index[x.eq(0).all(1)]
print(x[x.eq(0).all(1)].empty)

# convert the label to One Hot Encoding
#to_categorical requires 0..6 instead of 1..7
y -=1
y = y.to_numpy()

