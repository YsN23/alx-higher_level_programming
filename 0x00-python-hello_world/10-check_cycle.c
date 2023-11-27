#include "lists.h"

/**
* check_cycle - checks if we have a cycle in a Linked List
* @list: head of the Linked List
* Return: 1 if we have a cycle, 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
