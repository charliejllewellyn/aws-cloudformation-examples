import boto3
import json
import urllib.parse
import re

client = boto3.client('elastictranscoder')

def getS3ObjectId(event):
    s3Event = json.loads(event['Records'][0]['Sns']['Message'])
    Records = s3Event['Records']
    for eventItem in Records:
        Key = eventItem['s3']['object']['key']
    return str(Key)

def getPipelineId(jobName):
    response = client.list_pipelines()
    for pipeline in response['Pipelines']:
        if pipeline['Name'] == jobName:
            return pipeline['Id']
            
def getPresetId(presetName):
    response = client.list_presets()
    for preset in response['Presets']:
        if preset['Name'] == presetName:
            return preset['Id']

def transcodeAudio(key, pipelineId, presetId):
    decodedKey = urllib.parse.unquote(key)
    newKey = re.sub("\+", " ", decodedKey)
    keyName = newKey.split('.')[0]
    
    response = client.create_job(PipelineId=pipelineId,
                                Input={'Key': newKey},
                                Output={'Key': keyName + '.mp3','PresetId': presetId})
    print(response)
    return(response)

def lambda_handler(event, context):
    key = getS3ObjectId(event)
    pipelineId = getPipelineId('aws-interview')
    presetId = getPresetId('System preset: Audio MP3 - 320k')
    transcodeAudio(key, pipelineId, presetId)
    return

