bool holdingX = false;
bool holdingY = false;
bool holdingButton = false;

void handle_y()
{
  if(analogRead(5) == 0)
  {
    if(!holdingY)
    {
      holdingY = true;
      Serial.println('s');
    }
  }
  else if(analogRead(5) == 1023)
  {
    if(!holdingY)
    {
      holdingY = true;
      Serial.println('w');
    }

  }
  else
  {
    if(holdingY)
    {
      Serial.println("ye");
    }
    holdingY = false;

  }  
}

void handle_x()
{
  
  if(analogRead(4) == 0)
  {
    if(!holdingX)
    {
      holdingX = true;
      Serial.println('a');
    }
  }
  else if(analogRead(4) == 1023)
  {
    if(!holdingX)
    {
      holdingX = true;
      Serial.println('d');
    }

  }
  else
  {
    if(holdingX)
    {
      Serial.println("xe");
    }
    holdingX = false;

  }
}

void handle_buttons()
{
  int num = analogRead(0);
  if(num > 334)
  {
    if(!holdingButton)
    {
      holdingButton = true;
      Serial.println(num);
    }

  }
  else
  {
    if(holdingButton)
    {
      Serial.println("be");
    }
    holdingButton = false;
  }
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  handle_y();
  handle_x();
  handle_buttons();
}
