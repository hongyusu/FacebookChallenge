<<<<<<< HEAD




=======
>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
function [X,Xtest] = centering(X,Xtest)
    % centering
    Xall = [X;Xtest];

<<<<<<< HEAD
    Xall = [Xall(:,[2:4:29]),Xall];
    %Xall = Xall(:,51:250);
    
=======
    Xall = Xall(:,[1:49,8930:8949]);

>>>>>>> 778a41c7a7cd7219df5fe07207aea18548672de4
    Xall = Xall - repmat(mean(Xall),size(Xall,1),1);
    Xall = Xall ./ repmat(std(Xall),size(Xall,1),1);
    %
    X = Xall(1:size(X,1),:);
    Xtest = Xall((size(X,1)+1):size(Xall,1),:);
end


