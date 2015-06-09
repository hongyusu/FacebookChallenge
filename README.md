

#Facebook challenge of detecting bots in the online bidding environment

This repository contains the strategies, models and algorithms I used in Facebook challenge of detecting bots in the online bidding environment. The model I developed has an AUC score of 93.269% where the best AUC score reported in the leaderboard is about 94.254%, ranking 56 out of 1004. Everything documented here is done within about one week's time, and mostly at night. The model can be surely improved given more time. In particular, 

1. Event website: [https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot](https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot) 
2. Leaderboard: [https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/leaderboard?submissionId=1680911](https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/leaderboard?submissionId=1680911)
3. My participation name: Aalto
4. Ranking: 56 / 1004
5. Performance in AUC: 93.269% / 94.254%
4. GitHub project website: [http://hongyusu.github.io/FacebookChallenge/](http://hongyusu.github.io/FacebookChallenge/) 
5. GitHub project page: [https://github.com/hongyusu/FacebookChallenge](https://github.com/hongyusu/FacebookChallenge)


## Lessons learned

First thing first, lessons learned from this competition can be potentially useful. They are summarised in the following bullet list

1. Support Vector Machine can be useful as a baseline classifier for the following reasons
   1. SVM is a stable classifier. It is robust against training data perturbation.
   2. There are rich kernel functions in SVM which can do nonlinear feature map that map the data point from the original feature space to high dimensional feature space.
   3. In particular, kernel SVM allows user-defined kernel function for measuring similarities.
   4. The optimization of the model is standard and fast.
   5. SVM training and prediction is implemented in, e.g., LibSVM package.
2. However, it is better not to completely trust SVM for the following reasons
   1. It is not very efficient for large-scale data.
   2. Although kernel SVM is very useful, it is not practical in most cases when the number of training data is over a few thousands.
   3. It is a stable classifier, therefore, it is not very good to use as the base learner in ensemble learning.
3. Random forest is another good option in addition to SVM for the following reasons:
   1. Random forest does not need feature normalization, cantering, etc.
   2. Well, I guess random forest somehow needs feature selection, but not very extensive.
   2. Random forest does not have many parameter to tune where the only parameter in random forest is the number of decision trees.
   3. It is relatively fast to learn a random forest classifier than learning a SVM model.
   4. Off-the-shelf function in MATLAB.
4. Adding more feature is not always helpful. In many cases, more feature will be harmful to the performance.
5. It is  better to start with one classification model (e.g., SVM) and perform the experiments. Tune the model until hitting the bottleneck of the model. Then wisely change to another classification methods (e.g., random forest).
6. Measure the performance in terms of AUC other than Accuracy, as accuracy is easily mislead by the biasness of the data.
7. Training data and test data are sometime very heterogeneous. Parameter selection and model performance based on the Cross validation on the training data might not be similary on the test data.

## Final strategy

The following is about the final strategy I decided to use in the competetion. It could be better given more time.

### Feature representation 

1. Features are extract from auction log including local features, global features, local per hour feature, _bag-of-words_ features.
2. Some of the features are not used in the learning algorithm, which can potentially improve the prediction performance of the model.

   1. Global features
      1. Global feature are made by using all bids. 
      2. Global features are listed in the following table.
      3. There is only one bit for bid feature, four bits for others.
      4. Feature number 8-14 are computed but are not used in this stage.

        |Feature Id|Feature Name|Feature Position|
        |------:|----:|-----:|
        |1 |bid              |1 |
        |2 |auction          |3 |
        |3 |merchandise      |4 |
        |4 |device           |5 |
        |5 |time             |6 |
        |6 |country          |7 |
        |7 |ip               |8 |
        |8 |url              |9 |
        |9 |minute           |10|
        |10|hour             |11|
        |11|day              |12|
        |12|hourday          |13|
        |13|interval         |14|
        |14|average interval |15|

   2. Auction specific features
      1. Auction specific features are extracted from bider-auction files.
      2. We use auctions which has more than 2 bids.
      3. Features are listed in the following table.
      4. Besides there being one position for the bid sum, there is one position for average of each individual.

        |Feature Id|Feature Name|Feature Position|
        |------:|----:|-----:|
        |1 |bid      |1|
        |2 |device   |5|
        |3 |country  |7|
        |4 |ip       |8|
        |5 |url      |9|
        |6 |interval |14|

   3. Per-hour features
      1. Per-hour features include features listed in the following table.
      2. Per-hour features are computed based on hours.
      3. There is one position for the average of the per hour features.

        |Feature Id|Feature Name|Feature Position|
        |------:|----:|-----:|
        |1 |bid              |1 |
        |2 |auction          |3 |
        |3 |merchandise      |4 |
        |4 |device           |5 |
        |5 |country          |7 |
        |6 |ip               |8 |
        |7 |url              |9 |

   4. Per-minute features
      1. Per-minute features include features listed in the following table.
      2. Per-minute features are computed based on minute.
      3. There is one position for the average of the per minute features.

        |Feature Id|Feature Name|Feature Position|
        |------:|----:|-----:|
        |1 |bid              |1 |
        |2 |auction          |3 |
        |3 |merchandise      |4 |
        |4 |device           |5 |
        |5 |country          |7 |
        |6 |ip               |8 |
        |7 |url              |9 |

   5. _bag-of-words_ features
       1. Each bider is represented by the following _bag-of-words_ features.
       2. Most of them are not used in the current stage of the experiment due to the time limit.
       3. However, we consider auction/merchandise/device/country information as the only _bag-of-words_ features.

        |Feature Id|Feature Name|Feature Position|
        |------:|----:|-----:|
        |1 |auction          |3 |
        |2 |merchandise      |4 |
        |3 |device           |5 |
        |4 |time             |6 |
        |5 |country          |7 |
        |6 |ip               |8 |
        |7 |url              |9 |


### Learning algorithm

1. Support Vector Machine
   1. Support Vector Machine (SVM) with probability output as baseline learner.
   2. Feature representation of data is introduced in the last section.
   3. We center the feature vector to have zero mean and unit variance such that points are located in a unit square.
   4. Centering the feature is done base on both training and testing data.
   2. We use _Gaussian_ RBF kernel over the feature representation of the data points.
   3. We use grid Search for the best parameter combination, e,g, margin slack parameter, _Gaussian_ width parameter.
   4. Best model is then used for prediction.
   5. We use the implementation of SVM from LibSVM toolbox.
   6. The basic MATLAB usage example is 
   
                model = svmtrain(Ytr,Xtr,sprintf('-q -s 0 -c %.2f -t 2 -g %s -b 1',c,g));
                [~,~,Yprobsvm] = svmpredict(Yts,Xts, model ,'-b 1'); 
                [~,~,~,AUC] = perfcurve(Yts,Yprobsvm,1);

2. Random Forest 
   1. We use build-in function in MATLAB.
   2. We tune the parameter of the number of trees with 10 fold cross validation.
   3. The best model is then used for prediction.
   4. The basic MATLAB usage example is 

        model = TreeBagger(c,Xtr,Ytr, 'Method', 'classification');
        [~,Yprobtree] = predict(model, Xts);

   5. Be careful with the order of the probability outputs.

### Measure the performance

We use AUC score to measure the prediction performance of the models. AUC is the area under the ROC curve.

### Experimental results:

1. SVM

   1. global + auction + hour, duplicate 7 global feature, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8916|0.9950|||0.5|50   |
   
   1. auction + hour + minute, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8410|0.9325|||5|0.5   |
   
   1. global + auction + hour + minute, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8788|0.9898|||1|50   |
   
   1. global + auction + hour + minute, duplicate 7 global, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8895|0.9936|||0.01|50   |
   
   1. global + auction + hour + minute + _bag-of-words_ country, duplicate 7 global, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8819|0.9957|||5|50   |
   
   1. _bag-of-words_ country, 10 fold cv, tfidf
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.6934|0.8241|||1|0.001   |
   
   1. _bag-of-words_ country, 10 fold cv, centering
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.8484|0.9507|||0.5|0.5   |

2. Random Forest
   
   1. Random forest, global + auction + hour + minute + _bag-of-words_ country, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|N|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.9220|0.9974|||125| 
   
   1. Random forest, global + auction + hour + minute + _bag-of-words_ country/device, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|N|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|0.90757|0.9238|0.9978|||135| 
   
   1. Random forest, global + auction + hour + minute + _bag-of-words_ auction/merchandise/country/device, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|N|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.9107|0.9980|||195| 

   1. Random forest, global + auction + hour + minute + _bag-of-words_ merchandise/country/device, 10 fold cv
   
      |Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|N|
      |------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|
      | |0608|      |0.9191|0.9981|||195| 

### Best model

Best performance is achieved with model 2.2. In particular, it is a random forest learner with various hand made featuers.


----------------


## History of coding and experiments

The following text documents the history of joining the competetion, including 
1. Different feature embedding strategy
2. Coding
3. Parameter selection methods
4. Experimental results

### Basic setting as baseline
- Support Vector Machine (SVM) with probability output as baseline learner
- Compose about 10 global values as feature representation of each bidder.
- _Gaussian_ RBF kernel over the feature representation.
- Grid Search for the best parameter, e,g, margin slack parameter, _Gaussian_ width parameter.
- Best model is then used for prediction.
- Prediction performance is shown in the following table

|Methods|Time|Test AUC|Training best AUC|Training all AUC|
|-----:|-----:|-----:|-----:|-----:|
|Global|20150528|0.72485|0.75166|0.90494|
|Global+Local|20150530|0.87348|0.8230|0.8861|
|Global+Local(correct)|20150530|0.89848|0.8884|0.8983|
|Global+Local(correct)+10|20150601|0.88199|0.8858|0.9200|
|Global+Local(correct)+20|20150601|0.88186|0.8986|0.9198|
|add new time feature|20150601|0.88900|0.9020|0.9253|

###Time
- 1 second = 52631578
- min: 9631916842105263
- max: 9772885210526316 
- The data is for a period of 31 days.


###Feature
 unique bid

1. unique auction
2. unique merchandise
3. unique device
4. unique time in second
5. unique country
6. unique ip
7. unique url
8. unique minute
9. unqiue hour
10. unique day
11. unique hour-day
12. unique interval 
13. unique intervalcount

- Global features (1+13x4) 
  - How many unique XXX
  - MIN, MAX, AVERAGE bids per unique XXX

- Local features 
  - auction with more than 100 bidders 


- 1:12 (1-12)
- 13:900

- 1 (sum)
- 12x4 (1-13/ time)
- 3552


###Log

###History
1. 1+7+7x4 features, SVM, 10 fold cv
2. 1+7+7x4 features, SVM, 5 fold cv
3. 1+7+7x4 features, SVM, 5 fold cv, 5 replicates
4. 1+7+7x4 features, SVM, 10 fold cv, 10 replicates
5. 1+11+11x4 features, SVM, 10 fold cv, 10 replicates
6. 1+11+11x4 features, SVM, 5 fold cv, 5 replicates
7. 1+11x4 features, SVM, 5 fold cv, 5 replicates 
8. 1+11x4 features, SVM, 10 fold cv, 10 replicates 
9. 1+13x4 features, SVM, 10 fold cv, 10 replicates 
10. 1+13x4 features, SVM, 5 fold cv, 5 replicates 
11. 1+13x4 features, SVM, 10 fold cv, 10 replicates, 0 feature -> 0 prediction 
12. 1+13x4 features, SVM, 10 fold cv, 10 replicates, voting over 10 replicates 
13. 1+13x4 features, SVM, 15 fold cv, 15 replicates, voting over 15 replicates 
14. 1+12x4 features (no hour-day), SVM, 15 fold cv, 15 replicates, voting over 15 replicates 
15. 1+11x4 features (no hour,hour-day), SVM, 15 fold cv, 15 replicates, voting over 15 replicates 

|ind|Time|Test AUC|Training best AUC|Training all AUC|SVM C|RBF G|
|------:|----:|-----:|-----:|-----:|-----:|-----:|
|1|20150601||0.8776|0.9600|10|0.1|
|2|20150601||0.8729|0.9874|0.1|50|
|3|20150601||0.8750|0.9181|0.05|0.01|
|4|20150601||0.8808|0.9173|0.1|0.01|
|5|20150601||0.8840|0.9212|0.05|0.01|
|6|20150601||0.8873|0.9201|0.5|0.01|
|7|20150601||0.8745|0.9257|0.05|100|
|8|20150601||0.8743|0.9275|0.01|1|
|9|20150602|0.84797|0.8827|0.9902|0.5|50|
|10|20150602||0.8790|0.9845|0.1|50|
|11|20150602|0.84797|0.8837|0.9902|0.5|50|
|12|20150602|0.85515|0.9148||0.5|50|
|13|20150602||0.9159||0.5|50|
|14|20150603||0.9184||5|50|
|15|20150603||0.9030||5|50|





### Experimental settings with local featuers

1. 1+12x4 global features + 10X2 averaged local features, auctions with > 100 bidders, 10 fold cv+replications, voting in single best fold, centering
2. 1+12x4 global features + 10X2 averaged local features, auctions with > 100 bidders, 10 fold cv+replications, use all training data, centering
3. 1+12x4 global features + 10X2 averaged local features, auctions with > 100 bidders, 10 fold cv, use all training data, centering
4. 1+12x4 global features, auctions with > 100 bidders, 10 fold cv, use all training data, centering

2. Nx10 local auction features, auctions with > 100 bidders, 10 fold cv+replications, centering


|ind|Time|Test AUC|Training best AUC|Training all AUC|K|k|SVM C|RBF G|
|------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|1|0604|0.83405|0.9160||10|6|50|0.5|
|2|0604|0.83991|0.8919|0.9868|||10|0.5|
|3|0604||0.9002|0.9868|||10|0.5|
|4|0604|0.83685|0.9028|0.9912|||0.01|50|



1. 1+13x4 global features (original x7, time x4, interval x2), 10 fold cv, use all training data, centering
2. 1+13x4 global features (original x7, time x4, interval x2) + duplicate x1 global feature x13, 10 fold cv, use all training data, centering
3. 1+13x4 global features (original x7, time x4, interval x2) + duplicate x2 global feature x13, 10 fold cv, use all training data, centering
4. 1+13x4 global features (original x7, time x4, interval x2) + duplicate x1 global feature x13 + local, 10 fold cv, use all training data, centering
   1. local features
      1. local feature, which is extracted from bider-auction file
      2. use auction with more than 5 bids
      3. features include
         1. bid
         2. device
         3. country
         4. ip
         5. url
         6. interval
      4. there is one bit for bid sum, one bit for average of each individual (this constraint is added and experimented as 5.)
   2. global features
      1. global feature are made by using all bids 
      2. global feature includes
         1. bid 
         2. auction
         3. device
         4. country
         5. time
         6. ip
         7. url
         8. minute
         9. hour
         10. day
         11. hour-day
         12. interval
         13. average interval
      3. there is only one bit for bid feature, four bits for others
5. As 4, only 4.4 changes
6. As 5, 5 fold cv 
7. As 5, global feature without time, 5 fold cv 
8. As 5, global feature without hour-day and interval, 10 fold cv 
9. As 5, + local time features, 10 fold cv 
10. As 9, random seed is 0

|Experiment|Time|Test AUC|CV best AUC|Training all AUC|K|k|SVM C|RBF G|
|------:|----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|1 |0605|       |0.8987|0.9824|||0.01|50  |
|2 |0605|       |0.9038|0.9406|||0.01|1   |
|3 |0605|       |0.8996|0.9867|||0.05|50  | 
|4 |0605|0.85881|0.8959|0.9811|||0.1 |50  |
|5 |0605|       |0.8962|0.9816|||0.1 |50  |
|6 |0605|       |0.8922|0.9803|||0.5 |50  |
|7 |0605|       |0.8727|0.9803|||0.01|0.01|
|8 |0605|       |0.8900|0.9220|||0.05|0.01|
|9 |0605|0.86097|0.8964|0.9851|||1   |50  |
|10|0605|0.88444|0.8956|0.9445|||0.5 |1   |



