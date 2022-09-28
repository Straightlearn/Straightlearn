#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: list head
 * Return: 1 if true else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *backward = *head, *tmp;

	backward 
	/*while (current->next != NULL)
	{*/
		tmp = current;
		current = current->next;

		printf("c - %d, t - %d, b - %d\n", current->n, tmp->n, backward->n);
	//}
	/*
	current = *head;
	while (i < size)
	{
		if (forward[i] != current->n)
		{
			free(forward);
			return (0);
		}
		i++;
		current = current->next;
	}
	free(forward);*/
	return (1);
}
