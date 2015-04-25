/*
http://youtu.be/qUgFji4Figw
 */

boolean recdata = true;
boolean data;
int buf[64];
int rc = 0;
#define frontTrig 47
#define frontEcho 49

#define rightTrig A0
#define rightEcho A1

#define backTrig 13
#define backEcho 12

#define leftTrig 7
#define leftEcho 6

#define senFront 40
#define senRight 41
#define senBack 42
#define senLeft 43

#define laser 44

char mode = '0';
int countz = 0;
int countzs = 0;

void setup()
{
  //Sonar
  pinMode(frontTrig, OUTPUT);
  pinMode(frontEcho, INPUT);
  pinMode(rightTrig, OUTPUT);
  pinMode(rightEcho, INPUT);
  pinMode(backTrig, OUTPUT);
  pinMode(backEcho, INPUT);
  pinMode(leftTrig, OUTPUT);
  pinMode(leftEcho, INPUT);
  pinMode(senFront, OUTPUT);
  pinMode(senRight, OUTPUT);
  pinMode(senBack, OUTPUT);
  pinMode(senLeft, OUTPUT);
  digitalWrite(senFront, LOW);
  digitalWrite(senRight, LOW);
  digitalWrite(senBack, LOW);
  digitalWrite(senLeft, LOW);

  Serial.begin(115200);
  Serial1.begin(115200);
}

void loop()
{
  if (Serial.available() > 0) {
    mode = Serial.read();
  }
  //Sonar
  long frontDist = getSonar(frontTrig, frontEcho);
  long rightDist = getSonar(rightTrig, rightEcho);
  long backDist = getSonar(backTrig, backEcho);
  long leftDist = getSonar(leftTrig, leftEcho);
  if (frontDist < 100) {
    digitalWrite(senFront, LOW);
    //countzs = countzs + 1;
    Serial.println("Front");
    //Serial.println(countzs);
  }
  else {
    digitalWrite(senFront, LOW);
  }
  if (rightDist < 100) {
    digitalWrite(senRight, HIGH);
    Serial.println("Right");
  }
  else {
    digitalWrite(senRight, LOW);
  }
  if (backDist < 100) {
    digitalWrite(senBack, LOW);
    Serial.println("Back");
  }
  else {
    digitalWrite(senBack, LOW);
  }
  if (leftDist < 100) {
    digitalWrite(senLeft, LOW);
    //countz = countz + 1;
    Serial.println("Left");
    //Serial.println(countz);
  }
  else {
    digitalWrite(senLeft, LOW);
  }
  delay(500);

  if (digitalRead(laser)) {
    //Laser
    static unsigned long t = 0;
    if (millis() > (t + 2000)) { // Start timer when no data from the sensor
      Serial1.write("*00084553#");
      t = millis();
    }
    getdist();
    if (recdata) t = millis(); // Reset the timer when it receives data from the sensor
  }
}

int getSonar(int trigPin, int echoPin) {
  long duration;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return (duration / 2) / 29.1;
}

void printSonar(int distance) {
  if (!(distance >= 200 || distance <= 0)) {
    Serial.print(distance);
    Serial.println(" cm");
  }
}

int getdist() {
  int litera;

  if (Serial1.available() > 0) {
    while (Serial1.available() > 0) {
      litera = Serial1.read();
      if (litera == 42) { // If adopted by the sign "*"
        data = true;      // then set the sign of the beginning of the packet
      }

      if (litera == 35) { //Если принят знак "#"
        data = false;     //то устанавливаем признак окончания пакета...
        recdata = true;   //и устанавливаем признак получения данных для управления (сбросом) таймера и дальнейшей обработки пакета
      }
      if (data == true && rc < 40 && litera > 47) { //Если есть признак начала пакета, длина пакета в разумных пределах и litera имеет цифровое значение по ASCII, то...
        litera = litera - 48; // Преобразуем ASCII в цифру...
        buf[rc] = litera;  // и добавляем ее в массив.
        rc++;
      }
    }
  }
  else {
    if (recdata == true) {
      boolean dig = true; //Эта переменная будет работать для разделения пакета на разряды по 2 цифры
      int countdata = 0;  //Эта переменная будет считать разряды
      int data = 0;       //Эта переменная будет принимать значения разрядов
      int sum = 0;        //Это сумма всех разрядов за исключения последнего
      int src = 0;        //Это значение последнего разряда (10), в котором прописана контрольная сумма
      int countLaser = 0; //Это значение внутреннего счетчика в 5-м разряде
      int dist = 0;       //Это дистанция, которую мы подсчитаем
      for (int p = 0; p < rc; p++) {
        if (dig) {
          data = buf[p] * 10; //Здесь мы первый знак каждого нового разряда умножаем на 10....
          countdata++;
        }
        else {
          data += buf[p]; //... а здесь к нему прибавляем второе значение.
          if (countdata < 10)sum += data; //здесь подсчитваем контрольную сумму
          if (countdata == 5)countLaser = data; //здесь информация о счетчике
          if (countdata == 7)dist = data * 10000; //здесь считаем дистанцияю---------|
          if (countdata == 8)dist += data * 100; //                                  |
          if (countdata == 9)dist += data; //--------------------------------------|
          if (countdata == 10)src = data; //здесь извлекаем контрольную сумму из пакета
          //Serial.print(data);
          //Serial.print(" ");
          data = 0;
        }
        buf[p] = '\0';
        dig = !dig;
      }

      if (sum >= 100) { //Если контрольная сумма больше 99, то отсекаем лишнее, оставляя только последние два знака
        int a = sum;
        sum = sum / 100;
        sum = sum * 100;
        sum = a - sum;
      }
      if (sum == src) { //Если сумма разрядов (за исключением последнего) равна контрольной сумме (последний разряд) то...
        Serial.print(dist);//Выводим дистанцию и...
        if (countLaser == 99) { //если счетчик достиг предельного значения, то...
          Serial1.write("*00084553#"); //даем команду на начало нового цикла
        }
      }
      src = 0;
      countdata = 0;
      countLaser = 0;
      rc = 0;
      recdata = false;
      Serial.println();
    }
  }
}





