#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

void trace(vector<int> A, int N) {
    rep(i, N) {
        if (i > 0) printf(" ");
        printf("%d", A[i]);
    }
    printf("\n");
}

// O(N^2) データが降順に並んでいるとき
// O(N) データが昇順に並んでいるとき
// ある程度整列されたデータに対しては高速に動作する
void insertionSort(vector<int> A, int N) {
    for (int i = 1; i < N; i++) {
        // i: 未ソートの部分列の戦闘を示すループ変数
        // v: A[i]の値を一時的に保持しておくための変数
        // j: ソート済み部分列からvを挿入するための位置を探すループ変数
        int v = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > v) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = v;
        trace(A, N);
    }
}



int main() {
    int N;
    vector<int> A;
    cin >> N;
    A.resize(N);
    rep(i, N) cin >> A[i];

    trace(A, N);
    insertionSort(A, N);
}
