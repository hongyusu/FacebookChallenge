

% perform learning with svm


function perf = with_svm_predict()

    [K,k,c,g,auc_train] = get_best_parameter(); 
    [K,k,c,g,auc_train]

    cvresults = zeros(1,K);
    test = dlmread('../../FeatureExtraction/Results/test.csv',',');
    cvYts = zeros(size(test,1),K);

    for cvind = 1:K

        % Set the seed of the random number generator
        rand('twister', cvind);
        
        addpath '~/softwares/libsvm-3.12/matlab/'
        
        %-----------------------------------
        train = dlmread('../../FeatureExtraction/Results/train.csv',',');
        test = dlmread('../../FeatureExtraction/Results/test.csv',',');
        X = train(:,2:(size(train,2)-1));
        Y = train(:,size(train,2));
        Xtest = test(:,2:size(test,2));
        %-----------------------------------
        [X,Xtest] = centering(X,Xtest);
        
        
        % corss validation for parameter selection
        Ind = crossvalind('Kfold',size(X,1),K);    
        
        %-------------------------------------
        Xtr = X(Ind~=k,:);
        Ytr = Y(Ind~=k,:);
        Xts = X(Ind==k,:);
        Yts = Y(Ind==k,:);
        % training
        model = svmtrain(Ytr,Xtr,sprintf('-q -s 0 -c %.2f -t 2 -g %s -b 1',c,g));
        % prediction
        [~,~,Yprobsvm] = svmpredict(Yts,Xts, model ,'-b 1');
        Yprobsvm = clear_prob(Ytr,Yprobsvm);
        % performance
        [~,~,~,AUC] = perfcurve(Yts,Yprobsvm,1);
        %-------------------------------------
        cvresults(cvind) = AUC;
        % prediction in test
        [~,~,Yprobsvm] = svmpredict(zeros(size(Xtest,1),1),Xtest, model, '-b 1');
        Yprobsvm = clear_prob(Ytr,Yprobsvm);
        cvYts(:,cvind) = Yprobsvm;
    end
        
    
    [auc_train,mean(cvresults)]
    cvresults

    cvresults = cvresults/sum(cvresults);
    cvYts = cvYts*cvresults';

    % save results
    res = [test(:,1),mean(cvYts,2)];
    dlmwrite(sprintf('../../Learning/Results/prediction_svm'),res,'delimiter',',')

    %exit;
    
end



function [K,k,c,g,auc] = get_best_parameter()
        system('cat ../../Learning/Results/ParameterSelection/* | sort -t, -k 6,6n |tail -n1 > ../../Learning/Results/parameter_selection_result');
        data = dlmread('../../Learning/Results/parameter_selection_result');
        K = data(1,2);
        k = data(1,3);
        c = data(1,4);
        g = data(1,5);
        auc = data(1,6);
end




