#include <bits/stdc++.h>
using namespace std;
#define MAX 5
#define MAX_THREAD 10
int matrixA[MAX][MAX];
int matrixB[MAX][MAX];
int matrixC[MAX][MAX];
int matrixD[MAX][MAX];
int matrixE[MAX][MAX];
int matrixF[MAX][MAX];
int matrixG[MAX][MAX];
int matrixH[MAX][MAX];
int matrixY[MAX][MAX];
int step_i = 0;
void* multi(void* arg)
{
int i = step_i++; 
for (int j = 0; j < MAX; j++)
for (int k = 0; k < MAX; k++)
matrixY[i][j] += matrixA[i][k] * matrixB[k][j] * matrixC[k][j] * matrixD[k][j] * matrixE[k][j] * matrixF[k][j] * 
matrixG[k][j] * matrixH[k][j];
}
int main()
{
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++) {
matrixA[i][j] = rand() % 10;
matrixB[i][j] = rand() % 10;
matrixC[i][j] = rand() % 10;
matrixD[i][j] = rand() % 10;
matrixE[i][j] = rand() % 10;
matrixF[i][j] = rand() % 10;
matrixG[i][j] = rand() % 10;
matrixH[i][j] = rand() % 10;
}
}
cout << endl
<< "Matrix A" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixA[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix B" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixB[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix C" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixC[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix D" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixD[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix E" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixE[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix F" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixF[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix G" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixG[i][j] << " ";
cout << endl;
}
cout << endl
<< "Matrix H" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixH[i][j] << " ";
cout << endl;
}
pthread_t threads[MAX_THREAD];
for (int i = 0; i < MAX_THREAD; i++) {
int* p;
pthread_create(&threads[i], NULL, multi, (void*)(p));
}
for (int i = 0; i < MAX_THREAD; i++)
pthread_join(threads[i], NULL);
cout << endl
<< "Matrix Y =" << endl;
for (int i = 0; i < MAX; i++) {
for (int j = 0; j < MAX; j++)
cout << matrixY[i][j] << " ";
cout << endl;
}
return 0;
}