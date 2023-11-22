import boto3
# Initialize AWS resources
dynamodb = boto3.resource('dynamodb') s3 = boto3.client('s3')
bucket_name = 'your_s3_bucket_name' # DynamoDB table name
table_name = 'books'
table = dynamodb.Table(table_name) def lambda_handler(event, context):
# Get the HTTP method and path from the event http_method = event['httpMethod']
path = event['path']
# Handle different routes
if http_method == 'GET' and path == '/movies': # Retrieve all movies from DynamoDB table response = table.scan()
movies = response['Items'] return {
'statusCode': 200, 'body': {
'movies': movies
}
}
elif http_method == 'GET' and path.startswith('/movie/'): # Extract movie ID from the path
book_id = path.split('/')[-1]
# Retrieve movie details from DynamoDB response = table.get_item(Key={'id': movie_id}) movie = response.get('Item')

if http_method == 'GET' and path == '/movies': # Retrieve all movies from DynamoDB table response = table.scan()
books = response['Items'] return {
'statusCode': 200, 'body': {
'moviess': movie
}
}
elif http_method == 'GET' and path.startswith('/movie/'): # Extract movie ID from the path
book_id = path.split('/')[-1]
# Retrieve movie details from DynamoDB response = table.get_item(Key={'id': book_id}) book = response.get('Item')
# Generate a unique ID for the movie
# You may use a UUID or any other method to generate a unique ID id = generate_unique_id()
# Upload movie image to S3 image_file = body['image']
s3.upload_fileobj(image_file, bucket_name, f'images/{id}.jpg') image_url = f'https://{bucket_name}.s3.amazonaws.com/images/{id}.jpg' # Add movie details to DynamoDB
table.put_item( Item={
'id': id, 'title': title,
'author': author, 'description': description,

'image_url': image_url
}
)


}
else:

return { 'statusCode': 201,
'body': 'Movie added successfully'

return {
'statusCode': 404, 'body': 'Route not found'
}
