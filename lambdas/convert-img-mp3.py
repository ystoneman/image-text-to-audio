import boto3
import os
# import datetime

rekognition = boto3.client('rekognition')
polly = boto3.client('polly')

def lambda_handler(event, context):
    # TO DO: grab user name dynamically, sanitize it to meet S3 naming standard
    # user = 'ystoneman'
    # timestamp = datetime.datetime.now().isoformat().replace(':', '').lower()
    # key = user + '/' + timestamp

    detections = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': os.environ['BUCKET'],
                'Name': 'jack-the-giant-killer-by-fwn-bayley-author-of-the-new-tale-of-a-tub-etc-with-4d4051-1024.jpg'
            }
        }
    ).get('TextDetections')
    story = ''
    for line in detections:
        story = story + line.get('DetectedText') + '\n'
    print(story)
    # Later on save text in S3 too. For now just send straight to Polly

    response = polly.start_speech_synthesis_task(
        LanguageCode='en-US',
        OutputFormat='mp3',
        Text=story,
        VoiceId='Amy',
        OutputS3BucketName='testbucket-rekognition-image-audio-2019-09-20t141633'
    )

    # next: email the mp3 to myself
