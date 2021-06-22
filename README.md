### Introduction
    These are multiple serverless websites, either as Examples or for Local Businesses, 
    hosted through Amazon Web Services
    
    Example Websites:
    
    amoghghadge.com
    restaurant.amoghghadge.com
    doctor.amoghghadge.com

    Websites for Local Businesses:

    [To be done]
___________________________________________________________________________________________________

### Hosting
These websites are hosted serverlessly on Amazon Web Services <br>

Each folder in this Repository is the code for a Website

___________________________________________________________________________________________________

### Technical Components
   
- Websites               : Uploaded to an S3 bucket<br>
- Endpoint               : CloudFront provides an HTTPS endpoint to the S3 bucket<br>
- DNS                    : Route 53 points the website domain name to the CloudFront Distribution<br>

___________________________________________________________________________________________________

### Architecture
![Architecture](Website_Backend.png)
