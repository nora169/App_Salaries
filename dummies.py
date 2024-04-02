workclass_dummies={'Local-gov':[1,0,0,0,0,0],
                   'Private':[0,1,0,0,0,0],
                   'Self-emp-inc':[0,0,1,0,0,0],
                   'Self-emp-not-inc':[0,0,0,1,0,0],
                   'State-gov':[0,0,0,0,1,0],
                   'Without-pay':[0,0,0,0,0,1],
                   'Federal-gov':[0,0,0,0,0,0]
                   }





education_dummies= {
    
                   '11th':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   '12th':[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   '1st-4th':   [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                   '5th-6th':   [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                   '7th-8th':   [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                   '9th':       [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                   'Assoc-acdm':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                   'Assoc-voc': [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                   'Bachelors': [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                   'Doctorate': [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                    'HS-grad':  [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                    'Masters':  [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                    'Preschool':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                  'Prof-school':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                   'Some-college': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    '10th':     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      }

marital_status_dummies={
    'married':[1,0],
    'single':[0,1],
    'divorced':[0,0]
}



occupation_dummies={'Armed-Forces': [1,0,0,0,0,0,0,0,0,0,0,0,0] ,
                        'Craft-repair' :       [0,1,0,0,0,0,0,0,0,0,0,0,0] ,
                        'Exec-managerial':     [0,0,1,0,0,0,0,0,0,0,0,0,0] ,
                        'Farming-fishing' :    [0,0,0,1,0,0,0,0,0,0,0,0,0] ,
                        'Handlers-cleaners':   [0,0,0,0,1,0,0,0,0,0,0,0,0] ,
                        'Machine-op-inspct' :  [0,0,0,0,0,1,0,0,0,0,0,0,0] ,
                        'Other-service'    :   [0,0,0,0,0,0,1,0,0,0,0,0,0] ,
                        'Priv-house-serv'  :   [0,0,0,0,0,0,0,1,0,0,0,0,0] ,
                        'Prof-specialty'    :  [0,0,0,0,0,0,0,0,1,0,0,0,0] ,
                        'Protective-serv' :    [0,0,0,0,0,0,0,0,0,1,0,0,0] ,
                        'Sales'            :   [0,0,0,0,0,0,0,0,0,0,1,0,0] ,
                        'Tech-support'      :  [0,0,0,0,0,0,0,0,0,0,0,1,0] ,
                        'Transport-moving'  :  [0,0,0,0,0,0,0,0,0,0,0,0,1] ,
                        'Adm-clerical':        [0,0,0,0,0,0,0,0,0,0,0,0,0] 
}

relationship_dummies={'Not-in-family':[1,0,0,0,0],
    'Other-relative':[0,1,0,0,0],
                      'Own-child ':[0,0,1,0,0],
                      'Unmarried':[0,0,0,1,0],
                      'Wife':[0,0,0,0,1],
                      'Husband':[0,0,0,0,0]


}


race_dummies={
 'Asian-Pac-Islander':[1,0,0,0],
 'Black':[0,1,0,0],
 'Other':[0,0,1,0],
 'White':[0,0,0,1],
 'Amer-Indian-Eskimo':[0,0,0,0]

}

gender_dummies={
  'Male':[1],
  'Female':[0]
 }


country_dummies={
    'United-States':[1],
    'Other':[0]
    }

income_dummies={
  'income_>50K':[1],
  'income_<50K':[0] }