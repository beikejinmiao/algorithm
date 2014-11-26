#include<stdio.h>

int main(){
    
    int arr_max = 12;
    int arr_min = 1;            //最小值不用设定,本程序中最小值应为0
    int arr_len = 10;           //即需要排序的数的个数
    int A[10] = {1, 12, 7, 2, 5, 1, 3, 7, 6, 8};    //original array
    int B[arr_len];    //output array
    
    int c_len = arr_max - arr_min + 1;
    //int C[c_len] = {0};       
    //数组C的长度不能设为c_len
    //因为数组C[i]的值是数组A中值为i的个数
    //就本程序的例子数组A来说...........
    int C[arr_max];// = {0};           //assistant array

    int i;
    for(i = 0; i <= arr_max; i++){
        C[i] = 0;
    }
    //C统计 值为i 的个数
    for(i = 0; i < arr_len; i++){
        C[A[i]] += 1;
    }
    
    //C中保存的值是 值为i 应该在B中的位置
    for(i = 1; i <= arr_max; i++){
        C[i] = C[i] + C[i-1];
    }
    //因为数组下标从0开始,所以将C中的值都减去1
    for(i = 0; i <= arr_max; i++){
       C[i] -= 1;
    }
    //构造输出数组B   
    for(i = arr_len-1; i >= 0; i--){
        B[C[A[i]]] = A[i];      //
        C[A[i]] -= 1;
    }

    for(i = 0; i < arr_len; i++)
        printf("%d\t", B[i]);
    printf("\n");

    return 0;
}

