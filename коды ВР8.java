import java.util.Arrays;

public class Main {
    public static int arraySum(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }
        return arr[0] + arraySum(Arrays.copyOfRange(arr, 1, arr.length));
    }
    
    // Пример использования
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        System.out.println(arraySum(nums));  // Вывод: 15
    }
}
