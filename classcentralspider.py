import scrapy
from google.cloud import translate_v2 as translate


class ClassCentralSpider(scrapy.Spider):
    name = "classcentral"
    start_urls = [
        "https://www.classcentral.com/",
    ]

    def parse(self, response):
        # Extract the whole page
        page = response.css("html").get()

        # Translate the page to Hindi
        translate_client = translate.Client.from_service_account_json('/home/giorgi/Downloads/sunlit-hub-228011-840600fdca38.json')
        result = translate_client.translate(page, target_language='hi')

        # Save the translated content to a file
        with open("page_hi.html", "w") as f:
            f.write(result["translatedText"])

        print(u"Text: {}".format(result["input"]))
        print(u"Translation: {}".format(result["translatedText"]))
        print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))