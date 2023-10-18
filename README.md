# ridership-headline-project
This end to end data engineering / data analytics project will be about the Malaysian public transport ridership data. 

![test drawio](https://github.com/jasontanx/ridership-headline-project/assets/116934441/e2cd3f9f-ec10-4586-9a5d-54d89218d260)

## Starting minio

1. Install minio

2. Create and identify the access key and the secret key

3. Open terminal and key in following
```
minio server start
```

3. Copy the link provided and open the webpage

4. Key in the access key and secret key created earlier

## Files saved at MinIO bucket

<img width="1235" alt="Screenshot 2023-10-05 at 10 44 31 AM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/ee2fc2f7-596a-4480-b48d-f8981839cd35">


## BigQuery ingested data

<img width="1150" alt="Screenshot 2023-10-12 at 1 45 54 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/152e2d21-bc8e-414b-aafc-bcb68393e426">

## Running the script

```
python3 extract_load_minio.py
```
