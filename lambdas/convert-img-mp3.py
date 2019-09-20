import boto3
# import datetime

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # TO DO: grab user name dynamically, sanitize it to meet S3 naming standard
    # user = 'ystoneman'
    # timestamp = datetime.datetime.now().isoformat().replace(':', '').lower()
    # key = user + '/' + timestamp

    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': 'testbucket-rekognition-image-audio-2019-09-20t141633',
                'Name': 'jack-the-giant-killer-by-fwn-bayley-author-of-the-new-tale-of-a-tub-etc-with-4d4051-1024.jpg'
            }
        }
    )
    detections = response.get('TextDetections')
    for line in detections:
        print(line.get('DetectedText'))
