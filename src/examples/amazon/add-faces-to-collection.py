# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


import boto3

if __name__ == "__main__":
    # replace bucket, collectionId, and photo with your values.
    bucket='amazon-rekognition-service'
    collectionId='EmployeFaceCollection'
    photo='_IGP3800-1.jpg'
    
    client=boto3.client('rekognition')

    response=client.index_faces(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                ExternalImageId=photo,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    print ('Results for ' + photo) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)

'''
Results for _IGP3800-1.jpg
Faces indexed:
  Face ID: 96a8511d-fa47-427c-8516-318e48d4e9f6
  Location: {'Width': 0.1280091553926468, 'Height': 0.11858101934194565, 'Left': 0.36170050501823425, 'Top': 0.09981244802474976}
Faces not indexed:
 Location: {'Width': 0.053480081260204315, 'Height': 0.04408653452992439, 'Left': 0.8959308862686157, 'Top': 0.10316330194473267}
 Reasons:
   EXCEEDS_MAX_FACES
 Location: {'Width': 0.05014534667134285, 'Height': 0.04032258316874504, 'Left': 0.6875569224357605, 'Top': 0.243059441447258}
 Reasons:
   EXCEEDS_MAX_FACES
[Finished in 2.1s]
'''