#include<stdio.h>

int *counting_sort(int A[], int D[], int n, int base){
    //int n = strlen(A);    //Error: strlen(char *)
    int k = base;
    int C[k];
    int B[n];               //Error:没有新建数组
    int *bp = B;
    int i;

    for(i = 0; i < k; i++){
        C[i] = 0;
    }
    for(i = 0; i < n; i++){
        C[A[i]]++;    
    }  
    for(i = 1; i < k; i++){
        C[i] += C[i-1];
    }
    for(i = 0; i < n; i++){     //Error:必须逆序遍历数组A【i从n-1到0】
        B[C[A[i]] -1] = D[i];
        C[A[i]]--;
    }
 
    return bp;
}


int main(){
    int n = 7;
    int D[7] = {123, 53, 456, 99, 90, 12, 326};
    int *dp = D;
    int A[n];
    int word_len = 3;   //数的最大长度
    int base = 10;      //10进制
    int i;

    while(word_len){        

        for(i = 0; i < n; i++){
            A[i] = *(dp+i) % base;
            A[i] = A[i]*10 / base;
        }
        dp = counting_sort(A, dp, n, 10);       
        
        base *= base;        //Error
        word_len --;
    }

    for(i = 0; i < n; i++){
        printf("%d\t", *(dp+i));
    }
    printf("\n");

    return 0;
}


