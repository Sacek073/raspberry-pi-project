# Docker image for running webpage and receiver

## How to use

- In order to not duplicate files in the github follow these instructions:
1. Copy the Web directory to this directory: `cp -r ../Web .`
2. Build the image: `sudo docker build -t <Image> .`
3. Run the image: `sudo docker run --name <Container> --network=host -p 5000:5000 <Image>`

Přidat do webové stránky nastavení ip adresy MQTT brokera
