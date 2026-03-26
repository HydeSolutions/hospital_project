To create Kafka Topics Using create_topic.bat file

create_topic.bat orders 6 1

echo Usage: create-topic.bat ^<topic-name^> [partitions] [replication]
echo Example: create-topic.bat patient-admissions 3 1

where order is the name of the topic, 6 is the number of partitions and 1 is the replication factor

Usage 

create_topic.bat hospital-events 4 1
list_all_topics.bat
describe_topic.bat hospital-events
