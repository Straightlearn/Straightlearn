#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inset a node into a sorted singly linked list
 * @head: head node
 * @number: number to be added
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current;

	current = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (*head == NULL)
		*head = newnode;
	else if (current->n > number)
	{
		newnode->next = current;
		current = newnode;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n >= number)
			{
				newnode->next = current->next;
				current->next = newnode;
				break;
			}
			current = current->next;
		}
	}
	return (newnode);

}
