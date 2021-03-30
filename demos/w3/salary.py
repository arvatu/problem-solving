#include <stdio.h>

void salary(){
  //Decide if an employee will get a pay rise based on their current salary and who they are

char f_init, s_init;
float salary;

printf("Enter your initials: ");
scanf("%c%c",&f_init,&s_init);
printf("What's your current salary?\n");
scanf("%f", &salary);

if (salary < 25000){
  //increase salary of lower earners by 10%
  salary = 1.1*salary;
  printf("Congratulations! You got a 10%% salary increase!\n Your new salary is £%.2f", salary);

  } else if ((salary < 50000 ) || (f_init == 'p' && s_init == 'b')){
  //salary will be increased by 5% if the employee has initials pb or their salary is lower than 50000
  salary = 1.05*salary;
  printf("Congratulations! You got a 5%% salary increase!\n Your new salary is £%.2f", salary);
  
} else{
  printf("No rise for you, I am afraid!");
}
// suggest in chat, which two initals and what salary will force my code into lines 24-26 (getting 10% increase)
}