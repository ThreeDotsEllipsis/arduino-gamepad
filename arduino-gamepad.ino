bool holdingX = false;
bool holdingY = false;
bool holdingButton = false;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
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
