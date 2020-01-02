#### Function to convert categorcical data to numerical by establishing a monotonic relationship
def cattonum73(data,feature,target):
#    set up an array to calculate the mean and std for each unique feature
#    meanstd = np.zeros([data[feature].nunique(),2])
#    for i,x in enumerate(df[feature].unique()):
#        meanstd[i,0] = df[df[feature]==x][target].mean()
#        meanstd[i,1] = df[df[feature]==x][target].std()
#    #meanstd[:,0] = data.groupby(feature).mean()[[target]]
#    #meanstd[:,1] = data.groupby(feature).std()[[target]]
    
    #Sort by the mean of the label to arrange them in ascending order
#    s = meanstd[:,0].argsort()
#    meanstd = meanstd[s]
    
    #get the original labels
#    labels = data[feature].unique()[s]
    
    #Plot in an ascending 
#    plt.errorbar(range(0,s.shape[0]), meanstd[:,0], 0.5*meanstd[:,1], marker='o', mfc='red',
#         mec='blue', ms=2, mew=4)
#    plt.xticks(range(0,s.shape[0]), labels, rotation='vertical')
    
    #replace labels by numbers starting from 1 to no. of labels
#    data[feature] = data[feature].replace(labels,range(1,s.shape[0]+1))
    return data