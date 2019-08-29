本地编译器可以跑
import java.util.Arrays;

public class Practice{
    public static void reOrderArray(int [] array) {
        int [] a = new int[array.length];
        int k = 0;
        int m = array.length-1;
        for(int i=0;i< array.length;++i){
            if(array[i]%2==1){
                a[k] = array[i];
                k++;
            }
        }
        for(int j=array.length-1;j>=0;j--){
            if(array[j]%2==0){
                a[m] = array[j];
                m--;
            }
        }
        for(int i = 0;i<array.length;i++){
            array[i]=a[i];
        }
    }
    public static void main(String[] args){
        int a[] = {};
//        System.out.println(reOrderArray(a));
        int b[] = {1,3};
        reOrderArray(a);
        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(b));
    }

}

牛客网上会报错，数组访问越界
处理数组为空时的情况
public class Solution {
    public void reOrderArray(int [] array) {
        int [] a = new int[array.length];
        
        int k = 0;
        int m = array.length-1;
        if (m<0){m=0;}
        for(int i=0;i< array.length;++i){
            if(array[i]%2==1){
                a[k] = array[i];
                k++;
            }
        }
        for(int j=array.length-1;j>=0;j--){
            if(array[j]%2==0){
                if (j<0){j=0;}
                a[m] = array[j];
                m--;
            }
        }
        for(int i=0;i<array.length;i++){
            array[i] = a[i];
        }
    }
}
