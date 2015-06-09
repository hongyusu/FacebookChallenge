function Yprobsvm = clear_prob(Ytr,Yprobsvm)
    if Ytr(1) == 0
        Yprobsvm = Yprobsvm(:,2);
    end
    if Ytr(1) == 1
        Yprobsvm = Yprobsvm(:,1);
    end
end


