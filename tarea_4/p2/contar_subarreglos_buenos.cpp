#include <iostream>
#include <vector>
using namespace std;

int contar_subarreglos_buenos(vector<int> arr) {
    int n = arr.size(); /* Tamaño del arreglo */
    int memo[2][n];     /* Arreglo para guardar la cantidad de subarreglos
                           buenos que terminan en la posición i */
    int res = n;        /* Variable para guardar el resultado */
    int cont = 0;       /* Contador para subarreglos buenos */

    /* Inicializa el arreglo memo */
    for (int i = 0; i < n; i++)
        memo[0][i] = i + 1;


    /* Para cada número i, calcula la cantidad de subarreglos buenos que
       terminan en la posición j */
    for (int i = 2; i <= n; i++) {
        cont = 0;
        for (int j = i - 1; j < n; j++) {
            if (arr[j] % i == 0) {
                memo[(i - 1) % 2][j] = memo[(i - 2) % 2][j - 1] + cont;
                cont = memo[(i - 1) % 2][j];
            }
            else
                memo[(i - 1) % 2][j] = cont;
        }

        res += memo[(i - 1) % 2][n - 1];
    }

    return res;
}

int main() {
    vector<int> arr = {2, 2, 1, 22, 15};
    cout << contar_subarreglos_buenos(arr) << endl;
    return 0;
}
