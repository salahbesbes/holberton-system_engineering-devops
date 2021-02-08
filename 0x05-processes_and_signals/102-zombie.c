#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
  * infinite_while - infinite_while
  * Return: int
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
  * main - create 5 zombi process
  * Return: int
  */
int main(void)
{
	int i = 0;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
		{
			return (0);;
		}
		printf("Zombie process created, PID: %d\n", child);
	}
	infinite_while();
	return (1);
}
