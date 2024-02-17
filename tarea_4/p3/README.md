# Inicializador Virtual de Arreglos

Programa cliente desarrollado en `c++` que permite probar el proceso de inicialización virtual de arreglos de forma iterativa.

## Características

- **Inicialización:** Al invocarse, el programa recibe como argumento del sistema el tamaño del arreglo a utilizar.

- **Indexación:** El arreglo es indexado a partir de cero, es decir, las posiciones válidas para un arreglo de tamaño `n` van desde `0` hasta `n-1`.

- **Opciones del Cliente:**
  1. **ASIGNAR POS VAL:** Permite asignar el valor VAL en la posición POS del arreglo. Se reportará un error si la posición POS no es válida.
  
  2. **CONSULTAR POS:** Informa si la posición POS está inicializada o no. Si está inicializada, devuelve el valor asociado a esa posición. Se reportará un error si la posición POS no es válida.

  3. **LIMPIAR:** Limpia la tabla, dejando todas las posiciones sin inicializar.

  4. **SALIR:** Finaliza el programa.

## Compilación y Ejecución

Para compilar el programa, simplemente ejecuta el siguiente comando:

```bash
make
```

Posteriormente, ejecute el siguiente comando, donde `<n>` es el tamaño del arreglo T:

```bash
./runVirtualInitClient <n>
```
