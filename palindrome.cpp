#include<stdio.h>
#include<string.h>

void push(char);
char pop();

char s[50]   ,top = -1;

main()
{
    int i ,len ;
    char str[50]  ;
    printf(" \n enter the string:- ");
    scanf("%s",str);
    len =strlen(str);
     i = 0 ;
     
     while( i <len )
    	{
         push(str[i]);
         i++;
     }
     i = 0;
     while(i < len)
     {
         if(str[i] != pop())
         break;
         i++ ;
     }
     
      printf(" \nreversed a string: ");
for(int i =0 ; i< len ; i++)
{
int ch = pop();
printf("%c",ch);
    }
     
     
     if( i == len )
        printf(" \nstring is palindrome");
        
    else
    {
        printf("\n string is not palindrome");
      }    
        
//printf("%c",ch);
    
        
}

void push(char ele)

{
    top ++;
    s[top] = ele ;
}
char pop()
{
    char ele ;
    ele = s[top];
   //
   s[top] = '\0' ;
    top -- ;
    return ele ;
}    
