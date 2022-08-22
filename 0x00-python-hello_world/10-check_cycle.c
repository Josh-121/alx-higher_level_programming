#include "lists.h"
int check_cycle(listint_t *list)
{
 listint_t *ptr = NULL;
 listint_t *check = NULL;
 int i=0;
 int j=0;
 int num=0;

 ptr = list;
 check==list;
 while (ptr != NULL)
 {
    i++;
    ptr=ptr->next;
    while (j<i && check != NULL)
    {
        if (check == ptr)
        {
           num=1;
           break;
        }
        check=check->next;
        j++;
    }
    if (num==1)
        break;
    check=list;
    j=0;
 } 
 return num;  
}
