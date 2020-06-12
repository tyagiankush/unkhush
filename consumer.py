def consumer():
    try:
        from kafka import KafkaConsumer
        consumer = KafkaConsumer('first_topic',
                                 bootstrap_servers=['127.0.0.1:9092'],
                                 group_id='group_1',
                                 auto_offset_reset='earliest')
        print('here1')
        #consumer.subscribe(list('first_topic'))
        for message in consumer:
            print('in')
            print(message.value)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    consumer()
