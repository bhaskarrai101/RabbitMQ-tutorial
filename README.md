# RabbitMQ-tutorial

## INTRODUCTION

### AMQP :- Advance Message Queuing Protocol
- AMQP is created as an open standard protocol that allow messaging interoperability  between systems, regardless of meaaage broker vendor or platfrom.
- - AMQP is an application layer protocol that lets client application talk to the server and intract.
- This protocol is used for over the wire communication; AMQP is define both the network layer protocol and high level architecture for message brokers.
- It mainly focuses on process to process communication across IP networks.
- AMQP is an encoding schema and a set of procedures allow for two different servers to communicate regardless of the technology used.
- Goal of AMQP is to enable nessage passing through broker services over TCP/IP connection.
- AMQP is considered a compact protocol, since it is a BINARY PROTOCOL, meaning that everything sent over AMQP is binary data.
- A Binary protocol avoids sending useless data over the wire.

### AMQ MODEL
- In this model one client called the PRODUCER which sends a message to an EXCHANGE.
- Exchange then distribute  message copies to QUEUES, depending on rules defined by the exchange type and routing key provided in the message.
- The message is finally consumed by a subscriber/consumer.

# RabbitMQ
- RabbitMQ is an open source message-broker software that originally implemented the Advance Message Queuing Protocol and has since been extended with plug-in architecture to support Streaming Text Oriented Messaging Protocol,Message Queuing Telemetry Transport and other protocols.

## Terminology
- Producing:- It means nothing more than sending. A program that sends messages is a producers.
- Queue :- A queue is the name for a post box which lives inside the rabbitmq.
-  Although messages flow through Rabbitmq and your applications, they can only be stored inside a queue. 
-  A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
- Many producers can send message that go to one queue, and many consumers try to recieve data from one queue. THIS is how we represnt a queue.
-  Consuming is similar meaning to receiving. A consumer is a program that mostly wants to recieve message.
- Exchange and Exchange Types :-  A channel routes messages to a queue depending on the exchange type and bindings between the exchange and the queue. For a queue to receive messages, it must be bound to at least one exchange.
- An exchange can be declared with a number of attributes during creation. For instance, it can be marked as durable so that it survives a broker restart, or it can be marked as auto-delete meaning that it’s automatically deleted when the last queue is unbound.
- Binding :- A binding is a relation between a queue and an exchange consisting of a set of rules that the exchange uses (among other things) to route messages to queues.
- Connection :- A connection is a network connection between your application and the AMQP broker, e.g. a TCP/IP socket connection.
- Channel :- A channel is a virtual connection inside a connection, between two AMQP peers. Message publishing or consuming to or from a queue is performed over a channel (AMQP). A channel is multiplexed, one single connection can have multiple channels.
- Virtual Hosts :- Virtual hosts (vhost) provide a way to segregate applications in the broker. Different users can have different access privileges to different vhost. Queues and exchanges is created so they only exist in one vhost.

## Installation of RabbitMQ on Linux machine.

- Link https://www.rabbitmq.com/install-debian.html
- Choose quick installation using either CLOUDSMITH or PACKAGECLOUD.
- Follow the instructions carefully. 
- - Add Repository Signing Key
- - PackageCloud Quick Start Script
- - Enable apt HTTPS Transport
- - Add a Source List File
- - Distribution {focal} ( i am using Ubuntu 20.04)
- - To add the apt repository to the source list directory
- - -  Ubuntu 20.04 and later releases the above command becomes
- - Install Packages
- - Start the Server [$ sudo service rabbitmq-server start]
- - Check status [$ sudo rabbitmqctl status]
- - Stop the Server [$ sudo service rabbitmq-server stop]









