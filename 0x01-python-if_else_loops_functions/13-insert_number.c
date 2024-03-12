#include "lists.h"

/**
 * insert_node - inserts number in a sorted linked list
 * @head: pointer to list
 * @number: number to be inserted
 * Return: address of inserted list, NULL on failure
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp_fast, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return NULL;
	if (*head == NULL)
	{
		newnode->next = NULL;
		newnode->n = number;
		*head = newnode;
	}

	temp = temp_fast = *head;
	while (temp_fast->next != NULL && temp_fast->n < number)
	{
		temp = temp_fast;
		temp_fast = temp_fast->next;
	}

	if (temp_fast == *head && temp_fast->n > number)
	{
		newnode->next = temp_fast;
		*head = newnode;
		newnode->n = number;
	}
	else
	{
		if (temp_fast->next == NULL && temp_fast->n < number)
		{
			temp = temp_fast;
			temp_fast = NULL;
		}
		temp->next = newnode;
		newnode->next = temp_fast;
		newnode->n = number;
	}

	return (newnode);
}
