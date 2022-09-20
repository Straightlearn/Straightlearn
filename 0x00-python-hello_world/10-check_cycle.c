#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a list has a cycle
 * @list: current list
 * Return: 0 if no cycle, 1 if cycle
 */


int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
