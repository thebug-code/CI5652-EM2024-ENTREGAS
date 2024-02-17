#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

class VirtualInitClient {
    public:
        VirtualInitClient(size_t size) : n(size) {
            T = new int[n];
            a = new int[n];
            b = new int[n];
            ctr = 0;
        }

        ~VirtualInitClient() {
            delete[] T;
            delete[] a; 
            delete[] b;
        }
        
        void run_simulation();
        int* asignar_pos_val(unsigned i, int val);
        int* consultar_pos(unsigned i);
        
        // Utilidades
        vector<string> split(const string &text, char sep);
        string upper(string strToConvert);
        void usage();
    

    private:
        size_t n;
        unsigned ctr;
        int* T;
        int* a;
        int* b;
};

void VirtualInitClient::run_simulation() {
    string opt, t0;
    int* val;

    while(1) {
        cout << "Ingrese la operacion a realizar: ";
        getline(cin, opt);

        // Split the string
        vector<string> tokens = split(opt, ' ');

        // Convertir a mayusculas
        t0 = upper(tokens[0]);

        if (t0 == "ASIGNAR") {
            if (tokens.size() != 3) {
                cout << "Error: formato incorrecto" << endl;
                usage();
                continue;
            }

            if (!asignar_pos_val(stoi(tokens[1]), stoi(tokens[2])))
                continue;

            asignar_pos_val(stoi(tokens[1]), stoi(tokens[2]));
        } else if (t0 == "CONSULTAR") {
            if (tokens.size() != 2) {
                cout << "Error: formato incorrecto" << endl;
                usage();
                continue;
            }

            val = consultar_pos(stoi(tokens[1]));
            if (val == NULL) continue;
            cout << "Valor: " << *val << endl;

        } else if (t0 == "LIMPIAR") {
            delete[] T;
            delete[] a;
            delete[] b;
            T = new int[n];
            a = new int[n];
            b = new int[n];
            ctr = 0;
            cout << "Tabla limpiada" << endl;
        } else if (t0 == "SALIR") {
            cout << "Saliendo..." << endl;
            return;
        } else {
            cout << "Error: operacion no valida" << endl;
            usage();
        }
    }
}


/*
 * Asigna un valor a una posicion
 * @param i: posicion a asignar
 * @param val: valor a asignar
 * @return EXIT_SUCCESS si la asignacion fue exitosa, NULL en caso contrario
 */
int* VirtualInitClient::asignar_pos_val(unsigned i, int val) {
    if (i < 0 || i >= n) {
        cout << "Error: i fuera de rango" << endl;
        return NULL;
    }

    T[i] = val;
    a[ctr] = i;
    b[i] = ctr;
    ctr++;

    cout << "Asignacion exitosa" << endl;
    return EXIT_SUCCESS;
}



/*
 * Consulta el valor en la posicion i
 * @param i: posicion a consultar
 * @return valor en la posicion i
 */
int* VirtualInitClient::consultar_pos(unsigned i) {
    if (i < 0 || i >= n) {
        cout << "Error: i fuera de rango" << endl;
        return NULL;
    }

    if (0 <= b[i] && b[i] <= (int)ctr) {
        if (a[b[i]] == (int)i)
            return &T[i];
    }


    cout << "La posicion " << i << " no ha sido inicializada" << endl;
    return NULL;
}


/* Separa un string en tokens usando un delimitador
 * @param text: string a separar
 * @param sep: delimitador
 * @return vector con los tokens
 */
vector<string> VirtualInitClient::split(const string &text, char sep) {
  vector<string> tokens;
  size_t start = 0, end = 0;

  while ((end = text.find(sep, start)) != std::string::npos) {
    tokens.push_back(text.substr(start, end - start));
    start = end + 1;
  }

  tokens.push_back(text.substr(start));
  return tokens;
}

/*
 * Convierte un string a mayusculas
 * @param str: string a convertir
 * @return string convertido
 */
string VirtualInitClient::upper(string str) {
    for (auto & c: str) c = toupper(c);
    return str;
}

/*
 * Muestra el uso del programa
 */
void VirtualInitClient::usage() {
    cout << "Uso: " << endl;
    cout << "ASIGNAR <POS> <VAL>: Asigna el valor VAL a la posicion POS" << endl;
    cout << "CONSULTAR POS: Consulta el valor en la posicion POS" << endl;
    cout << "LIMPIAR: Limpia la tabla, eliminando todos los valores" << endl;
    cout << "SALIR: Termina la ejecucion" << endl;
}

int main(int argc, char* argv[]) {
    int n;
    if (argc != 2) {
        cout << "Error: formato incorrecto" << endl;
        cout << "Uso: ./runVirtualInitClient" << " <n>" << endl;
        return EXIT_FAILURE;
    }

    n = atoi(argv[1]);
    VirtualInitClient* vic = new VirtualInitClient(n);
    vic->run_simulation();
    delete vic;

    return 0;     
}
