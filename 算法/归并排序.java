public class MergeSort {
    public static void main(String[] args){
        int[] a = new int[] {5,3,6,2,1,9,4,8,7};
        mergeSort(a,9);
        System.out.println();
        print(a);
    }
    public static void print(int[] data) {
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i] + "\t");
        }
        System.out.println();
    }

    // 归并排序算法, a是数组，n表示数组大小
    public static void mergeSort(int[] a, int n) {
        mergeSortInternally(a, 0, n-1);
    }

    // 递归调用函数
    private static void mergeSortInternally(int[] a, int l, int r) {
        // 递归终止条件
        if (l >= r) return;

        // 取p到r之间的中间位置q,防止（p+r）的和超过int类型最大值
        int m = l + (r - l)/2;
        // 分治递归
        mergeSortInternally(a, l, m);
        mergeSortInternally(a, m+1, r);

        // 将A[p...q]和A[q+1...r]合并为A[p...r]
        mergeBySentry(a, l, m, r);
    }

    private static void merge(int[] a, int l, int m, int r) {
        int i = l;
        int j = m+1;
        int k = 0; // 初始化变量i, j, k
        int[] tmp = new int[r-l+1]; // 申请一个大小跟a[p...r]一样的临时数组
        while (i<=m && j<=r) {
            if (a[i] <= a[j]) {//=保证了形同数据的前后顺序不变，稳定排序
                tmp[k++] = a[i++]; // i++等于i:=i+1
            } else {
                tmp[k++] = a[j++];
            }
        }

        // 判断哪个子数组中有剩余的数据,只会有一个里面有数据?只会有一个有数据
        int start = i;
        int end = m;
        if (j <= r) {
            start = j;
            end = r;
        }

        // 将剩余的数据拷贝到临时数组tmp
        while (start <= end) {
            tmp[k++] = a[start++];
        }

        // 将tmp中的数组拷贝回a[l...r],为什么这么拷贝？分割的子数组，上层的递归还会调用merge合并函数
        for (i = 0; i <= r-l; ++i) {
            a[l+i] = tmp[i];
        }
    }

    /**
     * 合并(哨兵)
     *
     * @param arr
     * @param l
     * @param m
     * @param r
     */
    private static void mergeBySentry(int[] arr, int l, int m, int r) {
        int[] leftArr = new int[m - l + 2];//多一位放哨兵
        int[] rightArr = new int[r - m + 1];//多一位放哨兵

        for (int i = 0; i <= m - l; i++) {
            leftArr[i] = arr[l + i];
        }
        // 第一个数组添加哨兵（最大值）
        leftArr[m - l + 1] = Integer.MAX_VALUE;

        for (int i = 0; i < r - m; i++) {
            rightArr[i] = arr[m + 1 + i];
        }
        // 第二个数组添加哨兵（最大值）
        rightArr[r-m] = Integer.MAX_VALUE;

        int i = 0;
        int j = 0;
        int k = l;
        while (k <= r) {
            // 当左边数组到达哨兵值时，i不再增加，直到右边数组读取完剩余值，同理右边数组也一样
            if (leftArr[i] <= rightArr[j]) {
                arr[k++] = leftArr[i++];
            } else {
                arr[k++] = rightArr[j++];
            }
        }
    }
}
