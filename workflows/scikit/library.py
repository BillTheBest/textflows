import re


#
# CLASSIFICATION ALGORITHMS
#

def scikit_naiveBayes(input_dict):
    from sklearn.naive_bayes import GaussianNB 
    y_pred = GaussianNB()
    output_dict={}
    output_dict['bayesout'] = y_pred
    return output_dict

def scikit_J48(input_dict):
    from sklearn import tree
    #parse input and determin its type
    try:
        featureValue= float(input_dict["featureIn"]) if '.' in input_dict["featureIn"] else int(input_dict["featureIn"]) #return int or float
    except ValueError:
        featureValue= input_dict["featureIn"] #return string
    clf = tree.DecisionTreeClassifier(max_features=featureValue, max_depth=int(input_dict["depthIn"]))
    output_dict={}
    output_dict['treeOut'] = clf
    return output_dict

def scikit_linearSVC(input_dict):
    from sklearn.svm import LinearSVC
    clf = LinearSVC(C=float(input_dict["penaltyIn"]),loss=input_dict["lossIn"],penalty=input_dict["normIn"], multi_class=input_dict["classIn"])
    output_dict={}
    output_dict['SVCout'] = clf
    return output_dict

def scikit_SVC(input_dict):
    from sklearn.svm import SVC
    clf = SVC(C=float(input_dict["penaltyIn"]), kernel=str(input_dict["kernelIn"]), degree=int(input_dict["degIn"]))
    output_dict={}
    output_dict['SVCout'] = clf
    return output_dict

def scikit_kNearestNeighbors(input_dict):
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=int(input_dict['numNeib']), weights=input_dict['wgIn'], algorithm=input_dict['algIn'])
    output_dict={}
    output_dict['KNNout'] = knn
    return output_dict

def scikit_logiscticRegression(input_dict):
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression(penalty=str(input_dict["penIn"]), C=float(input_dict["cIn"]))
    output_dict={}
    output_dict['LRout'] = clf
    return output_dict

#
#   REGRESSION
#

def scikit_Ridge(input_dict):
    from sklearn.linear_model import Ridge
    clf = Ridge()
    output_dict={}
    output_dict['out'] = clf
    return output_dict

def scikit_ElasticNet(input_dict):
    from sklearn.linear_model import ElasticNet
    clf = ElasticNet()
    output_dict={}
    output_dict['out'] = clf
    return output_dict

def scikit_LassoLARS(input_dict):
    from sklearn.linear_model import LassoLars
    clf = LassoLars(alpha=float(input_dict["authIn"]))
    output_dict={}
    output_dict['out'] = clf
    return output_dict

def scikit_SGDRegressor(input_dict):
    from sklearn.linear_model import SGDRegressor
    clf = SGDRegressor()
    output_dict={}
    output_dict['out'] = clf
    return output_dict

def scikit_ARDRegression(input_dict):
    from sklearn.linear_model import ARDRegression
    clf = ARDRegression(n_iter=int(input_dict["iterIn"]))
    output_dict={}
    output_dict['out'] = clf
    return output_dict

def scikit_SVR(input_dict):
    from sklearn.svm import SVR 
    clf = SVR()
    output_dict={}
    output_dict['out'] = clf
    return output_dict

#
#   CLUSTERING
#

def scikit_KMeans(input_dict):
    from sklearn import cluster
    k_means = cluster.KMeans(input_dict['clustersNum']) #number of clusters
    output_dict={}
    output_dict['out'] = k_means
    return output_dict


#
#   UTILITIES
#

def scikit_UCIDataset(input_dict):
    from sklearn import datasets
    allDSets = {"iris":datasets.load_iris(), "boston":datasets.load_boston(), "diabetes":datasets.load_diabetes(), " linnerud":datasets.load_linnerud()}
    dataset = allDSets[input_dict['dsIn']]
    output_dict = {}
    output_dict['dtsOut'] = dataset#(dataset.data, dataset.target)
    return output_dict

def scikit_CSVtoNumpy(input_dict):
    # the targer value must be in the last colum of the CSV file
    output_dict={}
    # this code converts data from the csv file into scikit learn dataset and returns it as a tuple
    import numpy
    my_data = numpy.genfromtxt(input_dict['fileIn'], delimiter=',')
    n_sample = []
    n_feature = []
    for x in my_data:
        n_feature.append(x[-1]) 
        n_sample.append(x[:-1])
    print n_sample
    print n_feature
    dataset = (n_sample, n_feature)
    output_dict['scikitDataset'] =  dataset
    return output_dict # returns a touple consiting of n_samples x n_features numpy array X and an array of length n_samples containing the targets y


def scikit_SVMtoScikitDataset(input_dict):
    output_dict={}
    from sklearn.datasets import load_svmlight_file
    X_train, y_train = load_svmlight_file(input_dict['fileIn'])
    output_dict['datasetOut'] = (X_train, y_train)
    return output_dict # returns a touple consiting of n_samples x n_features numpy array X and an array of length n_samples containing the targets y

def scikit_buildClassifier(input_dict):
    learner = input_dict['learner']
    data = input_dict['instances']
    n_sample = data["data"]
    n_feature = data["target"]

    classifier = learner.fit(n_sample, n_feature) #.predict(n_sample)

    output_dict = {'classifier': classifier}
    return output_dict

def scikit_applyClassifier(input_dict):

    classifier = input_dict['classifier']
    data = input_dict['data']
    data["target"] = classifier.predict(data["data"])

    new_data = (data["data"], classifier.predict(data["data"]))
   
    output_dict = {'classes':data}
    return output_dict

def scikit_scikitDatasetToCSV(input_dict):
    output_dict={}
    dataset= input_dict['scikitDataset']
    n_sample = dataset[0]
    n_feature = dataset[1]
    import numpy
    csv=[]
    count=0
    for sample in n_sample:
        csv.append(numpy.append(sample,n_feature[count])) #join n_sample and n_feature array
        count+=1
    #numpy.savetxt("foo.csv", csv, delimiter=",")
    output_dict['CSVout'] = csv
    return output_dict

def scikit_CSVtoOrange(input_dict):
    import orange
    output_dict = {}
    output_dict['dataset'] = orange.ExampleTable(input_dict['file'])
    return output_dict

def scikit_displayDS(input_dict):
    return {}


def scikit_displayDecisionTree(input_dict):
    from sklearn import tree
    from StringIO import StringIO
    out = StringIO()
    out = tree.export_graphviz(input_dict['classifier'], out_file=out)
    import StringIO, pydot 
    from os import system
    dot_data = StringIO.StringIO() 
    dotfile = open("decisionTreeJ48-scikit.dot", 'w')
    dotfile = tree.export_graphviz(input_dict['classifier'], out_file=dotfile) 
    dotfile.close()
    system("dot -Tpng decisionTreeJ48-scikit.dot -o decisionTreeJ48-scikit.png") #CORRECT SO THAT IMAGE IS GOING TO BE SAVED IN THE CORRECT DIRECTORY


#     dataset = input_dict["data"]
#     n_sample = dataset[0]
#     n_feature = dataset[1]
#     import numpy
#     orangeDataset=[]
#     count=0
#     for sample in n_sample:
#         orangeDataset.append(numpy.append(sample,n_feature[count])) #join n_sample and n_feature array
#         count+=1
#     #numpy.savetxt("foo.tab", csv, delimiter="   ")

# def scikit_scikitDatasetToOrange(input_dict):
#     import orange
#     output_dict = {}
#     output_dict['dataset'] = orange.ExampleTable(input_dict['file'])
#     return output_dict





















