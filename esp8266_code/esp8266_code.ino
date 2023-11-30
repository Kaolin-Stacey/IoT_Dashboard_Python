#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <SPI.h>
#include <MFRC522.h>

const char *ssid = "kaolin-phone";
const char *password = "ConcreteBrick2018";
const char *mqtt_server = "192.168.238.253";

const int ldrPin = A0;
#define SS_PIN D8  // Set the SS pin for the RFID module
#define RST_PIN D0 // Set the RST pin for the RFID module

WiFiClient espClient;
PubSubClient client(espClient);

MFRC522 rfid(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  SPI.begin();
  rfid.PCD_Init();
}

void loop() {
  // Read lumens from photorealistic sensor
  int lumens = analogRead(ldrPin);
  String rfidData = "";

  // Read RFID data
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    Serial.println("RFID card detected!");

    // Get RFID card UID
    for (byte i = 0; i < rfid.uid.size; ++i) {
      rfidData += String(rfid.uid.uidByte[i], HEX);
    }


    // Halt for a moment to avoid reading the same card multiple times
    delay(1000);
  }

  if (client.connect("ESP8266Client")) {
      Serial.println("MQTT Connected");
      client.publish("IoT/lumens", String(lumens).c_str());
      if (rfidData != "") {
        client.publish("IoT/rfid", rfidData.c_str());
      }
      client.disconnect();
  }

  client.loop();
  delay(2000); // Adjust the delay based on your requirements
}

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
}
