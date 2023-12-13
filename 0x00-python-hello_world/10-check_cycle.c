#include "lists.h"
/**
 * check_cycle - linked list check
 * @list: start of list
 *
 * checks if list has cycle
 *
 * Return: 0 if no cycle
 * 1 if cycle
 */
int check_cycle(listint_t *list)
{
	int has_cycle = 0, is_initial = 0;
	listint_t *slow = list, *fast = list;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast && is_initial != 0)
		{
			has_cycle = 1;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;
		is_initial = 1;
	}
	return (has_cycle);
}