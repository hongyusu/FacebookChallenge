<<<<<<< HEAD
% perform learning with svm
function perf = with_svm_train(paramind,K,k,c,g,outfilename)
=======


% perform learning with svm


function perf = with_svm_train(paramind,K,k,c,g,outfilename)

>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    paramind = eval(paramind);
    K = eval(K);
    k = eval(k);
    c = eval(c);
    g = eval(g);
<<<<<<< HEAD

    cvresults = [];
    for cvind = 1:1

        % Set the seed of the random number generator
        rand('twister', 0);
        
        addpath('~/softwares/libsvm-3.12/matlab/');
=======
    
    cvresults = zeros(1,K);
    for cvind = 1:K

        % Set the seed of the random number generator
        rand('twister', cvind);
        
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
        %-----------------------------------
=======
        %-----------------------------------
        [X,Xtest] = centering(X,Xtest);
        %[X,Xtest] = tfidf(X,Xtest);
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
        
        
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
<<<<<<< HEAD
        cvresults = [cvresults,AUC];
=======
        cvresults(cvind) = AUC;
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    end
        
    perf = [paramind,K,k,c,g,mean(cvresults)];

    dlmwrite(sprintf('%s', outfilename),perf,',');

    exit;
    
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

function [X,Xtest] = centering(X,Xtest)
    % centering
    Xall = [X;Xtest];

    Xall = Xall(:,[1:49,8930:8949]);

    Xall = Xall - repmat(mean(Xall),size(Xall,1),1);
    Xall = Xall ./ repmat(std(Xall),size(Xall,1),1);
    %
    X = Xall(1:size(X,1),:);
    Xtest = Xall((size(X,1)+1):size(Xall,1),:);
end


function [X,Xtest] = tfidf(X,Xtest)

    Xall = [X;Xtest];

    %Xall = Xall(:,49:size(Xall,2));
    Xall = Xall(:,[1:19,8930:8949]);
    
    Xall_tf = Xall ./ repmat( sum(Xall,1), size(Xall,1), 1 );
    Xall_tf( isnan(Xall_tf) ) = 0;

    nz = sum( ( Xall > 0 ), 2 );
    Xall_idf = log( size(Xall,2) ./ (nz(:) + 1) );

    Xall = Xall_tf.*repmat(Xall_idf,1,size(Xall,2));
    %
    X = Xall(1:size(X,1),:);
    Xtest = Xall((size(X,1)+1):size(Xall,1),:);
end

>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4




