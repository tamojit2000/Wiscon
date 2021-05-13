import pandas as pd
import numpy as np

from sklearn.feature_selection import mutual_info_classif

import warnings
warnings.filterwarnings("ignore")



def Famex(X1_train, Y1_train):
    X1_train=pd.DataFrame(X)
    sim_mat = round(np.abs(X1_train.corr()), 2)
    sim_mat[sim_mat == 1.0] = 0
    
    
    vert_color_map = []
    node_grade = []
    for i in range(len(sim_mat)):
        if (len(sim_mat[sim_mat.iloc[i, :] >= 0.67]) == 0):
            #vert_color_map.insert(i,'green') 
            node_grade.insert(i,1) 
        elif((len(sim_mat[sim_mat.iloc[i, :] >= 0.9]) >= 1)| (len(sim_mat[sim_mat.iloc[i, :] >= 0.67]) >=3) ):
            #vert_color_map.insert(i,'red')
            node_grade.insert(i,3)
        else:
            #vert_color_map.insert(i,'blue')
            node_grade.insert(i,2)



def solve(filename):
    #print('Inside')
    #filename = 'wiscon.csv'
    data = pd.read_csv(filename)
    #print(data)

    X = data.iloc[:, 0 : (data.shape[1] - 1)]
    Y = pd.DataFrame(data.iloc[:, (data.shape[1] - 1)])

    

    X1_train=pd.DataFrame(X)
    sim_mat = round(np.abs(X1_train.corr()), 2)
    sim_mat[sim_mat == 1.0] = 0
    
    
    vert_color_map = []
    node_grade = []
    
    for i in range(len(sim_mat)):
        if (len(sim_mat[sim_mat.iloc[i, :] >= 0.67]) == 0):
            #vert_color_map.insert(i,'green') 
            node_grade.insert(i,1) 
        elif((len(sim_mat[sim_mat.iloc[i, :] >= 0.9]) >= 1)| (len(sim_mat[sim_mat.iloc[i, :] >= 0.67]) >=3) ):
            #vert_color_map.insert(i,'red')
            node_grade.insert(i,3)
        else:
            #vert_color_map.insert(i,'blue')
            node_grade.insert(i,2)




        

    sim_mat[sim_mat >= 0.67] = 1
    sim_mat[sim_mat < 0.67] = 0

    sim_score = np.square(node_grade) / np.mean(node_grade) #

    mi = mutual_info_classif(X, Y)

    rel_score = mi/np.mean(mi) #

    feature_criticality_score = rel_score/sim_score 

    feature_criticality_score=-np.sort(-feature_criticality_score) #

    '''
    df_feature_names = pd.DataFrame(X1_train.columns)

    df_criticality_score = pd.DataFrame(feature_criticality_score)
    df_feat_name2score = pd.concat([df_feature_names, df_criticality_score], axis = 1)
    df_feat_name2score.columns = ['Feature Name', 'Criticality Score']
    
    
    return df_feat_name2score.sort_values('Criticality Score', ascending=False)
    '''

    

    #print(sim_score,rel_score,feature_criticality_score)

    #print('Done')

    return sim_score,rel_score,feature_criticality_score,data.columns


#solve('wiscon.csv')

