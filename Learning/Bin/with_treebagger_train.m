% perform learning with svm
function perf = with_treebagger_train(paramind,K,k,c,outfilename)
    paramind = eval(paramind);
    K = eval(K);
    k = eval(k);
    c = eval(c);

    cvresults = [];
    for cvind = 1:1

        % Set the seed of the random number generator
        rand('twister', 0);
        
        addpath('~/softwares/libsvm-3.12/matlab/');
        
        %-----------------------------------
        train = dlmread('../../FeatureExtraction/Results/train.csv',',');
        test = dlmread('../../FeatureExtraction/Results/test.csv',',');
        X = train(:,2:(size(train,2)-1));
        Y = train(:,size(train,2));
<<<<<<< HEAD
        %Xtest = test(:,2:size(test,2));
        %-----------------------------------
        
        X = X(:,[1:50,15112:size(X,2)]);
=======
        Xtest = test(:,2:size(test,2));
        %-----------------------------------
        
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
        
        % corss validation for parameter selection
        Ind = crossvalind('Kfold',size(X,1),K);    
        
        %-------------------------------------
        Xtr = X(Ind~=k,:);
        Ytr = Y(Ind~=k,:);
        Xts = X(Ind==k,:);
        Yts = Y(Ind==k,:);
        % training
        model = TreeBagger(c,Xtr,Ytr, 'Method', 'classification');
        % predict
        [~,Yprobtree] = predict(model, Xts);
        Yprobtree = clear_prob(Ytr,Yprobtree);
        % performance
        [~,~,~,auc_validation] = perfcurve(Yts,Yprobtree,1);
        %-------------------------------------
        cvresults = [cvresults,auc_validation];
    end
        
    perf = [paramind,K,k,c,mean(cvresults)];

    dlmwrite(sprintf('%s', outfilename),perf,',');

    exit;
    
end





