#define EPI11 2
#define EPI12 3
#define EPI21 4
#define EPI22 5
#define EPI31 6
#define EPI32 7
#define EPI41 8
#define EP142 9
#define EPI51 10
#define EPI52 11
bool controle = false;
char s;

void setup() {
  Serial.begin(9600);
  for(int i=2; i<14; i++)
  {
    pinMode(i, OUTPUT);
  }
  pinMode(22,OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
   s=Serial.read(); 
  char EPI1 = 'a';
  char EPI2 = 'b';
  char EPI3 = 'c';
  char EPI4 = 'd';
  char EPI5 = 'e';
  char CR_LF = 'z';
  char erro = 'x';

 if(s == ':'){
  controle = true;
 }
 if(controle){
   if(s == EPI1)
   {
      dispenser(EPI11);
   }

   else if(s == EPI2)
   {
      dispenser(EPI21);
   }

   else if(s == EPI3)
   {
      dispenser(EPI31);
   }

   else if(s == EPI4 )
   {
      dispenser(EPI41);
   }

   else if(s == EPI5)
   {
      dispenser (EPI51);
   }
   else if(s == erro){
    digitalWrite(22,1);
   }
 }
  if(s == 'z'){
  controle = false;
  digitalWrite(22,0);
  }
  }
}

void dispenser(int pino)
{
  digitalWrite(pino, 0);
  digitalWrite(pino+1, 1);
  delay(200);
  digitalWrite(pino+1, 0);
  digitalWrite(pino, 1);
  delay(200);
  digitalWrite(pino, 0);
  digitalWrite(pino+1, 0);
}
