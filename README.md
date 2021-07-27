# RabbitMQ-tutorial
-  AMQP :- Advance Message Queuing Protocol
-          It is a messaging protocol that enables conforming client applictions to communicate with conforming messaging middleware brokers.
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








