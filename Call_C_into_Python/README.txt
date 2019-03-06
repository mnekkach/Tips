# Call C program into python code


## On Windows OS

1. Create a C program (main.c) for example :

```C
#include <stdio.h>
#include <stdlib.h>

int main()
{
    return 0;
}
int triple(int nombre)
{
    int resultat = 0;

    resultat = 3 * nombre;
    return resultat;
}
```


2. Compile it with the command :

> gcc -c -m32 main.c

gcc create a main.o file

3. Create a dll file with the command :

> gcc -m32 -shared -o main.dll main.o

gcc create main.dll

### Remark
==========
-m32 flag is used because I have python 2.7 32 bits and gcc compile 64 bits program by default.
It is not possible to call dll compiled in 64 bits by python 32 bits

4. Call dll in Python program

```python
import ctypes
main = ctypes.CDLL(path_of_dll_file)
f = main.triple(3)
```
