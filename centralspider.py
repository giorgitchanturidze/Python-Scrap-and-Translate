import scrapy
from google.cloud import translate_v2 as translate


class ClassCentralSpider(scrapy.Spider):
    name = "central"
    start_urls = [
        "https://www.classcentral.com/",
    ]

    def parse(self, response):
        # Extract the whole page
        page = response.css("html").get()

        # Split the page content into chunks of 10,000 characters
        chunks = [page[i:i+10000] for i in range(0, len(page), 10000)]

        # Translate each chunk separately
        translate_client = translate.Client.from_service_account_json('/home/giorgi/Downloads/sunlit-hub-228011-840600fdca38.json')
        translated_chunks = []
        for chunk in chunks:
            result = translate_client.translate(chunk, target_language='hi')
            translated_chunks.append(result["translatedText"])

        # Combine the translated chunks into a single string
        translated_page = ''.join(translated_chunks)

        # Save the translated content to a file
        with open("page_hi.html", "w") as f:
            f.write(translated_page)

        print(u"Text: {}".format(page))
        print(u"Translation: {}".format(translated_page))
        print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
