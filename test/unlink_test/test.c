#include <stdio.h>
#include <dmtcp.h>

#define filename "tmpfile"
int main(int argc, char** argv)
{

    FILE* thefile = fopen(filename, "w");
    unlink(filename);
    int i=0;
    for (i=0; i < 10; i++)
    {
        printf("%d\n", i); 
        if (i == 5){ dmtcp_checkpoint();}
        fprintf(thefile, "%d\n", i); 
        fflush(thefile);
        
    }
    fclose(thefile);

}
