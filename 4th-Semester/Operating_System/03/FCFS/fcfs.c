#include<stdio.h>

#define max 30

main()
{
    int i,j,n,t,p[max],bt[max],tat[max],wt[max];
    float awt = 0, atat = 0;
    printf("Enter the no. of process :");
    scanf("%d",&n);
    printf("Enter the process number : ");
    for(i = 0; i<n; i++)
    {
        scanf("%d",&p[i]);
    }
    printf("Enter the burst time : ");
    for(i=0; i<n; i++)
    {
        scanf("%d",&bt[i]);
    }
    printf("process\t Burst Time\tWaiting Time\tTurnaround Time\n");
    for(i = 0; i<n; i++)
    {
        wt[i] = 0;
        tat[i] = 0;
        for(j = 0; j< i; j++)
        {
            wt[i] = wt[i] + bt[j];
        }
        tat[i] = wt[i] + bt[j];
        awt = awt + wt[i];
        atat = atat + tat[i];
        printf("%d\t\t%d\t\t%d\t\t%d\n",p[i],bt[i],wt[i],tat[i]);
    }
    awt = awt/n;
    atat = atat/n;
    printf("Average Waiting Time = %f\n",awt);
    printf("Average Turnaround Time = %f",atat);
}
