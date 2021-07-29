# RabbitMQ-tutorial

## INTRODUCTION

### AMQP :- Advance Message Queuing Protocol
- AMQP is created as an open standard protocol that allow messaging interoperability  between systems, regardless of meaaage broker vendor or platfrom.
- - AMQP is an application layer protocol that lets client application talk to the server and intract.
- This protocol is used for over the wire communication; AMQP is define both the network layer protocol and high level architecture for message brokers.
- It mainly focuses on process to process communication across IP networks.
- - AMQP is an encoding schema and a set of procedures allow for two different servers to communicate regardless of the technology used.
- Goal of AMQP is to enable nessage passing through broker services over TCP/IP connection.
- AMQP is considered a compact protocol, since it is a BINARY PROTOCOL, meaning that everything sent over AMQP is binary data.
- A Binary protocol avoids sending useless data over the wire.
- 
### AMQ MODEL
- In this model one client called the PRODUCER which sends a message to an EXCHANGE.
- Exchange then distribute  message copies to QUEUES, depending on rules defined by the exchange type and routing key provided in the message.
- The message is finally consumed by a subscriber/consumer.
- 
# RabbitMQ
- RabbitMQ is an open source message-broker software that originally implemented the Advance Message Queuing Protocol and has since been extended with plug-in architecture to support Streaming Text Oriented Messaging Protocol,Message Queuing Telemetry Transport and other protocols.
## Terminology
- Producing:- It means nothing more than sending. A program that sends messages is a producers.
- Queue:- A queue is the name for a post box which lives inside the rabbitmq.
-  Although messages flow through Rabbitmq and your applications, they can only be stored inside a queue. 
-  A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
- Many producers can send message that go to one queue, and many consumers try to recieve data from one queue. THIS is how we represnt a queue.
-  Consuming is similar meaning to receiving. A consumer is a program that mostly wants to recieve message.
## Installation of Rabbit Mq on Linux machine.
1. First update your machine use code, $ sudo apt-get update
2. Befor you install rabbitmq you have to install erlang, $ sudo apt-get install erlang
3. Run, $ sudo apt install apt-transport-https -y
4. Now install rabbitmq-server, $ sudo apt install rabbitmq-server
5. Start rabbitmq server, $ sudo systemctl start rabbitmq-server.service
6. Check status, $ sudo systemctl status rabbitmq-server.service
7. Enabling the server, $  sudo systemctl is-enabled rabbitmq-server.service
8. Enabling plugins, $ sudo rabbitmq-plugins enable rabbitmq_management
9. $ sudo netstat -tunelp | grep 15672
10.$ sudo apt install net-tools
11.$ pip install pika 








