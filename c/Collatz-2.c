#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <fcntl.h>

int main()
{
  int k = 0;
  int pid,status=1000;
  int f_descriptor;

  printf(" Enter  number \n");
  scanf("%d", &k);
  
  f_descriptor = shm_open("SHAREDMEMORY_", O_RDWR|O_CREAT|O_EXCL, 0);
  if(f_descriptor==-1)
  {
    perror("shm_open error");
    return 1;
  }
  ftruncate(f_descriptor,100);
  int *mem_ptr = mmap(NULL, 100, PROT_READ|PROT_WRITE, MAP_SHARED, f_descriptor, 0);  
  if(k < 0)
  {
    printf("Enter a positive number, greather than 0 \n");
    scanf("%d", &k);
  }
  
  close(f_descriptor);
  pid = fork();
  if(pid < 0)
  {
    printf(" Child Process not created \n");
    exit(-1);
  }

  else if(pid == 0)
  {
      do
      {

        if(k%2 != 0)
        {
          k = (k*3)+1;
        } 
        else if(k%2 == 0)
        {
          k= k/2;
        }
        /*printf("%d",k);*/
        *mem_ptr = k;
        mem_ptr++;
      }while(k != 1);
      
  }
  else
  {

    printf("pid %d \n",pid);
    printf("Waiting for child process to finish \n");
    wait(&status);
    do{
      printf("%d ", *mem_ptr);
      mem_ptr++;
    }while(*mem_ptr != 0);
  }  
  munmap(mem_ptr, 100);
  // Remove the shared memory region.
  shm_unlink("SHAREDMEMORY_");    
  return 0;  
}
