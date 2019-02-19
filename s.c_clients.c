//NTGVrzH+0WpTFh63owDROYQkvNquB9JNAJ6vmv7DOa0=
#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *archivo;
	char caracter;
	int i = 1;
	archivo = fopen("bohemian.txt","r");
	
	if (archivo == NULL)
        {
            printf("\nError de apertura del archivo. \n\n");
        }
        else
        {
            printf("\nEl contenido del archivo de prueba es \n\n");
            while((caracter = fgetc(archivo)) != EOF)
	    {
		printf("%c",caracter);
		i++;
	    }
	    printf("\n");
	    printf("numero de letras = %d", i);
        }
        fclose(archivo);
	return 0;
}

