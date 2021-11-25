#include "lists.h"
#include <stdlib.h>
/**
* check_cycle - Checks if a singly linked list contains a cycle
* @list: a singly-linked list
*
* Return: If there is no cycle  return 0 else 1
*/
int check_cycle(listint_t *list)
{
	listint_t *Fast, *Slow;

	if (list == NULL || list->next == NULL)
		return (0);

	Slow = list->next;
	Fast = list->next->next;

	while (Slow && Fast && Fast->next)
	{
		if (Slow == Fast)
			return (1);
		Slow = Slow->next;
		Fast = Fast->next->next;
	}
	return (0);
}
