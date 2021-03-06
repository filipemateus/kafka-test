# kafka-test
This documentation contain files and ref used to setup the environment for the test

### Taks

- [x] Create environment in the public cloud (AWS)
- [x] Install Apache Kafka Versão 2.7.0
- [x] Setup Zookepeer with systemd linux service 
- [x] Setup Broker with systemd linux service
- [x] Once the both services up and running, create the topic "test-topic" (kafka-test)
- [x] Create an producer of messages with the programming language of your preference and send a message to the referred topic
- [x] Create an consumer of messages with the programming language of your preference and send a message to the referred topic

### Desirable features (plus)

- [x] Install and setup prometheus and grafana to collect JMX metrics from Kafka
- [x] Show the metric “Under Replicated Partitions” in the Grafana
- [ ] Setup the Zookeeper and broker to secure comunicatitons using Kerberos


### Description 

* For this test I created a EC2 instance and Ubuntu 20.04 linux operacional system.
* All software used (Zookepeer, Aapache Kafka, Prometheus, Grafana, Kafkat) was installed directly on instance's operational system in the systemd
* DNS chosen was https://duckdns.org
* HTTPs by letsencrypt certbot and nginx

### Producing and consuming mensages

Producing hello world
```bash
 echo "Hey, Say my name" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic KafkaTest > /dev/null && echo "Hey, Say my name" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic KafkaTest > /dev/null
```
consuming
```bash
 ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic KafkaTest --from-beginning
```


### Refs

- My github profile - https://github.com/filipemateus
- Kafka-test link - https://github.com/filipemateus/kafka-test
- Apache Kafka - https://kafka.apache.org/quickstart
- Kafka overview grafana dashboard - https://grafana.com/grafana/dashboards/721
- Kafka prometheus grafana - https://github.com/madhur/kafka-promethues-grafana/blob/master/grafana-kafka-dashboard-advanced.json
- Kafka monitpring - https://www.metricfire.com/blog/kafka-monitoring-using-prometheus/
