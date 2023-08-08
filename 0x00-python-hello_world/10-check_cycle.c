#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list has
 * a cycle in it or not.
 * @list: The pointer to the begining of the node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *current, *checker;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	checker = current->next;

	while (current != NULL && checker->next != NULL
			&& checker->next->next != NULL)
	{
		if (current == checker)
			return (1);
		current = current->next;
		checker = checker->next->next;
	}

	return (0);
}
