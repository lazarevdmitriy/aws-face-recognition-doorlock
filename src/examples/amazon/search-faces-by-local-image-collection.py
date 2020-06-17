# -*- coding: utf-8 -*-
'''
# Analyzing an Image Loaded from a Local File System
https://docs.aws.amazon.com/en_us/rekognition/latest/dg/images-bytes.html

with open(photo, 'rb') as image:
	response = client.detect_labels(Image={'Bytes': image.read()})

'''

import boto3

if __name__ == "__main__":

    #Replace bucket, collectionId and fileName with your values.
    bucket='amazon-rekognition-service'
    collectionId='EmployeFaceCollection'
    fileName='face.jpg'
    threshold = 70
    maxFaces=2

    client=boto3.client('rekognition')

    with open(fileName, 'rb') as image:
	    response=client.search_faces_by_image(CollectionId=collectionId,
	                                Image={'Bytes': image.read()},
	                                FaceMatchThreshold=threshold,
	                                MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print