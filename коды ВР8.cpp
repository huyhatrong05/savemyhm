#include <iostream>
#include <vector>
using namespace std;

int array_sum(vector<int> arr) {
    if (arr.empty()) {
        return 0;
    }
    int first = arr[0];
    arr.erase(arr.begin());
    return first + array_sum(arr);
}

// Пример использования
int main() {
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << array_sum(nums) << endl;  // Вывод: 15
    return 0;
}
