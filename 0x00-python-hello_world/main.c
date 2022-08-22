#include "lists.h"

int main()
{
    listint_t *head = malloc(sizeof(listint_t));
    listint_t *check = malloc(sizeof(listint_t));
    head->n= 60;
    head->next=NULL;
    check->n = 70;
    check->next=NULL;
    head->next=check;
    check=malloc(sizeof(listint_t));
    check->n=80;
    check->next=NULL;
    head->next->next=check;

    printf("%d\n",check_cycle(head));
    return (0);
}
