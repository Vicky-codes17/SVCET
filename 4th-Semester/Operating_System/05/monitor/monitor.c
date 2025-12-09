#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

#define MAX_PORTS 3

pthread_mutex_tport_mutex;
pthread_cond_tports_avilable;

int available_ports = MAX_PORTS;
void open_port(int process_id)
{
    pthread_mutex_lock(&port_mutex);

    while(available_ports == 0)
    {
        printf("Process %d: No ports available. Waiting..\n",process_id);
        pthread_cond_wait(&ports_available,&port_mutex);
    }
    available_ports--;
    printf("Process %d: Port opened.Available ports: %d\n",process_id,available_ports);

    pthread_mutex_unlock(&port_mutex);
}

void close_port(int process_id)
{
    pthread_mutex_lock(&port_mutex);
    available_ports++;

    printf("Process %d: Port closed.Available ports : %d\n",process_id,available_ports);

    pthread_cond_signal(&ports_available);
    pthread_mutex_unlock(&port_mutex);
}

void*process(void*arg)
{
    int process_id = *(int*)arg;
    open_port(process_id);

    sleep(2);

    close_port(process_id);
    return NULL;
}

int main()
{
    pthread_t threads[5];

    int process_ids[5] = {1,2,3,4,5};
    pthread_mutex_init(&port_mutex,NULL);
    pthread_cond_init(&ports_available,NULL);
    for(int i=0; i<5; i++)
    {
        pthread_create(&threads[i],NULL,process,(void*)&process_ids[i]);
    }
    for(int i=0; i<5; i++)
    {
        pthread_join(threads[i],NULL);
    }

    pthread_mutex_destroy(&port_mutex);
    pthread_cond_destroy(&ports_available);

    return 0;
}
