### Introduction
    Multiple serverless websites, either as Examples or for Local Companies, hosted through
    Amazon Web Services
    
    Websites:
    
    www.amoghghadge.com
    restaurant.amoghghadge.com
    doctor.amoghghadge.com
___________________________________________________________________________________________________

### Hosting
##### These websites are hosted on Amazon Web Services

___________________________________________________________________________________________________

### Technical Components
   
- Source Code            : Packaged and deployed on AWS Lambda<br>
- Website                : Uploaded to an S3 bucket<br>
- API                    : API Gateway invokes the lambda function when the button on the website is pressed<br>
- Messaging              : AWS SNS is used to send the SMS text message to the phone numbers<br>
- Application Endpoint   : CloudFront provides an HTTPS endpoint to the backend<br>
- DNS                    : Route 53 points opm.amoghghadge.com to the CloudFront Distribution<br>

___________________________________________________________________________________________________

### Architecture
![Architecture](Website_Backend.png)
