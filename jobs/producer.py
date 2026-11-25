import io

from minio import S3Error

def main ():


if __name__ == "__main__":
    try:
        main()
    except S3Error as e:
        print('Error accurred. ', e) 