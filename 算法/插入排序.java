import java.util.Arrays;

public class InsertSort {
    public static void main(String[] args) {
        int[] a = {9,2,3,4,5,6};
        InsertSort(a,6);
        System.out.println(Arrays.toString(a));
    }
    public  static void InsertSort(int[] a, int n){
        if(n<=1) return;
        for(int i = 1; i < n;i++){
            int value = a[i];
            int j = i-1;
            for(;j >= 0;j--){
                if (a[j]>value){
                    a[j+1] = a[j];
                }
                else break;
            }
            a[j+1] = value;
        }

    }
}
