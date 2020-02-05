#include<stdio.h>
void main()
{
int x,y,a;
a=0;
printf("enter two number:\n");
scanf("%d%d",&x,&y);
if(x>a && y>a)
{
printf("points lie in first quadrant");
}
else if(x<a && y>a)
{
printf("points lie in second quadrant");
}
else if(x<a && y<a)
{
printf("points lie in third quadrant");
}
else if(x>a && y<a)
{
printf("points lie in fourth quadrant");
}
}
