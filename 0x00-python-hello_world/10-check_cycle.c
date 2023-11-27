#include "lists.h"

/**
 * check_cycle - check if ther is a cycle in a list
 * @list: the list to be checked
 *
 * Return: 1if ther is a cycle 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *prec = list;

	if (list == NULL)
		return (0);
	while (tmp && prec && tmp->next)
	{
		prec = prec->next;
		tmp = tmp->next->next;
		if (tmp == prec)
			return (1);
	}
	return (0);
}
