#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

//Function to be executed by the first thread
void * thread_function1(void*arg)
{
    for(int i = 0; i<5; i++)
    {
        printf("Thread1 is running : iteration %d\n",i);

        sleep(1);
    }
    return NULL;
}

//Function to be executed by the first thread
void * thread_function2(void*arg)
{
    for(int i = 0; i<5; i++)
    {
        printf("Thread2 is running : iteration %d\n",i);

        sleep(1);
    }
    return NULL;
}
int main()
{
    pthread_t thread1,thread2;

    if(pthread_create(&thread1,NULL,thread_function1,NULL)!=0)
    {
        perror("Failed to create thread1");

        return 1;
    }

    if(pthread_create(&thread2,NULL,thread_function1,NULL)!=0)
    {
        perror("Failed to create thread2");

        return 1;
    }

    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);

    printf("Both threads have finished execution!!\n");

    return 0;
}
