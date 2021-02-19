#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct Shop {
    int code;///////Code number of product/////
	float price;//////price of the product////////
	float t;//////total price of the product////////
	struct Shop *next;////pointer///////
};
typedef struct Shop shop;//shorting the pointer//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void insertLast(shop *current) /// Function to insert code and price///
   {
	shop *temp = (shop *)malloc(sizeof(shop));
	printf("Enter the code:");
	scanf("%d",&temp->code);
	printf("Enter the price:");
	scanf("%f",&temp->price);

	temp->next = '\0';
	while (current->next != '\0')
		current = current->next;
	current->next = temp;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void insertUser(shop*current) /// Function to insert quantity and code ///
{
    int quantity;
    int code;
    printf("Enter the code:");
    scanf("%d",&code);
    printf("Enter the quantity:");
    scanf("%d",&quantity);
    while (current->next!='\0')
    {
        if (current->code==code)
        {
            current->t=current->price*quantity;
        }
        current=current->next;
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void display(shop *current) /// Function to display code and price///
 {
	while (current != '\0') {
		printf("code=%d\tprice=%.2f Taka\n", current->code,current->price);
		current = current->next;
	}
	printf("\n");
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void displayUser(shop *current) ///Function to display code price and total///
   {
	while (current != '\0') {
		printf("code=%d \tprice=%.2f Taka\ttotal=%.2f\n", current->code,current->price,current->t);
		current = current->next;
	}
	printf("\n");
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void totalsum (shop*current) ///Function for summing the total///
{
    float s=0;
    while (current!='\0')
    {
        s=s+current->t;///////////// NOT working ///////////////////
        current=current->next;
    }
    printf("------------------------------\n");
    printf("total price is %.2f\n",s);
    s=0;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void delete(shop *list)///Function to delete a product ///
{
    if (list->next == '\0')
        {
		printf("There is no products!\nEnter your option:\n");
		return;
	}
	int data;
	printf("Enter the product code that you want to delete\n");
	scanf("%d",&data);

    while (list->next != NULL)
    {
        if(list->next->code == data)
        {
           list->next = list->next->next;
           printf("%d is deleted!\nEnter your option:\n",data);
           free(list->next);
            return;
        }
        list = list->next;
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void main() {
	shop *head = (shop *)malloc(sizeof(shop));/// header pointer///
	head->next = '\0';
    printf("**********************************************\n");
    printf("**********************************************\n");
    printf("**     ! OOOOOOOOOOOOOOOOOOOOOOOOO !        **\n");
    printf("**^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^**\n");
    printf("**     !                           !        **\n");
    printf("**     ! WELCOME TO DIU SUPER SHOP !        **\n");
    printf("**     !                           !        **\n");
    printf("**^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^**\n");
    printf("**     ! OOOOOOOOOOOOOOOOOOOOOOOOO !        **\n");
    printf("**********************************************\n");
    printf("Press any key to continue:");
    getch();
    system("cls");/// Clear display///
      while(1)/// loop for password///
   {
       int password;
       printf("-----------------------\n");
       printf("-----------------------\n");
       printf("--Enter your password--\n");
       printf("-----------------------\n");
       printf("-----------------------\n");
    scanf("%d",&password);
    while (1){
        if (password==123)break;
        else
            printf("Wrong password,try again\n");
            scanf("%d",&password);
    }printf("access granted!\nEnter your option:\n");
    break;

   }
   printf("press 1 for admin\npress 2 display\npress 3 to user\npress 4 to display price\npress 5 to clean display\npress 6 to Factorial reset!\n");
    while (1){
    int a;
     scanf("%d",&a);
     if (a==1)
     {
         printf("Press 1 to insert product \nPress 2 to delete product\n");
     int ab;
     scanf("%d",&ab);
     if (ab==1)
     {
	int i,m;
	printf("Enter how many products:\n");
	scanf("%d",&m);
	for(i=0;i<m;i++){
            insertLast(head);
	}printf("Enter your option:\n");
     }if (ab==2){
     delete(head);
     }
     }

	if (a==2){
	display(head->next);
     printf("Enter your option:\n");
     }
     if (a==3)
        {printf("Enter how many products:");
     int p,k;
     scanf("%d",&p);
        for (k=0;k<p;k++)
        {insertUser(head);
     }printf("Enter your option:\n");}
	if (a==4){
        displayUser(head->next);
	totalsum(head->next);printf("Enter your option:\n");
	}
	if (a==5){
    system("cls");
    printf("press 1 for admin\npress 2 display\npress 3 to user\npress 4 to display price\npress 5 to clean display\npress 6 to Factorial reset!\nEnter your option:\n");
    }
    if (a==6)
        return;
}
}
