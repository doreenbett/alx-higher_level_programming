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
	const listint_t *ptr;
	unsigned int n;

	ptr = h;
	n = 0;
	while (ptr != NULL)
	{
		printf("%i\n", ptr->n);
		ptr = ptr->next;
		n++;
	}
	return (n);
}
/**
* add_nodeint - adds a new node at the beginning of a listint_t list
* @head: pointer to a pointer of the start of the list
* @n: integer to be added int the node
* Return: address of the new element or NULL if it fails
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	newnode->next = *head;
	*head = newnode;
	return (newnode);
}
/**
* free_listint - frees a listint_t list
* @head: pointer to list to be freed
* Return: void
*/
void free_listint(listint_t *head)
{
	listint_t *ptr;

	while (head != NULL)
	{
		ptr = head;
		head = head->next;
		free(ptr);
	}
}
