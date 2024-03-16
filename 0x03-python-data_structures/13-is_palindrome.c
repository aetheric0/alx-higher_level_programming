#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome -  Determines if a linked list is a palindrome
 * @head: Pointer to linked list
 * Return: 0 if palindrome, 1 if not
 **/

int is_palindrome(listint_t **head)
{
	int i, counter = 0;
	listint_t *temp, *prev_node, *next_node, *current_node;

	if ((*head)->next == NULL)
		return (0);
	temp = prev_node = current_node = next_node = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		counter++;
	}
	if (counter % 2 != 0)
		return (1);

	temp = *head;
	counter = (counter / 2);
	for (i = 0; i <= counter; i++)
		temp = temp->next;

	/* Reversing first-half of the list for comparison */
	reverse_list(current_node, prev_node, next_node, counter);

	/* Checks if list is not a Palindrome */
	while (current_node != NULL)
	{
		if (current_node->n != temp->n)
			return (1);
		current_node = current_node->next;
		temp = temp->next;
	}

	return (0);
}

/**
 * reverse_list - Reverses a list from a given point
 * @current_node: Tointer to head of list
 * @prev_node: To hold address of previous node while reversing
 * @next_node: To hold address of next node while reversing
 * @counter: Iterator for half-list
 **/

void reverse_list(listint_t *current_node, listint_t *prev_node,
		  listint_t *next_node, int counter)
{
	int i = 0;

	while (i < counter)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
		i++;
	}
}
