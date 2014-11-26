public class RadixSort {
	private static int N = 7;		//待排序元素个数
	private static int D[] = {13, 343, 9006, 29, 9, 112, 326};
	private static int RADIX = 10;	//基数
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		RadixSort rs = new RadixSort();
		int word_len = 4;		//需要指出数组元素最大长度
		int base = RADIX;
		int A[] = new int[N];
		int TMP[] = D; 
		int i = 0;
		while(word_len > 0){
			for(i = 0; i< N; i++){
				A[i] = TMP[i] % base;
				A[i] = A[i] * 10 / base;
			}
			
			TMP = rs.counting_sort(A, TMP, N, base);
			base *= RADIX; 
			word_len--;
		}
		
		for (int j = 0; j < TMP.length; j++) {
			System.out.print(TMP[j]+ "\t");
		}
		System.out.println();
	}
	
	
	private  int[] counting_sort(int[] A, int[] D, int n, int base){
		int k = base;
		int B[] = new int[n];
		int C[] = new int[k];
		int i;
		for(i=0; i<k; i++){
			C[i] = 0;
		}
		for(i=0; i<n; i++){
			C[A[i]]++;
		}
		for(i=1; i<k; i++){
			C[i] += C[i-1]; 
		}
		for(i=n-1; i>=0; i--){		//必须从高位到低位，为了保证稳定性；要不然相同的数会交换顺序。
			B[C[A[i]]-1] = D[i];
			C[A[i]]--;
		}
		
		return B;
	}

}
