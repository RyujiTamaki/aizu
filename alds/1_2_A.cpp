#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int bubbleSort(vector<int> &A, int N) {
    int sw = 0;
    bool flag = true;
    int i = 0;
    while (flag) {
        flag = false;
        for (int j = N - 1; j >= i + 1; j--) {
            if (A[j] < A[j - 1]) {
                swap(A[j], A[j - 1]);
                flag = true;
                sw++;
            }
        }
        i++;
    }
    return sw;
}

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    rep(i, N) cin >> A[i];

    int sw = bubbleSort(A, N);

    rep(i, N) {
        if (i > 0) cout << " ";
        cout << A[i];
    }
    cout << endl;
    cout << sw << endl;
}
