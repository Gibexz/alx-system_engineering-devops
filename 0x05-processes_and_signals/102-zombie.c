#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * infinite_while - function that containts an infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main -vEntry point
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("fork error");
			exit(1);
		}
		else if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
