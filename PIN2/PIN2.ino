#include <Keypad.h>

int ledPin = 13;  // Pin where the LED is connected

// Define the keypad layout
const byte ROWS = 4;  // four rows
const byte COLS = 4;  // four columns
char keys[ROWS][COLS] = {
  {'D', 'C', 'B', 'A'},
  {'#', '9', '6', '3'},
  {'0', '8', '5', '2'},
  {'*', '7', '4', '1'}
};

// Define the row and column pins
byte rowPins[ROWS] = {2, 3, 4, 5};  // Connect to the row pinouts of the keypad
byte colPins[COLS] = {6, 7, 8, 9};  // Connect to the column pinouts of the keypad

// Create the keypad object
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Define the correct PIN code
const String correctPIN = "1234";
String inputPIN;

void setup() {
  pinMode(ledPin, OUTPUT);  // Set the LED pin as an output
  Serial.begin(9600);
  Serial.println("Enter your PIN:");
}

void loop() {
  char key = keypad.getKey();

  if (key) {
    // If a key is pressed
    if (key == '#') {
      // Check the PIN when # is pressed
      if (inputPIN == correctPIN) {
        Serial.println("Access Granted!");
        digitalWrite(ledPin, HIGH);  // Turn on the LED
        delay(2000);  // Wait for 2 seconds
        digitalWrite(ledPin, LOW);  // Turn off the LED
      } else {
        Serial.println("Access Denied!");
      }
      inputPIN = "";  // Clear the input after checking
      Serial.println("Enter your PIN:");
    } else if (key == '*') {
      // Clear the input when * is pressed
      inputPIN = "";
      Serial.println("Input cleared. Enter your PIN:");
    } else {
      // Append the pressed key to the input PIN
      inputPIN += key;
      Serial.print("Current input: ");
      Serial.println(inputPIN);
    }
  }
}
