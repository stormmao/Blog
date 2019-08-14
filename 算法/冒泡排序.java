import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] a = {9,2,3,4,5,6};
        BubbleSort(a,6);
        System.out.println(Arrays.toString(a));
    }
    public static void  BubbleSort(int[] array, int n){
        if(n<=1) return ;
        boolean flag = false;//放在循环里是不是更好
        for (int i = 0;i < n;i++){
            for (int j = 0;j< n-1-i;j++){
                if(array[j]>array[j+1]){
                    int tmp = array[j+1];
                    array[j+1] = array[j];
                    array[j] = tmp;
                    flag = true;
                }
            }
            if(!flag) break;
        }

    }
}
