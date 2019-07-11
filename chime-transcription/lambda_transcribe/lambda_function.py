import boto3
import time
import json
import re

def getS3ObjectId(event):
    s3Event = json.loads(event['Records'][0]['Sns']['Message'])
    Records = s3Event['Records']
    for eventItem in Records:
        Key = eventItem['s3']['object']['key']
        Bucket = eventItem['s3']['bucket']['name']
    s3 = boto3.client('s3')
    mediaUrl = 'https://s3.amazonaws.com/' + str(Bucket) + '/' + str(Key)
    return mediaUrl

def putStatusSns(transcribeResponse):
    transcribeResponse['TranscriptionJob']['CreationTime'] = None
    transcribeResponse['TranscriptionJob']['CompletionTime'] = None
    sns = boto3.client('sns')
    topics = sns.list_topics()
    for arn in topics['Topics']:
        if re.match(".*cjl-transcribe-job-status$", arn['TopicArn']):
            snsResponse = sns.publish(TopicArn=arn['TopicArn'], Message=json.dumps(transcribeResponse))
    print(snsResponse)

def createTranscription(mediaUrl):
    client = boto3.client('transcribe')
    response = client.start_transcription_job(
        TranscriptionJobName='LambdaTest' + str(time.time()),
        LanguageCode='en-US',
        MediaSampleRateHertz=44100,
        MediaFormat='mp3',
        Media={
            'MediaFileUri': mediaUrl
        }
    )
    time.sleep(30)
    print('Writing message to SNS')
    putStatusSns(response)
    return response

def lambda_handler(event, context):
    mediaUrl = getS3ObjectId(event)
    print(createTranscription(mediaUrl))
    return 'Hello from Lambda'
