#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>

#define MAX_PORTS 3

sem_tports_semaphore;

void*open_port(void*arg)
{
    printf("Process %ID : Trying to open a  port...\n",(long)arg);

     sem_wait(&ports_semaphore);

    printf("Process %ID : Port opened successfully..\n",(long)arg);

    sleep(2);

    printf("Process %ID : closing port ...\n",(long)arg);

    sem_post(&ports_semaphore);

    return NULL;
}
int main()
{
    pthread_tthreads[5];
    sem_init(&ports_semaphore,0,MAX_PORTS);

    for(long i =0; i<5; i++)
    {
        pthread_create(&threads[i],NULL,open_port(void*)i);
    }
    for(int i =0; i<5; i++)
    {
        pthread_join(threads[i],NULL);
    }
    sem_destroy(&ports_semaphore);

    return 0;
}
