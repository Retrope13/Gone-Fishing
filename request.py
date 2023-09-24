import requests
import handle
import boto3


s3 = boto3.client('s3', region_name='us-west-2')


def request_API(army):
    try:
        response = get_s3()
        print(response)
        dump_s3()
        ##See if the name that is contained in the bucket is jenny, sam, or paul and then flip the necessary card.
        if response.lower() == 'jenny' or response.lower() == 'jenny\'s':
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
        elif response.lower() == 'paul' or response.lower() == 'paul\'s':
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
        elif response.lower() == 'sam' or response.lower() == 'sam\'s':
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            
            
        elif any(keyword in response.lower() for keyword in ['sam jenny', 'sam\'s jenny\'s', 'sam and jenny', 'sam\'s and jenny\'s', 'sam and jenny\'s']):
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
            
        elif any(keyword in response.lower() for keyword in ['jenny sam', 'jenny\'s sam\'s', 'jenny and sam', 'jenny\'s and sam\'s', 'jenny and sam\'s']):
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
            
            
        elif any(keyword in response.lower() for keyword in ['sam paul', 'sam\'s paul\'s', 'sam and paul', 'sam\'s and paul\'s', 'sam and paul\'s']):
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
            
        elif any(keyword in response.lower() for keyword in ['paul sam', 'paul\'s sam\'s', 'paul and sam', 'paul\'s and sam\'s', 'paul and sam\'s']):
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
            
        elif any(keyword in response.lower() for keyword in ['jenny paul', 'jenny\'s paul\'s', 'jenny and paul', 'jenny\'s and paul\'s', 'jenny and paul\'s']):
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
            
        elif any(keyword in response.lower() for keyword in ['paul jenny', 'paul\'s jenny\'s', 'paul and sam', 'paul\'s and sam\'s', 'paul and sam\'s']):
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
        
        elif response.lower() == 'all' or response.lower() == 'all cards':
            handle.handle_message('sammckay31@gmail.com', '', '', army)
            handle.handle_message('thepaulmckay@gmail.com', '', '', army)
            handle.handle_message('thejennymckay@gmail.com', '', '', army)
            
        else:
            pass
    except: 
        return False
    
    return True


def get_s3():
    ## find the bucket and retrieve the name that is contained within it.
    bucket_name = 'frogflipbucket'
    object_key = 'names/doc.txt'
    response = s3.get_object(
        Bucket=bucket_name,
        Key=object_key
    )
    
    data = response['Body'].read()
    return data.decode('utf-8')


def dump_s3():
    #find the bucket and clear it to prevent an infinite loop of card flipping
    bucket_name = 'frogflipbucket'
    object_key = 'names/doc.txt'
    s3.put_object(
        Bucket=bucket_name,
        Key=object_key,
        Body=''
    )

if __name__ == "__main__":

     ##just for testing purposes
    get_s3()