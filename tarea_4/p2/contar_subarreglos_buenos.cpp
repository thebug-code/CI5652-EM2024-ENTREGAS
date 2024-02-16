#include <iostream>
#include <vector>
using namespace std;

int contar_subarreglos_buenos(vector<int> arr) {
    int n = arr.size(); /* Tamaño del arreglo */
    int memo[2][n];     /* Arreglo para guardar la cantidad de subarreglos
                           buenos que terminan en la posición i */
    int res = n;        /* Variable para guardar el resultado */

    /* Inicializa el arreglo memo */
    memo[1][0] = 0;
    for (int i = 0; i < n; i++)
        memo[0][i] = i + 1;


    /* Para cada número i, calcula la cantidad de subarreglos buenos que
       terminan en la posición j */
    for (int i = 2; i <= n; i++) {
        for (int j = i - 1; j < n; j++) {
            if (arr[j] % i == 0)
                memo[1][j] = memo[0][j - 1] + memo[1][j - 1];
            else
                memo[1][j] = memo[1][j - 1];
        }

        res += memo[1][n - 1];

        /* Intercambia los valores de las filas */
        for (int k = 0; k < n; k++) {
            memo[0][k] = memo[1][k];
            memo[1][k] = 0;
        }
    }

    return res;
}

int main() {
    vector<int> arr = {2, 2, 1, 22, 15};
    cout << contar_subarreglos_buenos(arr) << endl;
    return 0;
}
