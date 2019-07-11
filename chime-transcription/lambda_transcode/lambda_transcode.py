Uploading to 88e6b747c723f29112eaf3c2b8b85bb2  1243 / 1243.0  (100.00%)
AWSTemplateFormatVersion: '2010-09-09'
Description: An AWS Serverless Specification template describing your function.
Resources:
  SNSTopic1:
    Type: AWS::SNS::Topic
  testsns:
    Properties:
      CodeUri: s3://cjl-lambda-functions/88e6b747c723f29112eaf3c2b8b85bb2
      Description: ''
      Events:
        SNS1:
          Properties:
            Topic:
              Ref: SNSTopic1
          Type: SNS
      Handler: lambda_function.lambda_handler
      MemorySize: 128
      Role: arn:aws:iam::008369042577:role/lambdaTranscribe
      Runtime: python3.6
      Timeout: 3
    Type: AWS::Serverless::Function
Transform: AWS::Serverless-2016-10-31
