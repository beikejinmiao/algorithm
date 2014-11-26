#include<stdio.h>
#define allocate_space(n)  (int *)calloc(n, sizeof(int))
int *B = NULL;
int *counting_sort(int A[], int D[], int n, int base){
    //int n = strlen(A);    //Error: strlen(char *)
    int k = base;
    int C[k];
    //int B[7] = {0};
    //int B[n];         //Error: 没有创建新数组
    B = allocate_space(n);    
    //int *B = allocate_space(n); 
    //Warning:
    //counting_sort执行完后该空间会被释放，可能会被其他程序占用
    //在main中引用这块空间可能会出现错误
    //建议使用静态变量或者全局变量
    printf("B:%p\n",B);
    //int *bp = B;
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
    for(i = n-1; i >= 0; i--){
        //Error:
        //若创建数组B时，使用 "int B[n];"的方式，那么
        //第二遍及之后的循环中,dp、bp、D、B指针全部指向同一个数组;
        //所以此处" B[C[A[i]] -1] = D[i]; "会出现错误
        B[C[A[i]] -1] = D[i];
        C[A[i]]--;
    }
    
    //return bp;
    return B;
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
        //counting_sort方法中若创建数组B时，使用 "int B[n];"的方式，那么
        //第二遍及之后的循环中,dp指针指向在方法counting_sort中创建的数组B;
        dp = counting_sort(A, dp, n, 10);      
        //base *= base;        //Error
        base *= 10;
        word_len --;
    }
    for(i = 0; i < n; i++){
        printf("%d\t", *(dp+i));
    }
    printf("\n");

    return 0;
}


