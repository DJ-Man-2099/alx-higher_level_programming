#include "lists.h"
/**
 * insert_node - linked list function
 * @head: first node
 * @number: number added
 *
 * inserts node in sorted linked list
 *
 * Return: address of new node
 * or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before_new_node = *head, *new_node = NULL;

	if (before_new_node->n >= number)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->next = before_new_node;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}
	while (before_new_node != NULL)
	{
		if ((before_new_node->next != NULL && before_new_node->next->n >= number) ||
			(before_new_node->next == NULL && before_new_node->n < number))
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				break;
			new_node->next = before_new_node->next;
			new_node->n = number;
			before_new_node->next = new_node;
			break;
		}
		before_new_node = before_new_node->next;
	}
	return (new_node);
}
