#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
listint_t *insert_node(listint_t **head, int number);

#endif
