from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('kafka-test', b'Hey! Say my name')
producer.send('test-topic', key=b'message-two', value=b'This is Kafka-Python')
