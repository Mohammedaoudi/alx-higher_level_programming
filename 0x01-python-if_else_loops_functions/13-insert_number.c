#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linekd list
 * @head: the head of the list
 * @number: the content of the node to be added
 *
 * Return: the address of the nouv node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prec;
	listint_t *next, *nouv;

	if (head == NULL)
		return (NULL);

	nouv = malloc(sizeof(listint_t));
	if (nouv == NULL)
		return (NULL);

	nouv->n = number;
	if (*head == NULL)
	{
		nouv->next = *head;
		*head = nouv;
		return (*head);
	}
	prec = *head;
	next = prec->next;
	while (prec != NULL)
	{
		if (number >= prec->n)
		{
			if (next == NULL || number <= next->n)
			{
				prec->next = nouv;
				nouv->next = next;
				return (*head);
			}
		}
		else
		{
			*head = nouv;
			nouv->next = prec;
			return (*head);
		}
		prec = prec->next;
		next = prec->next;
	}
	return (*head);
}
