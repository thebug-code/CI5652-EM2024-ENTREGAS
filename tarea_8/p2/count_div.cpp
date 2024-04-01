#include <iostream>
#include <vector>
using namespace std;

pair<int, int> count_div(int n) {
    int max_val, max_x;
    
    // Inicializa el arreglo cnt con 0.
    vector<int> cnt(n + 1, 0);
    
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            cnt[j]++; // Aquí cnt[x] representa la cantidad de divisores de x

            if (cnt[i] > max_val) {
                max_val = cnt[i];
                max_x = i;
            }
        
        }
    }
    return {max_x, max_val};
}

int main() {
    int n;
    cin >> n;

    auto r = count_div(n);

    printf("El máximo valor para decomp(X) donde 1 ≤ X ≤ %d es %d para X = %d.\n", n, r.second, r.first);
    return 0;
}