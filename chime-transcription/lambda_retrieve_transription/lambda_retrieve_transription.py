import boto3
import json
import datetime
import re

transcribeClient = boto3.client('transcribe')

def putStatusSns(transcribeResponse):
    sns = boto3.client('sns')
    topics = sns.list_topics()
    for arn in topics['Topics']:
        if re.match(".*cjl-transcribe-job-status$", arn['TopicArn']):
            arn = arn['TopicArn']
    snsResponse = sns.publish(TopicArn=arn, Message=json.dumps(response))
    print(snsResponse)
    
def checkTranscribeStatus(event):
    jobDetails = event['Records'][0]['Sns']['Message']
    transcribeDetails=json.loads(jobDetails)['TranscriptionJob']
    transcribeResponse = transcribeClient.get_transcription_job(TranscriptionJobName=transcribeDetails['TranscriptionJobName'])
    if transcribeResponse['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        print(transcribeResponse['TranscriptionJob']['Transcript']['TranscriptFileUri'])
    elif transcribeDetails['TranscriptionJob']['TranscriptionJobStatus'] == 'IN_PROGRESS':
        putStatusSns(transcribeResponse)
    else:
        print(TranscriptionJob)
    
def lambda_handler(event, context):
    checkTranscribeStatus(event)
    # TODO implement
    return 'Hello from Lambda'

