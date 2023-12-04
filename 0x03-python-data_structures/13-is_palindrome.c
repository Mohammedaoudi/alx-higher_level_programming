#include "lists.h"
#include <stddef.h>

/**
 * len_list - get the legth of a list
 * @head: the head of the list
 *
 * Return: the legth of the list
 */

int len_list(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		len++;
		head = head->next;
	}
	return (len);
}

/**
 * last_node - get the last node of a linked list
 * @head: the current head of the list
 * @mid: input
 *
 * Return: a pointer to the last node
 */

listint_t *last_node(listint_t *head, int mid)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (mid > 0)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
		mid--;
	}
	return (prev);
}

/**
 * is_palindrome - check if the list is a palindrome
 * @head: the head of the list
 *
 * Return: 0 if not 1 if yes
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *next, *first, *second;
	int len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	next = *head;
	len = len_list(current);

	while (next->next != NULL && next->next->next != NULL)
	{
		current = current->next;
		next = next->next->next;
	}

	second = last_node(current->next, len / 2);
	first = *head;
	while (second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
