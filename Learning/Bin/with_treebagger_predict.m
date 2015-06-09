

% perform learning with svm


function perf = with_treebagger_predict()

    [c,auc_train] = get_best_parameter(); 
    [c,auc_train]
    
    % Set the seed of the random number generator
    rand('twister', 0);
    
    addpath('~/softwares/libsvm-3.12/matlab/');

    %-----------------------------------
    train = dlmread('../../FeatureExtraction/Results/train.csv',',');
    test = dlmread('../../FeatureExtraction/Results/test.csv',',');
    X = train(:,2:(size(train,2)-1));
    Y = train(:,size(train,2));
    Xtest = test(:,2:size(test,2));
<<<<<<< HEAD
    size(X)
    %-----------------------------------
        X = X(:,[1:50,15112:size(X,2)]);
        Xtest = Xtest(:,[1:50,15112:size(Xtest,2)]);
=======
    %[X,Xtest] = centering(X,Xtest);
    %[X,Xtest] = tfidf(X,Xtest);
    size(X)
    %-----------------------------------
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    
    %-------------------------------------
    Xtr = X;
    Ytr = Y;
    Xts = X;
    Yts = Y;
    % training
    model = TreeBagger(c,Xtr,Ytr, 'Method', 'classification');
    % prediction in validation
    [~,Yprobtree] = predict(model, Xts);
    Yprobtree = clear_prob(Ytr,Yprobtree);
    [~,~,~,auc_validation] = perfcurve(Yts,Yprobtree,1);
    % prediction in test
    [~,Yprobtree] = predict(model, Xtest);
    Yprobtree = clear_prob(Ytr,Yprobtree);
    %-------------------------------------
 
    [auc_train,auc_validation]

    % save results
    res = [test(:,1),Yprobtree];
    dlmwrite(sprintf('../../Learning/Results/prediction_svm'),res,'delimiter',',')

    %exit;
    
end



function [c,auc] = get_best_parameter()

        system('cat ../../Learning/Results/ParameterSelection/tree_* | sort -t, -k 1,1n > ../../Learning/Results/tree_parameter_selection_result');
        data = dlmread('../../Learning/Results/tree_parameter_selection_result');

        K = data(1,2);
        n = ceil(data(size(data,1),1)/K);
        perf = [];
        for i = 1:n
                subind = floor((data(:,1)-1)/K)==i-1;
                subdata = data(subind,:);
                subperf = mean(subdata);
                perf = [perf;subperf(4:5)];
        end
        perf = perf(perf(:,2)==max(perf(:,2)),:);
        %pickingind = size(perf,1);
        pickingind = 1;
        c = perf(pickingind,1);
        auc = perf(pickingind,2);

        
end




