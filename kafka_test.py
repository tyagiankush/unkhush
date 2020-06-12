import sys,json
def producer():
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', api_version=(2,5,0))
    print('here')
    producer.send('first_topic', b'Hello, World!')
    producer.send('first_topic', key=b'message-two', value=b'This is Kafka-Python')
    #producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    #producer.send('first_topic', {'foo': 'bar'})
    print('here a')
    producer.flush()





if __name__ == '__main__':
    producer()
