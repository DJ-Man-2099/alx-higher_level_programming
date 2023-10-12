#include "lists.h"
/**
 * print_dlistint - dlinklist function
 * @h: head of list
 *
 * prints contents of list
 *
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count;
	const dlistint_t *current = h;

	for (count = 0; current != NULL; count++)
	{
		printf("%d\n", current->n);
		current = current->next;
	}
	return (count);
}
