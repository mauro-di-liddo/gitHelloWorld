def minor(A,i,j):
    n=len(A)-1
    m=[]
    for k in range(1,n+1):
        b=[]
        if j==0:
            ii=range(1,n+1)
            for kk in ii:
                b.append(A[k][kk])
        elif j==n:
            ii=range(0,n)
            for kk in ii:
                b.append(A[k][kk])
        else:
            prec=range(0,j)
            succ=range(j+1,n+1)
            for kk in prec:
                b.append(A[k][kk])
            for kk in succ:
                b.append(A[k][kk])
        m.append(b)
    return m
    

    def determinante(A):
        det=0;
        if len(A)==1:
            return A[0][0]
        elif len(A)==2:
            return A[0][0]*A[1][1]-A[0][1]*A[1][0]
        else:
            for i in range(len(A)):
                B=minor(A,0,i)
                det=det+((-1)**(i))*A[0][i]*determinante(B)
        return det


    M=[[1,4,9,10,5],[4,1,0,2,1],[5,2,1,7,9],[9,2,1,7,9],[5,4,1,3,9]]
    determinante(M)

    C=[[1,2,3],[4,5,6],[7,8,9]]
    determinante(C)
