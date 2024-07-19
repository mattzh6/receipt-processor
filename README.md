# receipt-processor

## Instructions

1. To run this program you must first install Docker

2. Next run the command ```docker build -t receipt-processor . ```

3. After building the image and ensuring that port 5050 is not in use as you will be using that port for this application, run the image with this command ``` docker run -d -p 5050:5050 receipt-processor ```

4. Once that is done feel free to test this application by sending HTTP get and post methods.

5. To stop this image I ran ``` docker stop <name> ```

## Assumptions made while working on this project

### Validation checking
I am using Pydantic to validate the fields that are given from requests to my application to ensure that all the required fields are included and that they follow the regex expressions as outlined in the app.yml file.

### Prices
I am also assuming that the total in the receipt and the prices in items can be negative as a customer could be refunding items. Whether this behavior influences the reward points in a negative way could potentially be an issue for the customer if it results in rewards points being taken away.
However, I assume that this is intended as you don't want to give customers free points after they refund items.