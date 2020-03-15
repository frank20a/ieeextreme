#include <iostream>

using namespace std;

static unsigned long int F[400000000] = {0};

unsigned long long int fibo(unsigned long int i){
    if (i == 0) return 0;
    if (i == 1) return 1;
    if (i < 400000000){
	    if (F[i] == 0) F[i] = fibo(i-1) + fibo(i-2);
	    return F[i];
	} else {
		return fibo(i-1) + fibo(i-2);
	}
}


int main() {
    unsigned long int n, t;
    cin >> n;
    for (unsigned long int i = 0; i < n; i++){
        cin >> t;
        cout << fibo(t+1);
    }
    return 0;
}
