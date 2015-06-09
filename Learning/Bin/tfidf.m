
function [X,Xtest] = tfidf(X,Xtest)

    Xall = [X;Xtest];

<<<<<<< HEAD
    Xall = Xall(:,51:250);
=======
    %Xall = Xall(:,49:size(Xall,2));
    Xall = Xall(:,[1:19,8930:8949]);
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    
    Xall_tf = Xall ./ repmat( sum(Xall,1), size(Xall,1), 1 );
    Xall_tf( isnan(Xall_tf) ) = 0;

    nz = sum( ( Xall > 0 ), 2 );
    Xall_idf = log( size(Xall,2) ./ (nz(:) + 1) );

    Xall = Xall_tf.*repmat(Xall_idf,1,size(Xall,2));
    %
    X = Xall(1:size(X,1),:);
    Xtest = Xall((size(X,1)+1):size(Xall,1),:);
end


