#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - A function that checks if a singly linked list
  * is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: if it is not a palindrome (0),
  * if it is a palindrome (1)
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int j = 0, len = 0, len_cycle = 0, len_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	len = listint_len(start);
	len_cycle = len * 2;
	len_list = len_cycle - 2;
	end = *head;

	for (; j < len_cycle; j = j + 2)
	{
		if (start[j].n != end[len_list].n)
			return (0);

		len_list = len_list - 2;
	}

	return (1);
}

/**
  * get_nodeint_at_index - A function that gets a node from a linked list
  * @index: The index to find in the linked list
  * @head: The head of the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iter_times == index)
				return (current);

			current = current->next;
			++iter_times;
		}
	}

	return (NULL);
}

/**
  * listint_len - Counts the number of elements in a linked list
  * @h: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t listint_len(const listint_t *h)
{
	int lenght = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}

	return (lenght);
}
