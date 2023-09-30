#include <iostream>
using namespace std;

int main() {
    int ano;

    cout << "Ingrese un ano: ";
    cin >> ano;

    if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0)) {
        cout << ano << " es un año bisiesto." << endl;
    } else {
        cout << ano << " no es un año bisiesto." << endl;
    }

    return 0;
}