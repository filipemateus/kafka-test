from kafka import KafkaConsumer
consumer = KafkaConsumer('test-topic')
for message in consumer:
    print (message)
