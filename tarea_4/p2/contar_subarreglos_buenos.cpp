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
                memo[(i - 1) & 1][j] = memo[(i - 2) & 1][j - 1] + cont;
                cont = memo[(i - 1) & 1][j];
            }
            else
                memo[(i - 1) & 1][j] = cont;
        }

        res += memo[(i - 1) & 1][n - 1];
    }

    return res;
}

int main(int argc, char const *argv[]) {
    vector<int> arr;
    if (argc > 1) {
        for (int i = 1; i < argc; i++)
            arr.push_back(atoi(argv[i]));
        cout << contar_subarreglos_buenos(arr) << endl;
        return 0;
    }
    return 1;
}
