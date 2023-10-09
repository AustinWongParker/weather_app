import python_weather
import asyncio
import os

from twilio.rest import Client
import secret_dont_share

# async def get_weather():
#     async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
#         weather = await client.get('Chicago')

#         message_body = (
#             "The current date is: " + str(weather.current.date) + "\n" +
#             "The current temperature is: " + str(weather.current.temperature) + "\n" +
#             "The current 'feel' of the weather is " + str(weather.current.feels_like) + "\n" +
#             "The current pressure is: " + str(weather.current.pressure) + "\n" +
#             "The current humidity is: " + str(weather.current.humidity) + "\n" +
#             "The current description is: " + weather.current.description + "\n" +
#             "The current precipitation is: " + str(weather.current.precipitation)
#         )


async def sms_weather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Chicago')

        message_body = (
            "From Austin :)"
            "The current date is: " + str(weather.current.date) + "\n" +
            "The current temperature is: " + str(weather.current.temperature) + "\n" +
            "The current 'feel' of the weather is " + str(weather.current.feels_like) + "\n" +
            "The current pressure is: " + str(weather.current.pressure) + "\n" +
            "The current humidity is: " + str(weather.current.humidity) + "\n" +
            "The current description is: " + weather.current.description + "\n" +
            "The current precipitation is: " + str(weather.current.precipitation)
        )

    # Create a Twilio client
    client = Client(secret_dont_share.account_sid, secret_dont_share.auth_token)

    try:
        # Send the message
        message = client.messages.create(
            body=message_body,
            from_=secret_dont_share.from_phone_number,
            to=secret_dont_share.to_phone_number
        )
        print(f"Message sent with SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(sms_weather())