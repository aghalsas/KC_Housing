## Function doe Ridge regression with n features
def withnfeatures(data,n):
    #correlation matrix between all the variables
    
    corrmat = data.corr()
#    k = train_cont.shape[1] #number of variables for heatmap
    k = data.shape[1]
    cols = corrmat.nlargest(k, 'price')['price'].index
    cm = np.corrcoef(data[cols].values.T)
    #Selecting the features most correlated with target variable in their absolute value
    l = cols[np.argsort(np.abs(cm[0]))[::-1][1:n+1]].values#n+1 because just 1:1 gives the index only

    #Select those particular features
    data_l = data[l]
    
    y = data['price']
    X = data_l

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

    ridge = RidgeCV(alphas=np.logspace(0,3,20)).fit(X_train, y_train)
    
    testpred = ridge.predict(X_test)
    alpha = ridge.alpha_
    
    #Calculate rmse
    testpred[testpred < 0] = np.mean(y_train)
    err = np.sqrt(((testpred-y_test)**2).sum()/len(y_test))
    act_err = np.sqrt((((np.exp(testpred)-1)-(np.exp(y_test))-1)**2).sum()/len(y_test))

    
    
    #Return
    return err, l, act_err

#### Function to convert categorcical data to numerical by establishing a monotonic relationship
def cattonum(data,feature,target):
#    set up an array to calculate the mean and std for each unique feature
#    meanstd = np.zeros([data[feature].nunique(),2])
    for i,x in enumerate(df[feature].unique()):
        meanstd[i,0] = df[df[feature]==x][target].mean()
        meanstd[i,1] = df[df[feature]==x][target].std()
    #meanstd[:,0] = data.groupby(feature).mean()[[target]]
    #meanstd[:,1] = data.groupby(feature).std()[[target]]
    
    #Sort by the mean of the label to arrange them in ascending order
    s = meanstd[:,0].argsort()
    meanstd = meanstd[s]
    
    #get the original labels
    labels = data[feature].unique()[s]
    
    #Plot in an ascending 
    plt.errorbar(range(0,s.shape[0]), meanstd[:,0], 0.5*meanstd[:,1], marker='o', mfc='red',
         mec='blue', ms=2, mew=4)
    plt.xticks(range(0,s.shape[0]), labels, rotation='vertical')
    
    #replace labels by numbers starting from 1 to no. of labels
    data[feature] = data[feature].replace(labels,range(1,s.shape[0]+1))
    return None