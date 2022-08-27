#include "lists.h"
/**
 * insert_node  - insert listint_t according to sorted linked list
 * @head: next that store the address of the head next
 * @number: value to insert in the linked list
 *
 * Return: return the address of the new memory allocated
 */
listint_t *insert_node(listint_t **head, int value)
{
	listint_t *ptr = NULL ;
    listint_t *temp=NULL;
    ptr = malloc(sizeof(listint_t));
    ptr -> n =value;
    ptr-> next=NULL;
    temp=*head;
    
    if (temp->n > value)
    {
        ptr->next=*head;
        *head=ptr;
    }

    else
    {
        while (1)
    {
        if (temp->next== NULL || temp->next->n > value)
        {
            ptr->next=temp->next;
            temp->next=ptr;
            break;
        }
        
        temp=temp->next;
    }

    }
    return *head;
}