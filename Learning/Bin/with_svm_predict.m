

% perform learning with svm


function perf = with_svm_predict()

    [c,g,auc_train] = get_best_parameter(); 
<<<<<<< HEAD
    [c,g,auc_train]
=======
    [c,g]
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    
    % Set the seed of the random number generator
    rand('twister', 0);
    
<<<<<<< HEAD
    addpath('~/softwares/libsvm-3.12/matlab/');
=======
    addpath '~/softwares/libsvm-3.12/matlab/'
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4

    %-----------------------------------
    train = dlmread('../../FeatureExtraction/Results/train.csv',',');
    test = dlmread('../../FeatureExtraction/Results/test.csv',',');
    X = train(:,2:(size(train,2)-1));
    Y = train(:,size(train,2));
    Xtest = test(:,2:size(test,2));
<<<<<<< HEAD
    [X,Xtest] = centering(X,Xtest);
    %[X,Xtest] = tfidf(X,Xtest);
    size(X)
=======
    % centering
    Xall = [X;Xtest];
    Xall = Xall - repmat(mean(Xall),size(Xall,1),1);
    Xall = Xall ./ repmat(std(Xall),size(Xall,1),1);
    %
    X = Xall(1:size(X,1),:);
    Xtest = Xall((size(X,1)+1):size(Xall,1),:);
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    %-----------------------------------
    
    %-------------------------------------
    Xtr = X;
    Ytr = Y;
    Xts = X;
    Yts = Y;
    % training
    model = svmtrain(Ytr,Xtr,sprintf('-q -s 0 -c %.2f -t 2 -g %s -b 1',c,g));
    % prediction in validation
<<<<<<< HEAD
    [Ypred,~,Yprobsvm] = svmpredict(Yts,Xts, model ,'-b 1');
    Yprobsvm = clear_prob(Ytr,Yprobsvm);
    [~,~,~,auc_validation] = perfcurve(Yts,Yprobsvm,1);
    %[~,~,~,auc_validation] = perfcurve(Yts,Ypred,1);
    % prediction in test
    [Ypred,~,Yprobsvm] = svmpredict(zeros(size(Xtest,1),1),Xtest, model, '-b 1');
    Yprobsvm = clear_prob(Ytr,Yprobsvm);
    %-------------------------------------
    
    [auc_train,auc_validation]
=======
    [~,~,Yprobsvm] = svmpredict(Yts,Xts, model ,'-b 1');
    Yprobsvm = clear_prob(Ytr,Yprobsvm);
    [~,~,~,auc_validation] = perfcurve(Yts,Yprobsvm,1);
    % prediction in test
    [~,~,Yprobsvm] = svmpredict(zeros(size(Xtest,1),1),Xtest, model, '-b 1');
    Yprobsvm = clear_prob(Ytr,Yprobsvm);
    %-------------------------------------
    
    auc_train
    auc_validation
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4

    % save results
    res = [test(:,1),Yprobsvm];
    dlmwrite(sprintf('../../Learning/Results/prediction_svm'),res,'delimiter',',')

    %exit;
    
end

<<<<<<< HEAD
=======
function Yprobsvm = clear_prob(Ytr,Yprobsvm)
    if Ytr(1) == 0
        Yprobsvm = Yprobsvm(:,2);
    end
    if Ytr(1) == 1
        Yprobsvm = Yprobsvm(:,1);
    end
end

>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4


function [c,g,auc] = get_best_parameter()
        system('cat ../../Learning/Results/ParameterSelection/* | sort -t, -k 1,1n > ../../Learning/Results/parameter_selection_result');
        data = dlmread('../../Learning/Results/parameter_selection_result');
        K = data(1,2);
        n = ceil(data(size(data,1),1)/K);
        perf = [];
        for i = 1:n
                subind = floor((data(:,1)-1)/K)==i-1;
                subdata = data(subind,:);
                subperf = mean(subdata);
                perf = [perf;subperf(4:6)];
        end
        perf = perf(perf(:,3)==max(perf(:,3)),:);
        %pickingind = size(perf,1);
        pickingind = 1;
        c = perf(pickingind,1);
        g = perf(pickingind,2);
        auc = perf(pickingind,3);
end




