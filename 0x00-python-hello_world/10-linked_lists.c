#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *temp;
    unsigned int nbr; /* number of nodes */

    temp = h;
    nbr = 0;
    while (temp != NULL)
    {
        printf("%i\n", temp->num);
        temp = temp->next;
        nbr++;
    }

    return (nbr);
}

/**
 * add_nodeint - adds a nouv node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the nouv element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *nouv;

    nouv = malloc(sizeof(listint_t));
    if (nouv == NULL)
        return (NULL);

    nouv->num = n;
    nouv->next = *head;
    *head = nouv;

    return (nouv);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
