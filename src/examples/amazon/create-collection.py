# -*- coding: utf-8 -*-
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

    # Replace collectionID with the name of the collection that you want to create.
    maxResults = 2
    collectionId = 'EmployeFaceCollection'

    # Create a collection
    print('Creating collection:' + collectionId)

    client=boto3.client('rekognition')
    response = client.create_collection(CollectionId=collectionId)

    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
'''
source venv/bin/activate
subl
 
Creating collection:EmployeFaceCollection
Collection ARN: aws:rekognition:eu-central-1:119212719574:collection/EmployeFaceCollection
Status code: 200
Done...
'''
